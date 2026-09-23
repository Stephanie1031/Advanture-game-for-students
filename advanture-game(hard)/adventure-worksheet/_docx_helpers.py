#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""共用排版工具 / shared docx layout helpers.

从 dino-pet-game/worksheet/make_worksheet.py 抽出来复用：
中文字体设置、代码块、下划线留白、表格等。
Reusable pieces for building a printable A4 worksheet with python-docx.
"""

import os
import re
import sys

try:
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError:                                     # pragma: no cover
    sys.exit('请先安装 python-docx / please install python-docx:\n'
             '    python3 -m pip install python-docx')

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# 字体与颜色 / fonts and colours
# ---------------------------------------------------------------------------
HAN = '微软雅黑'          # 中文正文字体
HAN_FALLBACK = 'PingFang SC'
MONO = 'Consolas'        # 代码字体
MONO_HAN = '楷体'         # 代码里的中文（等宽感更好）
LATIN = 'Arial'

GREY = RGBColor(0x59, 0x59, 0x59)
ACCENT = RGBColor(0x1F, 0x4E, 0x79)
GREEN = RGBColor(0x2E, 0x6B, 0x2E)
RED = RGBColor(0xA6, 0x2A, 0x1F)

BODY_SIZE = Pt(10.5)
CODE_SIZE = Pt(9.5)
SMALL_SIZE = Pt(9)


# ---------------------------------------------------------------------------
# 底层小工具 / low-level helpers
# ---------------------------------------------------------------------------
def set_run_font(run, latin=LATIN, han=HAN, size=BODY_SIZE, bold=False,
                 italic=False, color=None):
    """给一段文字设置中西文字体 / set both the Latin and the East-Asian font."""
    run.font.name = latin
    run.font.size = size
    run.bold = bold
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts')
        rpr.insert(0, rfonts)
    rfonts.set(qn('w:ascii'), latin)
    rfonts.set(qn('w:hAnsi'), latin)
    rfonts.set(qn('w:eastAsia'), han)
    return run


def shade(element, fill):
    """给段落或单元格加底色 / background shading."""
    pr = element.get_or_add_tcPr() if element.tag.endswith('tc') \
        else element.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    pr.append(shd)


def border(paragraph, edges=('bottom',), size=8, color='808080', space=2):
    """给段落加边框（下划线留白就用它）/ paragraph borders."""
    ppr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    for edge in edges:
        node = OxmlElement('w:' + edge)
        node.set(qn('w:val'), 'single')
        node.set(qn('w:sz'), str(size))
        node.set(qn('w:space'), str(space))
        node.set(qn('w:color'), color)
        pbdr.append(node)
    ppr.append(pbdr)


def keep_with_next(paragraph):
    ppr = paragraph._p.get_or_add_pPr()
    node = OxmlElement('w:keepNext')
    ppr.append(node)


def no_split(table):
    """让表格的行不要跨页断开 / keep table rows on one page."""
    for row in table.rows:
        tr_pr = row._tr.get_or_add_trPr()
        tr_pr.append(OxmlElement('w:cantSplit'))


def no_table_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        node = OxmlElement('w:' + edge)
        node.set(qn('w:val'), 'none')
        node.set(qn('w:sz'), '0')
        borders.append(node)
    tbl_pr.append(borders)


# ---------------------------------------------------------------------------
# 段落与代码 / paragraphs and code blocks
# ---------------------------------------------------------------------------
def para(doc, parts, size=BODY_SIZE, space_before=2, space_after=2,
         left_indent=0.0, first_line=0.0, align=None, line=1.15):
    """写一段文字。parts 可以是字符串，也可以是 (文字, 是否加粗) 的列表。"""
    if isinstance(parts, str):
        parts = [parts]
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.space_before = Pt(space_before)
    fmt.space_after = Pt(space_after)
    fmt.line_spacing = line
    if left_indent:
        fmt.left_indent = Cm(left_indent)
    if first_line:
        fmt.first_line_indent = Cm(first_line)
    if align is not None:
        p.alignment = align
    for part in parts:
        text, bold = (part, False) if isinstance(part, str) else part
        set_run_font(p.add_run(text), size=size, bold=bold)
    return p


def rich(doc, parts, size=BODY_SIZE, **kwargs):
    """一段混排文字。parts 里每项是 (文字, 样式名)：
       'b' 加粗 / 'code' 等宽 / 'han' 中文等宽 / 'g' 灰色小字
    """
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.space_before = Pt(kwargs.get('space_before', 2))
    fmt.space_after = Pt(kwargs.get('space_after', 2))
    fmt.line_spacing = kwargs.get('line', 1.15)
    if kwargs.get('left_indent'):
        fmt.left_indent = Cm(kwargs['left_indent'])
    if kwargs.get('first_line'):
        fmt.first_line_indent = Cm(kwargs['first_line'])
    for text, style in parts:
        if style == 'b':
            set_run_font(p.add_run(text), size=size, bold=True)
        elif style == 'code':
            set_run_font(p.add_run(text), latin=MONO, han=MONO_HAN,
                         size=Pt(size.pt - 0.5))
        elif style == 'codeb':
            set_run_font(p.add_run(text), latin=MONO, han=MONO_HAN,
                         size=Pt(size.pt - 0.5), bold=True)
        elif style == 'han':
            set_run_font(p.add_run(text), latin=MONO_HAN, han=MONO_HAN, size=size)
        elif style == 'g':
            set_run_font(p.add_run(text), size=Pt(size.pt - 1), color=GREY)
        elif style == 'acc':
            set_run_font(p.add_run(text), size=size, bold=True, color=ACCENT)
        elif style == 'fill':
            set_run_font(p.add_run(text), latin=MONO, han=MONO_HAN,
                         size=Pt(size.pt - 0.5), bold=True, color=RED)
        else:
            set_run_font(p.add_run(text), size=size)
    return p


def code_block(doc, lines, fill='F4F5F7', size=CODE_SIZE, space=0):
    """一块代码。lines 是字符串列表；每行里 '>>>' 之类的照原样。"""
    table = doc.add_table(rows=1, cols=1)
    no_table_borders(table)
    no_split(table)
    cell = table.cell(0, 0)
    shade(cell._tc, fill)
    cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)
    for line in lines:
        p = cell.add_paragraph()
        fmt = p.paragraph_format
        fmt.space_before = Pt(space)
        fmt.space_after = Pt(space)
        fmt.line_spacing = 1.0
        set_run_font(p.add_run(line if line else ' '), latin=MONO, han=MONO_HAN,
                     size=size)
    return table


def blank_lines(doc, count=1, width_cm=None):
    """留白的书写行（下划线），打印出来可以手写。"""
    for _ in range(count):
        p = doc.add_paragraph()
        fmt = p.paragraph_format
        fmt.space_before = Pt(6)
        fmt.space_after = Pt(6)
        fmt.line_spacing = 1.0
        if width_cm:
            fmt.right_indent = Cm(16.4 - width_cm)
        border(p, edges=('bottom',), size=6, color='A6A6A6')
    return doc


def heading(doc, number, zh, en=''):
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.space_before = Pt(12)
    fmt.space_after = Pt(4)
    set_run_font(p.add_run('{}  {}'.format(number, zh)), size=Pt(13), bold=True,
                 color=ACCENT)
    if en:
        set_run_font(p.add_run('   ' + en), size=SMALL_SIZE, color=GREY)
    keep_with_next(p)
    return p


def subheading(doc, text, en=''):
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.space_before = Pt(8)
    fmt.space_after = Pt(3)
    set_run_font(p.add_run(text), size=Pt(11.5), bold=True)
    if en:
        set_run_font(p.add_run('   ' + en), size=SMALL_SIZE, color=GREY)
    keep_with_next(p)
    return p


def note_box(doc, lines, fill='FFF7E6'):
    """提示框 / a tinted note box."""
    table = doc.add_table(rows=1, cols=1)
    no_table_borders(table)
    cell = table.cell(0, 0)
    shade(cell._tc, fill)
    cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)
    no_split(table)
    for line in lines:
        p = cell.add_paragraph()
        fmt = p.paragraph_format
        fmt.space_before = Pt(2)
        fmt.space_after = Pt(2)
        fmt.line_spacing = 1.1
        for part in (line if isinstance(line, list) else [line]):
            text, style = (part, 'n') if isinstance(part, str) else part
            if style == 'b':
                set_run_font(p.add_run(text), size=SMALL_SIZE, bold=True)
            elif style == 'code':
                set_run_font(p.add_run(text), latin=MONO, han=MONO_HAN,
                             size=Pt(SMALL_SIZE.pt - 0.5))
            else:
                fill_runs(p, text)
    return table


INLINE_SPLIT = re.compile(r'(`[^`]+`)')


def fill_runs(paragraph, text, size=SMALL_SIZE):
    """把一段文字写进段落；用反引号包起来的部分渲染成等宽代码。

    Why: 表格单元格里经常是「中文说明 + 一小段代码」混排，
    直接 strip('`') 会把不成对的反引号留在版面上。
    """
    for piece in INLINE_SPLIT.split(text):
        if not piece:
            continue
        if piece.startswith('`') and piece.endswith('`') and len(piece) > 2:
            set_run_font(paragraph.add_run(piece[1:-1]), latin=MONO, han=MONO_HAN,
                         size=Pt(size.pt - 0.5))
        else:
            set_run_font(paragraph.add_run(piece), size=size)
    return paragraph


def two_col_table(doc, rows, widths=(5.0, 11.4), header=None):
    """左右两栏的表格，用来放「方法 → 作用」这类对照。"""
    table = doc.add_table(rows=len(rows) + (1 if header else 0), cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    offset = 0
    if header:
        for index, text in enumerate(header):
            cell = table.cell(0, index)
            cell.text = ''
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            set_run_font(p.add_run(text), size=SMALL_SIZE, bold=True)
            shade(cell._tc, 'EDF2F8')
        offset = 1
    for row_index, row in enumerate(rows):
        for col_index, text in enumerate(row):
            cell = table.cell(row_index + offset, col_index)
            cell.text = ''
            for line_index, line in enumerate(text.split('\n')):
                # 第一行之外都另起一段，这样单元格里的换行会真的换行
                p = (cell.paragraphs[0] if line_index == 0 else cell.add_paragraph())
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.line_spacing = 1.05
                fill_runs(p, line)
    no_split(table)
    for row in table.rows:
        for index, width in enumerate(widths):
            row.cells[index].width = Cm(width)
    return table


def page_break(doc):
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)
    return p


def add_footer(section, text):
    """页脚：页码 + 文件名 / footer with page number."""
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run_font(p.add_run(text + '    第 '), size=Pt(8), color=GREY)
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    p._p.append(fld)
    set_run_font(p.add_run(' 页 / page'), size=Pt(8), color=GREY)


def setup_page(doc):
    section = doc.sections[0]
    section.page_height = Cm(29.7)
    section.page_width = Cm(21.0)
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(1.4)
    section.left_margin = Cm(1.8)
    section.right_margin = Cm(1.8)
    return section




def drop_trailing_empty(doc):
    """删掉文档最后多出来的空段落 / remove the stray empty paragraph at the end."""
    body = doc.element.body
    for child in list(body.iterchildren()):
        if child.tag.endswith('}sectPr'):
            continue
        if child.tag.endswith('}p'):
            text = ''.join(t.text or '' for t in child.findall('.//' + qn('w:t')))
            if not text.strip() and not child.findall('.//' + qn('w:br')):
                body.remove(child)
                continue
        break
    return doc
