const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, 
        ImageRun, PageBreak, LevelFormat, WidthType } = require('docx');
const fs = require('fs');
const path = require('path');

// Load images
const image2 = fs.readFileSync('[LOCAL_PATH]');

// Helper functions
const indent = { firstLine: 720 }; // 0.5 inch indent
const spacing = { line: 480, lineRule: 'auto' }; // Double spacing (240 = single, 480 = double)

function heading1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text, bold: true, size: 24, font: 'Times New Roman' })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 360, after: 240, line: 480 }
  });
}

// ... etc