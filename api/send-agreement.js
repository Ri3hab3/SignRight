// Vercel Serverless Function — POST /api/send-agreement
//
// Receives form data from the browser (small payload, no PDFs).
// Generates the SELLER PDF on the server using pdfkit.
// Emails:
//   - Owner (contact@microtechlabs.io) → SELLER PDF attached
//   - Customer → confirmation email (no attachment, they downloaded their own copy in browser)
//
// SETUP — Vercel Environment Variables (Settings → Environment Variables):
//   SMTP_HOST       mail.microtechlabs.io
//   SMTP_PORT       465
//   SMTP_SECURE     true
//   SMTP_USER       contact@microtechlabs.io
//   SMTP_PASS       (your email password)
//   FROM_EMAIL      contact@microtechlabs.io
//   OWNER_EMAIL     contact@microtechlabs.io

import nodemailer from 'nodemailer';
import PDFDocument from 'pdfkit';

export default async function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  try {
    const d = req.body || {};

    if (!d.email || !d.docId) {
      return res.status(400).json({ ok: false, error: 'Missing required fields (email, docId)' });
    }

    const FROM = process.env.FROM_EMAIL || process.env.SMTP_USER;
    const OWNER = process.env.OWNER_EMAIL || 'contact@microtechlabs.io';
    const customerName = ((d.firstName || '') + ' ' + (d.lastName || '')).trim();

    // ─── Generate seller PDF on the server ───
    const sellerPdfBuffer = await generateSellerPDF(d);
    const sellerFilename = `MicroTech-Agreement-${d.docId}-SELLER.pdf`;

    // ─── Set up SMTP ───
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: parseInt(process.env.SMTP_PORT || '465', 10),
      secure: String(process.env.SMTP_SECURE || 'true') === 'true',
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS,
      },
      connectionTimeout: 10000,
      greetingTimeout: 10000,
      socketTimeout: 20000,
      tls: { rejectUnauthorized: false },
    });

    // ─── Email 1: Owner email with seller PDF attached ───
    const ownerHtml = `
      <div style="font-family:Arial,sans-serif;max-width:640px;margin:0 auto;padding:20px;color:#152038">
        <h2 style="color:#0A1628;border-bottom:3px solid #C8922A;padding-bottom:8px">New Agreement Signed</h2>
        <p>A new MicroTech service agreement has been signed. The seller copy PDF is attached.</p>
        <table style="border-collapse:collapse;margin:16px 0;font-size:14px">
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Agreement No.</td><td style="font-weight:bold">${esc(d.docId)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Customer</td><td>${esc(customerName)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Email</td><td><a href="mailto:${esc(d.email)}">${esc(d.email)}</a></td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Phone</td><td>${esc(d.phone)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Address</td><td>${esc(d.address)}, ${esc(d.city)}, ${esc(d.state)} ${esc(d.zip)}, ${esc(d.country)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Plan</td><td>${esc(d.plan)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Tenure</td><td>${esc(d.tenure)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Start Date</td><td>${esc(d.startDate)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Amount</td><td style="font-weight:bold;color:#1355C7">${esc(d.amount)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Payment Method</td><td>${esc(d.paymentMethod)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Signed</td><td>${esc(d.sigDate)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Submitted</td><td>${esc(d.timestampReadable)}</td></tr>
        </table>
        ${d.issueDesc ? `<p style="margin-top:16px"><strong>Issue Description:</strong><br>${esc(d.issueDesc)}</p>` : ''}
        <hr style="border:none;border-top:1px solid #D6D9E0;margin:24px 0">
        <p style="font-size:12px;color:#6B7280">SignRight™ Verified · ESIGN Act Compliant</p>
      </div>
    `;

    const ownerSend = transporter.sendMail({
      from: `"MicroTech Agreements" <${FROM}>`,
      to: OWNER,
      replyTo: d.email,
      subject: `[Signed] ${d.docId} — ${customerName || d.email}`,
      html: ownerHtml,
      attachments: [{
        filename: sellerFilename,
        content: sellerPdfBuffer,
        contentType: 'application/pdf',
      }],
    });

    // ─── Email 2: Customer confirmation (no attachment, they downloaded their copy in browser) ───
    const customerHtml = `
      <div style="font-family:Arial,sans-serif;max-width:640px;margin:0 auto;padding:20px;color:#152038">
        <h2 style="color:#0A1628;border-bottom:3px solid #C8922A;padding-bottom:8px">MicroTech Agreement Confirmation</h2>
        <p>Hi ${esc(customerName) || 'Customer'},</p>
        <p>Thank you for choosing MicroTech. Your service agreement <strong>${esc(d.docId)}</strong> has been signed and submitted successfully.</p>
        <p>You should already have a PDF copy of the agreement in your <strong>Downloads folder</strong>. Please keep it for your records.</p>
        <table style="border-collapse:collapse;margin:16px 0;font-size:14px">
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Agreement No.</td><td style="font-weight:bold">${esc(d.docId)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Service Plan</td><td>${esc(d.plan)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Amount</td><td>${esc(d.amount)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Signature Date</td><td>${esc(d.sigDate)}</td></tr>
          <tr><td style="padding:6px 12px 6px 0;color:#6B7280">Submitted</td><td>${esc(d.timestampReadable)}</td></tr>
        </table>
        <p>If you have any questions or need a copy of your agreement re-sent, please contact us at
          <a href="mailto:${OWNER}">${OWNER}</a>.</p>
        <hr style="border:none;border-top:1px solid #D6D9E0;margin:24px 0">
        <p style="font-size:12px;color:#6B7280">
          MicroTech · Premium Technical Support Services<br>
          ESIGN Act–compliant electronic agreement.
        </p>
      </div>
    `;

    const customerSend = transporter.sendMail({
      from: `"MicroTech Agreements" <${FROM}>`,
      to: d.email,
      replyTo: OWNER,
      subject: `Your MicroTech Agreement Confirmation — ${d.docId}`,
      html: customerHtml,
    });

    const [ownResult, custResult] = await Promise.all([ownerSend, customerSend]);

    return res.status(200).json({
      ok: true,
      ownerMessageId: ownResult.messageId,
      customerMessageId: custResult.messageId,
    });

  } catch (err) {
    console.error('send-agreement handler error:', err);
    return res.status(500).json({
      ok: false,
      error: err.message || 'Server error',
      code: err.code,
    });
  }
}

