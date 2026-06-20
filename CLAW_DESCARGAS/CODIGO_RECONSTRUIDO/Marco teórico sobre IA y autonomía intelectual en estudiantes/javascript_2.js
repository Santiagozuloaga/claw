const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, 
        ImageRun, PageBreak, LevelFormat, NumberingLevel } = require('docx');
const fs = require('fs');

const img2 = fs.readFileSync('/mnt/user-data/uploads/1778794893718_image.png');

// Page margins (2.54cm = 1440 twips, but in DXA: 1440)
// Times New Roman 12pt = size 24 in half-points

const FONT = "Times New Roman";
const SIZE = 24; // 12pt
const LINE_SPACING = { line: 480, lineRule: "auto" }; // double spacing
const INDENT = { firstLine: 720 }; // 0.5 inch first line indent

// Helper to create body paragraph
function p(text, options = {}) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SIZE })],
    spacing: { ...LINE_SPACING, before: 0, after: 0 },
    indent: INDENT,
    alignment: AlignmentType.JUSTIFIED,
    ...options
  });
}

// Helper with mixed runs
function pRuns(runs, options = {}) {
  return new Paragraph({
    children: runs.map(r => typeof r === 'string' 
      ? new TextRun({ text: r, font: FONT, size: SIZE })
      : new TextRun({ font: FONT, size: SIZE, ...r })
    ),
    spacing: { ...LINE_SPACING, before: 0, after: 0 },
    indent: INDENT,
    alignment: AlignmentType.JUSTIFIED,
    ...options
  });
}

function h1(text) {
  return new Paragraph({
    children: [new TextRun({ text: text.toUpperCase(), font: FONT, size: 24, bold: true })],
    heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.CENTER,
    spacing: { before: 480, after: 240, line: 480 }
  });
}

function h2(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 24, bold: true })],
    heading: HeadingLevel.HEADING_2,
    alignment: AlignmentType.LEFT,
    spacing: { before: 360, after: 240, line: 480 }
  });
}

function h3(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 24, bold: true, italics: true })],
    heading: HeadingLevel.HEADING_3,
    alignment: AlignmentType.LEFT,
    spacing: { before: 240, after: 120, line: 480 }
  });
}

function blank() {
  return new Paragraph({
    children: [new TextRun({ text: "", font: FONT, size: SIZE })],
    spacing: { line: 480 }
  });
}

function pageBreak() {
  return new Paragraph({
    children: [new PageBreak()],
    spacing: { line: 480 }
  });
}

function figureCaption(num, title) {
  return new Paragraph({
    children: [new TextRun({ 
      text: `Figura ${num}`, font: FONT, size: SIZE, bold: true 
    }), new TextRun({ 
      text: `\n${title}`, font: FONT, size: SIZE, italics: true 
    })],
    alignment: AlignmentType.LEFT,
    spacing: { before: 120, after: 240, line: 480 }
  });
}

function reference(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SIZE })],
    spacing: { before: 0, after: 0, line: 480 },
    indent: { hanging: 720, left: 720 },
    alignment: AlignmentType.JUSTIFIED
  });
}