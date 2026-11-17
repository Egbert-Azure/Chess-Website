// Newsletter sign-up form (/newsletter/) posts here. Sends the confirmation email.
import { store, sender, safe, toPage } from "../lib/runtime.mjs";
import { subscribe } from "../lib/newsletter.mjs";

export default async (request) => {
  let email = "", honeypot = "";
  try {
    const form = await request.formData();
    email = form.get("email");
    honeypot = form.get("website");
  } catch { /* empty or broken form */ }
  try {
    return toPage(await subscribe({ store: store(), send: sender(), email, honeypot }));
  } catch (error) {
    console.error("newsletter subscribe failed:", safe(error));
    return toPage("error-busy");
  }
};

export const config = { path: "/api/subscribe", method: "POST" };
