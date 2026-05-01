# MicroTech Agreement — Deployment Notes

## What's in this revision

1. **Agreement Number** is fully auto-generated. The "↻ New" / regenerate button is gone. A fresh number is generated every page load.
2. **Signature Date** is locked to today or future. Past-date quick buttons (−1 Day, −3 Days, etc.) are removed. The date picker has `min` set to today, and a JS guard catches any past-date attempt.
3. **Live timestamp** showing date + time + timezone from the customer's local system clock is displayed under the signature date and stamped onto every PDF.
4. **Email-on-download.** When the user clicks "Download Both Copies":
   - Customer gets the customer copy (sent to their email)
   - You (`contact@microtechlabs.io`) get BOTH copies for record-keeping
   - You're also BCC'd on the customer email

## Project structure

```
microtech-agreement/
├── index.html              ← the agreement form
├── package.json
└── api/
    └── send-agreement.js   ← Vercel serverless email function
```

`index.html` at the project root. `send-agreement.js` inside an `api/` folder. Vercel auto-detects `api/` and turns each file into a serverless endpoint.

---

## Setup — using your cPanel email (mail.microtechlabs.io)

### 1. Install the dependency

In your project root:

```bash
npm install nodemailer
```

Commit the updated `package.json` and `package-lock.json`.

### 2. Add environment variables in Vercel

Vercel dashboard → your project → **Settings → Environment Variables**. Add these for **Production, Preview, AND Development**:

| Name | Value |
|------|-------|
| `SMTP_HOST` | `mail.microtechlabs.io` |
| `SMTP_PORT` | `465` |
| `SMTP_SECURE` | `true` |
| `SMTP_USER` | `contact@microtechlabs.io` |
| `SMTP_PASS` | *your contact@microtechlabs.io password* |
| `FROM_EMAIL` | `contact@microtechlabs.io` |
| `OWNER_EMAIL` | `contact@microtechlabs.io` |

**Important:** make sure `SMTP_PASS` has no quotes around it and no trailing spaces when you paste it into Vercel.

### 3. Deploy

```bash
git add .
git commit -m "Auto agreement number, future-only date, email-on-download"
git push
```

Vercel auto-deploys.

### 4. Test

1. Open the deployed site
2. Fill the form, sign, click "Download Both Copies"
3. Both PDFs download as before
4. Check `contact@microtechlabs.io` — you should have **two** emails:
   - One to you (the customer email, you're BCC'd)
   - One to you (the owner record with both copies attached)
5. The customer should also have one email with their copy
6. The success overlay on the page will say "✅ Email sent to..." once the API responds

---

## Troubleshooting

### Where to look first

Vercel dashboard → Deployments → click the latest deployment → **Functions tab** → click `send-agreement`. Any errors print there with the SMTP error code.

### Common issues with cPanel SMTP

**"Connection timeout" or "ETIMEDOUT"**
Vercel's serverless functions have a hard 10-second limit on free tier. If your cPanel SMTP is slow to respond:
- Try port `587` with `SMTP_SECURE=false` (uses STARTTLS, sometimes faster)
- Confirm your hosting provider hasn't blocked external SMTP connections

**"Invalid login" / 535 authentication failed**
- Double-check the password — paste it into webmail at `https://mail.microtechlabs.io` first to confirm it works
- Some cPanel hosts require enabling "Authenticated SMTP" or "External SMTP" in cPanel → Email Accounts
- If your hosting has 2FA on the email account, you may need an app-specific password from cPanel

**"self signed certificate" / "DEPTH_ZERO_SELF_SIGNED_CERT"**
Already handled in the code (`tls.rejectUnauthorized: false`). If you still see it, the host likely needs you to use port `587` instead.

**"Sender address rejected" / "550 not allowed"**
Some cPanel configs only allow sending FROM the same email account you authenticated WITH. The code already does this (`FROM_EMAIL = SMTP_USER = contact@microtechlabs.io`), so you should be fine.

**Customer not getting their copy, but you are**
Likely your hosting's outbound spam filter is being cautious about emails to external addresses. Check the email provider on the customer's side first, then your cPanel's outbound mail logs (cPanel → Track Delivery).

### Fallback: switch to port 587

If port 465 fails, change just two env vars in Vercel and redeploy:

| Name | Value |
|------|-------|
| `SMTP_PORT` | `587` |
| `SMTP_SECURE` | `false` |

No code changes needed.

---

## Local development

To test the API locally before pushing:

```bash
npm i -g vercel
vercel dev
```

Runs both the static site and `/api/*` functions on `http://localhost:3000`. Vercel CLI will prompt to pull env vars from your project on first run.
