// Unsubscribe: from the page /newsletter/unsubscribe/?t=..., or straight from the mail
// app's own "Unsubscribe" button (List-Unsubscribe-Post, RFC 8058). Deletes the address.
import { store, safe, toPage, json, tokenFrom, wantsJson } from "../lib/runtime.mjs";
import { unsubscribe } from "../lib/newsletter.mjs";

export default async (request) => {
  const oneClick = (request.headers.get("content-type") || "").includes("form") &&
    !wantsJson(request) && new URL(request.url).searchParams.has("t");
  let state = "unsubscribed";
  try {
    state = await unsubscribe({ store: store(), token: await tokenFrom(request) });
  } catch (error) {
    console.error("newsletter unsubscribe failed:", safe(error));
    state = "error-busy";
  }
  if (wantsJson(request)) return json({ state });
  if (oneClick) return new Response("Unsubscribed.", { status: state === "unsubscribed" ? 200 : 500 });
  return toPage(state);
};

export const config = { path: "/api/unsubscribe", method: "POST" };