// ─── Helpers ───
function esc(s) {
  if (s == null) return '';
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

// Server-side PDF generation using pdfkit
function generateSellerPDF(d) {
  return new Promise((resolve, reject) => {
    try {
      const doc = new PDFDocument({ size: 'A4', margin: 40 });
      const chunks = [];
      doc.on('data', (chunk) => chunks.push(chunk));
      doc.on('end', () => resolve(Buffer.concat(chunks)));
      doc.on('error', reject);

      const NAVY = '#0A1628';
      const BLUE = '#1355C7';
      const GOLD = '#C8922A';
      const GRAY = '#6B7280';
      const customerName = ((d.firstName || '') + ' ' + (d.lastName || '')).trim();

      // Header
      doc.rect(0, 0, doc.page.width, 80).fill(NAVY);
      doc.fillColor('#fff').fontSize(22).font('Helvetica-Bold').text('MicroTech', 40, 24);
      doc.fillColor(GOLD).fontSize(11).font('Helvetica').text('PREMIUM TECHNICAL SUPPORT SERVICES', 40, 52);
      doc.fillColor('#fff').fontSize(9).font('Helvetica').text('SELLER COPY · INTERNAL', doc.page.width - 180, 32, { width: 140, align: 'right' });
      doc.fillColor(GOLD).fontSize(8).text('SignRight™ Verified', doc.page.width - 180, 50, { width: 140, align: 'right' });

      doc.fillColor('#000');
      let y = 100;

      // Title
      doc.fillColor(NAVY).fontSize(16).font('Helvetica-Bold').text('Technical Support Service Agreement', 40, y, { align: 'center' });
      y += 24;
      doc.fillColor(GRAY).fontSize(9).font('Helvetica').text('SELLER REFERENCE COPY', 40, y, { align: 'center' });
      y += 22;

      // Reference box
      doc.rect(40, y, doc.page.width - 80, 32).fill('#F0F4FF');
      doc.fillColor(NAVY).fontSize(9).font('Helvetica-Bold')
         .text(`Agreement No: ${d.docId}`, 52, y + 8)
         .text(`Signed: ${d.sigDate || ''}`, 52, y + 20);
      doc.fillColor(GRAY).font('Helvetica').fontSize(9)
         .text(`Submitted: ${d.timestampReadable || ''}`, 52, y + 8, { width: doc.page.width - 104, align: 'right' })
         .text('SignRight™ Verified · ESIGN Act Compliant', 52, y + 20, { width: doc.page.width - 104, align: 'right' });
      y += 48;

      // Section helper
      const section = (title, num) => {
        doc.rect(40, y, doc.page.width - 80, 22).fill('#EBF1FF');
        doc.circle(56, y + 11, 9).fill(BLUE);
        doc.fillColor('#fff').fontSize(9).font('Helvetica-Bold').text(String(num), 52, y + 6);
        doc.fillColor(NAVY).fontSize(10).font('Helvetica-Bold').text(title, 76, y + 6);
        y += 28;
      };

      const row = (label, value, x, w) => {
        doc.fillColor(GRAY).fontSize(8).font('Helvetica-Bold').text(label.toUpperCase(), x, y);
        doc.fillColor('#000').fontSize(10).font('Helvetica').text(value || '—', x, y + 10, { width: w });
      };

      // 1. CUSTOMER INFORMATION
      section('CUSTOMER INFORMATION', 1);
      row('Full Name', customerName, 40, 250);
      row('Phone', d.phone || '', 290, 220);
      y += 30;
      row('Email Address', d.email || '', 40, doc.page.width - 80);
      y += 30;
      row('Street Address', d.address || '', 40, doc.page.width - 80);
      y += 30;
      const fullLoc = [d.city, d.state, d.zip, d.country].filter(Boolean).join(', ');
      row('City / State / ZIP / Country', fullLoc, 40, doc.page.width - 80);
      y += 36;

      // 2. SERVICE PLAN
      section('SERVICE PLAN & DETAILS', 2);
      row('Service Plan', d.plan || '', 40, 200);
      row('Service Amount', d.amount || '', 240, 130);
      row('Tenure', d.tenure || '', 380, 140);
      y += 30;
      row('Start Date', d.startDate || '', 40, 180);
      row('Payment Method', d.paymentMethod || '', 220, 180);
      row('Reference No.', d.docId, 400, 140);
      y += 36;

      if (d.issueDesc) {
        doc.fillColor(GRAY).fontSize(8).font('Helvetica-Bold').text('ISSUE DESCRIPTION', 40, y);
        y += 12;
        doc.fillColor('#000').fontSize(9).font('Helvetica').text(d.issueDesc, 40, y, { width: doc.page.width - 80 });
        y = doc.y + 10;
      }

      // 3. KEY TERMS
      section('KEY TERMS SUMMARY', 3);
      const terms = [
        '• 14-day satisfaction guarantee from service start date.',
        '• Services delivered remotely by Microsoft-certified technicians.',
        '• Customer authorizes payment via the selected method above.',
        '• Refunds processed per published refund policy on microtechlabs.io.',
        '• Both parties agree to electronic signature per ESIGN Act and UETA.',
      ];
      doc.fillColor('#000').fontSize(9).font('Helvetica');
      terms.forEach(t => {
        doc.text(t, 40, y, { width: doc.page.width - 80 });
        y = doc.y + 4;
      });
      y += 12;

      // 4. SIGNATURE
      if (y > 680) { doc.addPage(); y = 40; }
      section('ELECTRONIC SIGNATURE', 4);
      row('Printed Name', d.printedName || customerName, 40, 240);
      row('Signature Date', d.sigDate || '', 290, 220);
      y += 30;

      doc.fillColor(GRAY).fontSize(8).font('Helvetica-Bold').text('SIGNATURE', 40, y);
      y += 12;
      doc.rect(40, y, doc.page.width - 80, 70).stroke('#D6D9E0');

      // Embed signature image
      if (d.sigImageSmall && d.sigImageSmall.indexOf('data:image') === 0) {
        try {
          const base64Data = d.sigImageSmall.split(',')[1];
          const sigBuffer = Buffer.from(base64Data, 'base64');
          doc.image(sigBuffer, 50, y + 5, { width: 270, height: 60, fit: [270, 60] });
        } catch (e) {
          doc.fillColor(GRAY).fontSize(9).font('Helvetica-Oblique').text('[signature not rendered]', 50, y + 30);
        }
      }
      y += 80;

      // Seller-only internal box
      if (y > 700) { doc.addPage(); y = 40; }
      doc.rect(40, y, doc.page.width - 80, 60).fill('#FFF8E7').stroke('#E8B14C');
      doc.fillColor(GOLD).fontSize(9).font('Helvetica-Bold').text('INTERNAL — SELLER NOTES', 50, y + 8);
      doc.fillColor('#000').fontSize(9).font('Helvetica')
         .text(`Customer email: ${d.email}`, 50, y + 24)
         .text(`Submitted IP timestamp: ${d.timestamp || ''}`, 50, y + 38);
      y += 70;

      // Footer
      const footerY = doc.page.height - 40;
      doc.fillColor(GRAY).fontSize(8).font('Helvetica')
         .text(`Document ID: ${d.docId}  ·  Copy: SELLER`, 40, footerY, { width: doc.page.width - 80, align: 'center' });

      doc.end();
    } catch (e) {
      reject(e);
    }
  });
}

// Increase body size limit (still small, but safe)
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '2mb',
    },
  },
};
