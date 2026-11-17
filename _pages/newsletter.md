---
layout: page
title: Newsletter
description: "A short email when there is a new post or a new Puzzle of the Month. No ads, nothing else."
permalink: /newsletter/
---
<div class="newsletter-status" data-newsletter-states hidden>
  <p data-state="check-your-inbox" hidden><strong>Almost done.</strong> Please check your inbox and click the link in the email to confirm. No email after a few minutes? Look in your spam folder.</p>
  <p data-state="welcome" hidden><strong>You're subscribed.</strong> Thank you! You'll get a short email whenever there's something new.</p>
  <p data-state="unsubscribed" hidden><strong>You're unsubscribed.</strong> Your address has been deleted. Sorry to see you go, and you're always welcome back.</p>
  <p data-state="error-email" hidden>That email address doesn't look right. Please check it and try again.</p>
  <p data-state="error-link" hidden>That link doesn't work any more. Please sign up again below.</p>
  <p data-state="error-busy" hidden>Something went wrong on my side. Please try again later.</p>
</div>

<form class="form" action="/api/subscribe" method="POST" data-newsletter-form>
  <div class="form__field">
    <label for="newsletter-email">Your email</label>
    <input id="newsletter-email" type="email" name="email" autocomplete="email" required>
  </div>
  <div class="form__field newsletter-trap" aria-hidden="true">
    <label for="newsletter-website">Leave this field empty</label>
    <input id="newsletter-website" type="text" name="website" tabindex="-1" autocomplete="off">
  </div>
  <button class="button" type="submit">Subscribe</button>
</form>

## What you get

One short email when a new post goes up, usually on the 15th, and when the new Puzzle of the Month is out on the 1st. The email has the title, two lines and a link. That's all.

## Your address

Your address is used for this newsletter only. It is never shared or sold, and the emails carry no tracking. You confirm your subscription with one click, every email has a link to unsubscribe with one click, and unsubscribing deletes your address.

Prefer a feed reader? Use the [RSS feed]({{ '/feed.xml' | relative_url }}).
