// /newsletter/confirm/?t=... posts the token here. A POST, not a GET, so mail scanners
// that open links can't confirm on someone's behalf.
import { store, safe, toPage, json, tokenFrom, wantsJson } from "../lib/runtime.mjs";
import { confirm } from "../lib/newsletter.mjs";

export default async (request) => {
  let state = "error-busy";
  try {
    state = await confirm({ store: store(), token: await tokenFrom(request) });
  } catch (error) {
    console.error("newsletter confirm failed:", safe(error));
  }
  return wantsJson(request) ? json({ state }) : toPage(state);
};

export const config = { path: "/api/confirm", method: "POST" };
