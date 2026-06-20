const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, 
        ImageRun, PageBreak } = require('docx');
const fs = require('fs');

// Load image
const googleAIImg = fs.readFileSync('[LOCAL_PATH]');

// Formatting helpers
const FONT = "Times New Roman";
const SZ = 24; // 12pt
const LS = { line: 480, lineRule: "auto" }; // double spacing

const style = {
  body: (text, opts = {}) => new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SZ })],
    spacing: { ...LS, before: 0, after: 0 },
    indent: { firstLine: 720 },
    alignment: AlignmentType.JUSTIFIED,
    ...opts
  }),
  
  // For paragraphs with mixed formatting (italics for titles)
  bodyMixed: (runs, opts = {}) => new Paragraph({
    children: runs.map(r => new TextRun({ font: FONT, size: SZ, ...r })),
    spacing: { ...LS, before: 0, after: 0 },
    indent: { firstLine: 720 },
    alignment: AlignmentType.JUSTIFIED,
    ...opts
  }),
  
  h1: (text) => new Paragraph({
    children: [new TextRun({ text: text.toUpperCase(), font: FONT, size: SZ, bold: true })],
    heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.CENTER,
    spacing: { before: 480, after: 240, line: 480 }
  }),
  
  h2: (text) => new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SZ, bold: true })],
    heading: HeadingLevel.HEADING_2,
    alignment: AlignmentType.LEFT,
    spacing: { before: 360, after: 240, line: 480 }
  }),
  
  h3: (text) => new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SZ, bold: true, italics: true })],
    heading: HeadingLevel.HEADING_3,
    alignment: AlignmentType.LEFT,
    spacing: { before: 240, after: 120, line: 480 }
  }),
  
  blank: () => new Paragraph({
    children: [new TextRun("")],
    spacing: { line: 480 }
  }),
  
  pageBreak: () => new Paragraph({ children: [new PageBreak()] }),
  
  ref: (text) => new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SZ })],
    spacing: { ...LS, before: 0, after: 0 },
    indent: { hanging: 720, left: 720 },
    alignment: AlignmentType.JUSTIFIED
  }),
  
  figureLabel: (num) => new Paragraph({
    children: [new TextRun({ text: `Figura ${num}`, font: FONT, size: SZ, bold: true })],
    alignment: AlignmentType.LEFT,
    spacing: { before: 120, after: 0, line: 480 }
  }),
  
  figureTitle: (text) => new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SZ, italics: true })],
    alignment: AlignmentType.LEFT,
    spacing: { before: 0, after: 240, line: 480 }
  }),
  
  figureNote: (text) => new Paragraph({
    children: [
      new TextRun({ text: "[REDACTED_INFRASTRUCTURE]. ", font: FONT, size: SZ, italics: true }),
      new TextRun({ text, font: FONT, size: SZ })
    ],
    alignment: AlignmentType.LEFT,
    spacing: { before: 0, after: 240, line: 480 }
  }),
  
  centered: (text, opts = {}) => new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SZ, ...opts })],
    alignment: AlignmentType.CENTER,
    spacing: { line: 480, before: 0, after: 0 }
  })
};