// Every morning (16:00 UTC, 8 AM in Redmond) look for posts and Puzzles of the Month
// that went live since the last run and email them to the confirmed readers.
// The first run only remembers what is already on the site and sends nothing.
import { store, sender, safe } from "../lib/runtime.mjs";
import { announce, fetchFeed } from "../lib/newsletter.mjs";

export default async () => {
  try {
    const result = await announce({ store: store(), send: sender(), feed: await fetchFeed() });
    console.log("newsletter:", JSON.stringify({ ...result, items: result.items?.length }));
  } catch (error) {
    console.error("newsletter send failed:", safe(error));
  }
};

export const config = { schedule: "0 16 * * *" };
