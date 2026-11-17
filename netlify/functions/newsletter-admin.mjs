// Admin commands, run from Terminal with curl. Only works with the key saved in
// Netlify as NEWSLETTER_ADMIN_KEY; without that variable it is switched off.
//
//   ?action=count                  how many readers (active, waiting for confirmation)
//   ?action=list                   all addresses with their status
//   ?action=import&exclude=a,b     body: follow.it CSV export (or one address per line)
//   ?action=remove&email=x         delete one reader
//   ?action=test&to=x              send the newest post or puzzle to x only
//   ?action=test-moved&to=x        send the "newsletter has moved" email to x only
//   ?action=moved-notice           send that email once to every reader imported from follow.it
//   ?action=send-now[&dry=1]       announce what's new right away (dry=1: only show what would go out)
import { store, sender, safe, json } from "../lib/runtime.mjs";
import {
  allSubscribers, announce, fetchFeed, importList, movedMail, normEmail, removeSubscriber,
  sameSecret, sendMovedNotice, updateMail, validEmail,
} from "../lib/newsletter.mjs";

const PREVIEW_TOKEN = "0".repeat(40);   // test mails: the unsubscribe link just shows "unsubscribed"

export default async (request) => {
  const key = Netlify.env.get("NEWSLETTER_ADMIN_KEY");
  const given = (request.headers.get("authorization") || "").replace(/^Bearer\s+/i, "");
  if (!key) return json({ error: "not found" }, 404);
  if (!sameSecret(given, key)) return json({ error: "wrong key" }, 401);

  const params = new URL(request.url).searchParams;
  const action = params.get("action") || "count";
  const s = store();
  try {
    switch (action) {
      case "count": {
        const all = await allSubscribers(s);
        return json({ active: all.filter((r) => r.status === "active").length, waiting: all.filter((r) => r.status === "pending").length });
      }
      case "list": {
        const all = await allSubscribers(s);
        return json(all.map(({ email, status, source, created }) => ({ email, status, source, since: created?.slice(0, 10) })));
      }
      case "import": {
        const exclude = (params.get("exclude") || "").split(",").filter(Boolean);
        return json(await importList({ store: s, csv: await request.text(), exclude }));
      }
      case "remove": {
        return json({ removed: await removeSubscriber(s, params.get("email") || "") });
      }
      case "test":
      case "test-moved": {
        const to = normEmail(params.get("to"));
        if (!validEmail(to)) return json({ error: "add &to=your address" }, 400);
        const record = { email: to, token: PREVIEW_TOKEN };
        let mail;
        if (action === "test") {
          const feed = await fetchFeed();
          const newest = [...(feed.posts || []), ...(feed.puzzles || [])].sort((a, b) => Date.parse(b.date) - Date.parse(a.date))[0];
          if (!newest) return json({ error: "nothing on the site to send" }, 400);
          mail = updateMail(record, [newest]);
        } else {
          mail = movedMail(record);
        }
        await sender().one(mail);
        return json({ sent: 1, subject: mail.subject });
      }
      case "moved-notice":
        return json(await sendMovedNotice({ store: s, send: sender() }));
      case "send-now":
        return json(await announce({ store: s, send: sender(), feed: await fetchFeed(), dryRun: params.get("dry") === "1" }));
      default:
        return json({ error: `unknown action ${action}` }, 400);
    }
  } catch (error) {
    return json({ error: safe(error) }, 500);
  }
};

export const config = { path: "/api/newsletter-admin", method: "POST" };
