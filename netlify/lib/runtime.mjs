// Netlify-side helpers for the newsletter functions: the Blobs store, the Resend
// sender from environment variables, and small response helpers.
import { getStore } from "@netlify/blobs";
import { resendSender } from "./newsletter.mjs";

export const store = () => getStore({ name: "newsletter", consistency: "strong" });

export function sender() {
  const apiKey = Netlify.env.get("RESEND_API_KEY");
  const from = Netlify.env.get("NEWSLETTER_FROM");
  if (!apiKey || !from) throw new Error("RESEND_API_KEY and NEWSLETTER_FROM must be set in Netlify");
  return resendSender({ apiKey, from, replyTo: Netlify.env.get("NEWSLETTER_REPLY_TO") || undefined });
}

// Logs never contain email addresses.
export const safe = (error) => String(error?.message || error).replace(/[^\s"'<>]+@[^\s"'<>]+/g, "<address>");

export const toPage = (state) =>
  new Response(null, { status: 303, headers: { Location: `/newsletter/?state=${encodeURIComponent(state)}` } });

export const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });

// The token comes in the query string (?t=...) or, from a plain form, in the body.
export async function tokenFrom(request) {
  const url = new URL(request.url);
  let token = url.searchParams.get("t");
  if (!token) {
    try { token = (await request.formData()).get("t"); } catch { /* no form body */ }
  }
  return String(token || "");
}

export const wantsJson = (request) => (request.headers.get("accept") || "").includes("application/json");
