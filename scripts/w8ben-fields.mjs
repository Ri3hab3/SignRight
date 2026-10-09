// Lists every form field in the official IRS W-8BEN PDF, in reading order,
// so FIELD_MAP in fill-w-8ben-online.html can be filled in and verified.
// Usage:  npm i pdf-lib  &&  node scripts/w8ben-fields.mjs assets/forms/fw8ben.pdf
import { readFileSync } from 'node:fs';
import { PDFDocument, PDFCheckBox, PDFTextField } from 'pdf-lib';

const file = process.argv[2] || 'assets/forms/fw8ben.pdf';
const doc = await PDFDocument.load(readFileSync(file));
const pages = doc.getPages();
const rows = [];
for (const f of doc.getForm().getFields()) {
  for (const w of f.acroField.getWidgets()) {
    const r = w.getRectangle();
    const p = pages.findIndex(pg => pg.ref === w.P());
    rows.push({
      page: p + 1,
      y: Math.round(r.y), x: Math.round(r.x), w: Math.round(r.width),
      type: f instanceof PDFCheckBox ? 'checkbox' : f instanceof PDFTextField ? 'text' : f.constructor.name,
      name: f.getName(),
      maxLen: f instanceof PDFTextField ? f.getMaxLength() ?? '' : '',
    });
  }
}
rows.sort((a, b) => a.page - b.page || b.y - a.y || a.x - b.x);
console.table(rows);
