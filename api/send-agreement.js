// Vercel Serverless Function — POST /api/send-agreement
// Sends agreement PDFs via Nodemailer + SMTP.
// Configured to work with cPanel email (mail.microtechlabs.io), Gmail,
// Outlook, or any SMTP server.
//
// SETUP — Vercel dashboard → Project → Settings → Environment Variables:
//
//   SMTP_HOST       mail.microtechlabs.io
//   SMTP_PORT       465
//   SMTP_SECURE     true
//   SMTP_USER       contact@microtechlabs.io
//   SMTP_PASS       (your email account password)
//   FROM_EMAIL      contact@microtechlabs.io
//   OWNER_EMAIL     contact@microtechlabs.io
//
// If port 465 has issues, fall back to port 587:
//   SMTP_PORT=587  SMTP_SECURE=false   (uses STARTTLS)

import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  // CORS — keep if form may be served from a different origin
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  try {
    const {
      docId,
      customerEmail,
      customerName,
      sigDate,
      timestamp,
      plan,
      amount,
      customerPdf,
      sellerPdf,
    } = req.body || {};

    if (!customerEmail || !docId || !customerPdf || !sellerPdf) {
      return res.status(400).json({ ok: false, error: 'Missing required fields' });
    }

    const FROM = process.env.FROM_EMAIL || process.env.SMTP_USER;
    const OWNER = process.env.OWNER_EMAIL || 'contact@microtechlabs.io';

    // Build the SMTP transporter from env vars.
    // cPanel-friendly settings: explicit timeouts, TLS that tolerates
    // self-signed/non-strict certs (common on shared hosting).
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: parseInt(process.env.SMTP_PORT || '465', 10),
      secure: String(process.env.SMTP_SECURE || 'true') === 'true',
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS,
      },
      // Connection / socket / greeting timeouts (Vercel functions have ~10s limits)
      connectionTimeout: 10000,
      greetingTimeout:   10000,
      socketTimeout:     20000,
      tls: {
        // cPanel/shared hosting often presents self-signed or hostname-mismatched
        // certs. Set to false if you hit cert errors. Set to true for stricter prod.
        rejectUnauthorized: false,
      },
    });

    // Convert base64 strings to Buffers for Nodemailer attachments
    const customerAttachment = {
      filename: customerPdf.filename,
      content: Buffer.from(customerPdf.contentBase64, 'base64'),
      contentType: 'application/pdf',
    };
    const sellerAttachment = {
      filename: sellerPdf.filename,
      content: Buffer.from(sellerPdf.contentBase64, 'base64'),
      contentType: 'application/pdf',
    };

    const customerHtml = `
      <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;padding:20px;color:#152038">
        <h2 style="color:#0A1628;border-bottom:3px solid #C8922A;padding-bottom:8px">
          MicroTech Agreement Confirmation
        </h2>
        <p>Hi ${escapeHtml(customerName) || 'Customer'},</p>
        <p>Thank you for choosing MicroTech. Your signed service agreement is attached for your records.</p>
        <table style="border-collapse:collapse;margin:16px 0">
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Agreement No.</td><td style="font-weight:bold">${escapeHtml(docId)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Service Plan</td><td>${escapeHtml(plan || '—')}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Amount</td><td>${escapeHtml(amount || '—')}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Signature Date</td><td>${escapeHtml(sigDate || '—')}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Submitted</td><td>${escapeHtml(timestamp || '—')}</td></tr>
        </table>
        <p>If you have any questions, reply to this email or contact us at
          <a href="mailto:${OWNER}">${OWNER}</a>.</p>
        <hr style="border:none;border-top:1px solid #D6D9E0;margin:24px 0">
        <p style="font-size:12px;color:#6B7280">
          MicroTech · Premium Technical Support Services<br>
          This is an ESIGN Act–compliant electronic agreement.
        </p>
      </div>
    `;

    const ownerHtml = `
      <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;padding:20px;color:#152038">
        <h2 style="color:#0A1628">New Agreement Signed</h2>
        <table style="border-collapse:collapse;margin:16px 0">
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Agreement No.</td><td style="font-weight:bold">${escapeHtml(docId)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Customer</td><td>${escapeHtml(customerName || '—')}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Email</td><td>${escapeHtml(customerEmail)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Plan</td><td>${escapeHtml(plan || '—')}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Amount</td><td>${escapeHtml(amount || '—')}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Signed</td><td>${escapeHtml(sigDate || '—')}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Submitted</td><td>${escapeHtml(timestamp || '—')}</td></tr>
        </table>
        <p>Both customer and seller copies are attached.</p>
      </div>
    `;

    // Email 1 → Customer (their copy attached, owner BCC'd for record)
    const customerSend = transporter.sendMail({
      from: `"MicroTech Agreements" <${FROM}>`,
      to: customerEmail,
      bcc: OWNER,
      replyTo: OWNER,
      subject: `Your MicroTech Agreement — ${docId}`,
      html: customerHtml,
      attachments: [customerAttachment],
    });

    // Email 2 → Owner (BOTH copies attached, for filing)
    const ownerSend = transporter.sendMail({
      from: `"MicroTech Agreements" <${FROM}>`,
      to: OWNER,
      replyTo: customerEmail,
      subject: `[Signed] ${docId} — ${customerName || customerEmail}`,
      html: ownerHtml,
      attachments: [customerAttachment, sellerAttachment],
    });

    const [custResult, ownResult] = await Promise.all([customerSend, ownerSend]);

    return res.status(200).json({
      ok: true,
      customerMessageId: custResult.messageId,
      ownerMessageId: ownResult.messageId,
    });
  } catch (err) {
    console.error('send-agreement handler error:', err);
    return res.status(500).json({
      ok: false,
      error: err.message || 'Server error',
      // Surface SMTP error code if present (helps debugging in browser console)
      code: err.code,
      command: err.command,
    });
  }
}

function escapeHtml(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// Increase body size limit — base64 PDFs can be 1–3 MB
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '10mb',
    },
  },
};
