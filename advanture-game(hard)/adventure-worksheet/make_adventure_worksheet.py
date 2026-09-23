#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成「校园冒险游戏」进阶作业纸 / printable worksheet for the campus adventure game.

    python3 adventure-worksheet/make_adventure_worksheet.py

产出 / output（都写在本文件夹里，不改动上级目录的任何源文件）:
    adventure-worksheet/校园冒险-作业纸.docx      （学生用，4 页）
    adventure-worksheet/校园冒险-参考答案.docx    （老师用，3 页）

排版工具在 _docx_helpers.py（和 dino-pet-game 的作业纸共用同一套）。
Layout helpers live in _docx_helpers.py, shared with the dino-pet worksheet.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

from _docx_helpers import (ACCENT, BODY_SIZE, CODE_SIZE, GREY, HAN, MONO, MONO_HAN,
                           RED, SMALL_SIZE, blank_lines, code_block,
                           drop_trailing_empty, fill_runs, heading, note_box,
                           page_break, para, rich, set_run_font, setup_page,
                           add_footer, subheading, two_col_table)

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)


# ---------------------------------------------------------------------------
# 学生作业纸 / the student worksheet
# ---------------------------------------------------------------------------
def build_worksheet(path):
    from docx import Document

    doc = Document()
    section = setup_page(doc)
    add_footer(section, '校园冒险游戏 · 进阶作业纸')

    # ---------------- 标题 ----------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    set_run_font(p.add_run('校园冒险游戏'), size=Pt(20), bold=True, color=ACCENT)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(6)
    set_run_font(p.add_run('Campus Adventure — Python class 进阶作业纸（Q2–Q5）'),
                 size=Pt(11), color=GREY)

    table = doc.add_table(rows=1, cols=3)
    from _docx_helpers import border, no_table_borders
    no_table_borders(table)
    for index, label in enumerate(['姓名 Name：', '班级 Class：', '日期 Date：']):
        cell = table.cell(0, index)
        cell.text = ''
        inner = cell.paragraphs[0]
        inner.paragraph_format.space_before = Pt(6)
        inner.paragraph_format.space_after = Pt(6)
        set_run_font(inner.add_run(label), size=BODY_SIZE)
        border(inner, edges=('bottom',), size=8, color='000000')
        cell.width = Cm(5.4)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

    note_box(doc, [
        [('本节目标 / goal：', 'b'),
         ('在已写好的 ', 'n'), ('go_to / talk_to / take / unlock / Key', 'code'),
         (' 五处留空里，写出「读数据 → 改数据」的代码。', 'n')],
        [('本节任务 / tasks：', 'b'),
         ('必做 4 项（Q2–Q5），约 40 行；做完就能通关拿零食、开咖啡厅的门。', 'n')],
        [('跟简单版的关系 / how it relates：', 'b'),
         ('小恐龙养成记练「一个类的数据」；这一份练「多个对象互相调用」。', 'n')],
        [('怎么检查 / how to check：', 'b'),
         ('python3 adventure.py', 'code'), ('（文字版）或 ', 'n'),
         ('python3 adventure_gui.py', 'code'), ('（图形版）玩一局；'
          '每个方法的 docstring 里有 doctest 可以对照。', 'n')],
    ])

    # ---------------- 一、参考卡片 ----------------
    heading(doc, '一', '参考卡片', 'reference card — 做题时随时回来看')

    rich(doc, [('1. 五个类的关系（', 'n'), ('谁装着谁', 'b'), ('）', 'n')])
    code_block(doc, [
        'Place（地点）',
        '  ├─ characters : {"杰瑞": Character对象, ...}   名字 → 角色',
        '  ├─ things     : {"Lemon": Thing对象, ...}      名字 → 物品',
        '  ├─ exits      : {"学生食堂": (Place对象, 描述)} 名字 → 出口',
        '  └─ locked     : False / True',
        '',
        'Character（角色）',
        '  └─ talk()  →  返回台词字符串',
        '',
        'Thing（物品）  ←  Key 继承它',
        '  ├─ use(place)   普通物品：打印「用不了」',
        '  └─ name / description',
        '',
        'Player（玩家）',
        '  ├─ place    : 当前所在的地方（一个 Place 对象）',
        '  ├─ backpack : []  背包（装着 Thing 对象）',
        '  └─ name',
    ], fill='F4F5F7')

    rich(doc, [('2. 三种数据访问方式（', 'n'), ('最容易混的地方', 'b'), ('）', 'n')])
    code_block(doc, [
        'self.place                     # 点号：拿对象自己的属性',
        'self.place.things              # 点号套点号：进入那个地点',
        'self.place.things["Lemon"]     # 方括号：用「名字」取字典里的对象',
        'self.place.get_neighbor("FSM") # 用方法把「名字」变成 Place 对象',
    ], fill='F0F6F0')

    rich(doc, [('3. 会用到的方法（', 'n'), ('都已写好，直接调用', 'b'), ('）', 'n')])
    two_col_table(doc, [
        ('`self.place.get_neighbor(名字)`',
         '把出口名字变成 Place 对象；名字不对时打印提示并返回**原地**'),
        ('`self.place.characters[名字]`', '取出那个 Character 对象'),
        ('`角色.talk()`', '返回这个角色的台词（字符串）'),
        ('`self.place.things[名字]`', '取出那个 Thing 对象'),
        ('`self.place.take(名字)`', '把物品从地点里移除（`pop`），并返回那个对象'),
        ('`self.backpack.append(物品)`', '放进背包'),
        ('`钥匙.use(地点对象)`', '调用钥匙的 use 方法把门打开'),
    ], widths=(7.4, 9.0), header=('方法 / method', '作用 / what it does'))

    # ---------------- 二、Q2 ----------------
    page_break(doc)
    heading(doc, '二', 'Q2  go_to：去另一个地方', 'go_to — 读锁、改 place、打印位置')

    rich(doc, [('在 ', 'n'), ('classes.py', 'code'), (' 的 ', 'n'), ('Player.go_to', 'code'),
               (' 里，把 ', 'n'), ('*** YOUR CODE HERE ***', 'code'),
               (' 换成真正的移动逻辑。', 'n')])
    rich(doc, [('已经给你的两行 / already written：', 'g')], space_before=4)
    code_block(doc, [
        'destination_place = self.place.get_neighbor(location)',
        "if destination_place.locked:",
        "    print(destination_place.name, 'is locked! Go look for a key to unlock it')",
    ])

    rich(doc, [('你要写 / what you write：', 'b')], space_before=6)
    two_col_table(doc, [
        ('① 只有', '`not destination_place.locked` 时才移动：`self.place = destination_place`'),
        ('② 最后', '一定打印一行 `You are at <地点名>, <描述>.`（注意最后的句点）'),
    ], widths=(2.0, 14.4))

    note_box(doc, [
        [('三个容易踩的坑 / three traps：', 'b')],
        [('1. 忘记「打印位置」这一行 —— 锁着、名字错、成功，三种情况都要打印。', 'n')],
        [('2. 把打印写在 if 里面 —— 那样锁着的时候就不打印了。', 'n')],
        [('3. 移动写在了判断之外 —— 门锁着也能进去，Q5 就白写了。', 'n')],
    ])

    rich(doc, [('把 (1)(2) 两行写在下面 / write your code：', 'b')], space_before=8)
    blank_lines(doc, 2)

    # ---------------- 三、Q3（接在 Q2 后面，同一页）----------------
    heading(doc, '三', 'Q3  talk_to：和人说话', 'talk_to — 字典查角色、分三种情况')

    rich(doc, [('已经给你的 / already written：', 'g')], space_before=2)
    code_block(doc, [
        "if type(person) != str:",
        "    print('Person has to be a string.')",
    ])
    rich(doc, [('注意：这一段现在是「如果类型不对就打印」，后面的代码还会继续跑。'
                '你要把它变成「不对就到此为止」。', 'n')])

    rich(doc, [('你要写 / what you write：', 'b')], space_before=6)
    two_col_table(doc, [
        ('① 类型不对', '打印 `Person has to be a string.` 之后**就结束**（`return` 或者 `else`）'),
        ('② 人不在这里', '打印 `Tiffany is not here.`（用传进来的名字）'),
        ('③ 人在这里', '取出角色对象，调用它的 `talk()`，打印 `Jerry says: 台词`'),
    ], widths=(3.0, 13.4), header=('情况 / case', '要做什么 / what to do'))

    note_box(doc, [
        [('提示 / hint：', 'b'),
         ('字典可以用 ', 'n'), ('in', 'code'), (' 判断名字在不在：', 'n')],
        [('    if person not in self.place.characters:   # 不在 → 情况 ②', 'code')],
        [('    character = self.place.characters[person] # 在 → 情况 ③', 'code')],
    ], fill='F0F6F0')

    rich(doc, [('把三种情况写出来 / write your code：', 'b')], space_before=8)
    blank_lines(doc, 2)

    # ---------------- 四、Q4 ----------------
    page_break(doc)
    heading(doc, '四', 'Q4  take：捡起物品', 'take — 名字查字典、放进背包、从原地移除')

    rich(doc, [('同样先看已经给你的类型判断 / the same type guard is given：', 'g')])
    code_block(doc, [
        "if type(thing) != str:",
        "    print('Thing should be a string.')",
    ])

    rich(doc, [('你要写 / what you write：', 'b')], space_before=6)
    two_col_table(doc, [
        ('① 这里有这件东西吗', '用 `in` 判断：`if thing in self.place.things:`'),
        ('② 不在', '打印 `orange is not here.`'),
        ('③ 在', '取出对象 → `self.backpack.append(对象)` → 打印 `Player takes the Lemon`'),
        ('④ 别忘了', '用 `self.place.take(thing)` 把它从地点里移除，否则还能再拿一次'),
    ], widths=(4.0, 12.4), header=('步骤 / step', '要做什么 / what to do'))

    note_box(doc, [
        [('顺序很重要 / order matters：', 'b')],
        [('先取出对象 → 再放进背包 → 再从地点移除。', 'n')],
        [('如果先 ', 'n'), ('self.place.take(thing)', 'code'),
         (' 再用名字去查，字典里已经没有它了。', 'n')],
    ])

    rich(doc, [('把 (1)(2)(3) 三步写出来 / write your code：', 'b')], space_before=8)
    blank_lines(doc, 2)

    # ---------------- 五、Q5 ----------------
    page_break(doc)
    heading(doc, '五', 'Q5  没有门能挡得住我们', 'unlock + Key — 继承与多态')

    rich(doc, [('Q5 有两部分：先实现 ', 'n'), ('Key', 'code'), (' 类，再补全 ', 'n'),
               ('Player.unlock', 'code'), ('。', 'n')])

    subheading(doc, '第一部分：Key 类（继承 Thing）')
    rich(doc, [('先看父类 / the parent class：', 'g')])
    code_block(doc, [
        'class Thing(object):',
        '    def __init__(self, name, description):',
        '        self.name = name',
        '        self.description = description',
        '',
        '    def use(self, place):',
        '        print("You can\'t use a {0} here".format(self.name))',
    ])
    rich(doc, [('Key 是 Thing 的**子类**，只重写 ', 'n'), ('use', 'code'),
               (' 这一个方法：普通物品用不了，钥匙能把门打开。', 'n')])
    rich(doc, [('在 ', 'n'), ('classes.py', 'code'), (' 里把 ', 'n'),
               ('""" Implement Key here! """', 'code'), (' 换成：', 'n')], space_before=4)
    code_block(doc, [
        'class Key(Thing):',
        '    def use(self, place):',
        '        # *** 在这里写 ***：把 place 上锁的状态改成「没锁」',
        '        #   提示：place 是一个 Place 对象，它有一个 locked 属性',
        '        #   一行就够了：place.locked = ???',
    ], fill='FFF7E6')
    rich(doc, [('继承的作用 / why inherit：', 'b'),
               ('Key 自动拥有 Thing 的 ', 'n'), ('__init__', 'code'),
               ('、name、description，你只需要写不一样的那一个行为。', 'n')],
         space_before=6)

    subheading(doc, '第二部分：Player.unlock')
    rich(doc, [('已经给你的 / already written：', 'g')])
    code_block(doc, [
        'if type(place) != str:',
        '    print("Place must be a string")',
        '    return',
        'key = None                  # 先在背包里找一把钥匙',
        'for item in self.backpack:',
        '    if type(item) == Key:',
        '        key = item',
    ])
    two_col_table(doc, [
        ('① 没钥匙', '`key is None` → 打印 `FSM can\'t be unlocked without a key!` 并 return'),
        ('② 门本来就没锁', '用 `get_neighbor(place)` 拿到 Place 对象，'
                           '`locked == False` 就打印 `FSM is already unlocked!`'),
        ('③ 有钥匙、门锁着', '调用 `key.use(那个地点对象)`，再打印 `FSM is now unlocked!`'),
    ], widths=(3.8, 12.6), header=('情况 / case', '要做什么 / what to do'))

    note_box(doc, [
        [('为什么钥匙要「地点对象」而不是直接改 True？', 'b')],
        [('因为 ', 'n'), ('unlock', 'code'), (' 拿到的是**名字**（字符串），', 'n'),
         ('要先用 ', 'n'), ('get_neighbor', 'code'),
         (' 把它变成真正的 Place 对象。', 'n')],
        [('钥匙只负责「把这一扇门打开」，不需要知道是哪一扇 —— 这就是多态。', 'n')],
    ])

    rich(doc, [('Key.use 和 unlock 的关键两三行 / write your code：', 'b')], space_before=8)
    blank_lines(doc, 2)

    # ---------------- 六、预期输出对照 ----------------
    page_break(doc)
    heading(doc, '六', '预期输出对照', 'expected output — 全部来自 docstring')

    rich(doc, [('做题时对着这里检查格式。', 'b'),
               ('锁着的门、说错的名字、没有的钥匙 —— 这些「出错情况」也有规定输出，'
                '不能漏。', 'n')], space_after=6)

    subheading(doc, 'Q2  go_to')
    code_block(doc, [
        ">>> me.go_to('GBC')",
        'You are at GBC, Golden Bear Cafe.',
        ">>> me.go_to('GBC')                 # 已经在原地",
        "Can't go to GBC from GBC.",
        'Try looking around to see where to go.',
        'You are at GBC, Golden Bear Cafe.',
        ">>> me.go_to('Sather Gate')         # 目的地锁着",
        'Sather Gate is locked! Go look for a key to unlock it',
        'You are at GBC, Golden Bear Cafe.',
    ], fill='FFFDF0')

    subheading(doc, 'Q3  talk_to')
    code_block(doc, [
        '>>> me.talk_to(jerry)               # 传的不是字符串',
        'Person has to be a string.',
        ">>> me.talk_to('Jerry')",
        'Jerry says: I am not the Jerry you are looking for.',
        ">>> me.talk_to('Tiffany')           # 这里没有蒂凡尼",
        'Tiffany is not here.',
    ], fill='FFFDF0')

    subheading(doc, 'Q4  take')
    code_block(doc, [
        '>>> me.take(lemon)                  # 传的不是字符串',
        'Thing should be a string.',
        ">>> me.take('orange')",
        'orange is not here.',
        ">>> me.take('Lemon')",
        'Player takes the Lemon',
        ">>> me.take('Lemon')                # 拿过一次就没了",
        'Lemon is not here.',
        '>>> len(me.backpack)',
        '1',
    ], fill='FFFDF0')

    subheading(doc, 'Q5  unlock（Key 类写好以后）')
    code_block(doc, [
        ">>> me.unlock('FSM')                # 背包里没有钥匙",
        "FSM can't be unlocked without a key!",
        ">>> me.take('SkeletonKey')",
        'Player takes the SkeletonKey',
        ">>> me.unlock('FSM')",
        'FSM is now unlocked!',
        ">>> me.unlock('FSM')                # 再开一次",
        'FSM is already unlocked!',
    ], fill='FFFDF0')

    note_box(doc, [
        [('判分时会逐字比对', 'b'),
         ('（包括标点和空格）。最容易丢分的是 Q2 最后那一行 '
          '`You are at ..., ... .`：三种情况都必须打印。', 'n')],
    ])

    # ---------------- 七、检查清单 + 拓展 ----------------
    page_break(doc)
    heading(doc, '七', '检查清单', 'checklist')

    for tag, text in [
        ('Q2', '`go_to` 写完，四种情况（成功 / 已在原地 / 名字错 / 锁着）都打印了位置'),
        ('Q3', '`talk_to` 三种情况都对，类型不对时不再往下跑'),
        ('Q4', '`take` 能放进背包，而且拿过一次就再也拿不到'),
        ('Q5', '`Key` 类和 `unlock` 都写好了，咖啡厅进得去'),
        ('通关', '带上 Smoothie + Lemon 走到大礼堂（hp）'),
    ]:
        rich(doc, [('☐  ', 'n'), (tag + '：', 'b'), (text, 'n')],
             space_before=3, space_after=3)

    heading(doc, '八', '拓展题（选做，不计分）', 'extension — optional')

    two_col_table(doc, [
        ('E1', '给 `Thing` 加一个 `locked` 属性，让 `look()` 里上锁的物品显示成 `???`，'
               '拿到「综合楼深处」的宝藏（`Treasure`）以后才现身'),
        ('E2', '再加一个状态标记（例如 `self.key_show`），配合 E1 做一个「隐藏剧情」：'
               '拿到的宝藏会悄悄改变某件物品的状态'),
        ('E3', '写一个 `Treasure(Thing)` 子类，`__init__` 里先用 '
               '`Thing.__init__(self, name, description)` 再存 `value` / `weight`'),
        ('E4', '给 `Player` 加 `drop(thing)`：把背包里的物品放回当前地点'),
        ('E5', '给 `Place` 加 `describe()`：把 `look()` 拆成「收集数据」和「打印」两步'),
        ('E6', '写一个 `Food(Thing)` 子类，重写 `use(place)` 让它增加一个 `energy` 属性'),
        ('E7', '把 `Player.go_to` 翻译成 CAIE 9618 伪代码（`IF ... THEN ... ELSE ... ENDIF`）'),
    ], widths=(1.6, 14.8))

    note_box(doc, [
        [('E1 + E2 的思路 / one way to do it：', 'b'),
         ('给物品加一个 ', 'n'), ('locked', 'code'),
         (' 属性当「还没解锁」的标记，在 ', 'n'), ('look()', 'code'),
         (' 里判断它，在 ', 'n'), ('take()', 'code'),
         (' 里检查这个标记。拿到达成条件的物品时设一个状态标记，'
          '以后再进某个地点就把钥匙的标记翻开。', 'n')],
        [('要点 / key idea：', 'n'),
         ('新功能 = 加一个属性（数据） + 在已有的方法里多一个判断（逻辑）。'
          '不用改类的结构。', 'n')],
    ], fill='F0F6F0')

    rich(doc, [('九、课堂笔记 / notes', 'b')], space_before=10)
    blank_lines(doc, 3)

    drop_trailing_empty(doc)
    doc.save(path)
    return path


# ---------------------------------------------------------------------------
# 参考答案 / answer sheet (teacher)
# ---------------------------------------------------------------------------
def build_answers(path):
    from docx import Document

    doc = Document()
    section = setup_page(doc)
    add_footer(section, '校园冒险游戏 · 参考答案（老师用）')

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(8)
    set_run_font(p.add_run('校园冒险游戏 · 参考答案与评分要点'), size=Pt(16),
                 bold=True, color=ACCENT)
    rich(doc, [('老师用 / for the teacher：', 'b'),
               ('必做 4 项约 40 行；Q2/Q4/Q5 是「读数据改数据」，Q3 是「字典查找 + 分情况」。', 'n')],
         space_after=8)

    heading(doc, '一', 'Q2  go_to 标准答案', 'classes.py · Player.go_to')
    code_block(doc, [
        "        destination_place = self.place.get_neighbor(location)",
        "        if destination_place.locked:",
        "            print(destination_place.name, 'is locked! Go look for a key to unlock it')",
        '',
        '        if not destination_place.locked:        # 只有没锁时才移动',
        '            self.place = destination_place',
        '',
        '        # 三种情况都要打印这一行',
        "        print('You are at {}, {}'.format(self.place.name, self.place.description))",
    ])
    rich(doc, [('评分 / marking：', 'b'),
               ('能移动（1 分）+ 锁着不移动（1 分）+ 打印格式正确（1 分）。'
                '打印写在 if 里面会丢掉一半情况，扣分。', 'n')], space_before=6)

    heading(doc, '二', 'Q3  talk_to 标准答案', 'classes.py · Player.talk_to')
    code_block(doc, [
        "        if type(person) != str:",
        "            print('Person has to be a string.')",
        '        else:',
        '            if person not in self.place.characters:',
        "                print('{} is not here.'.format(person))",
        '                return',
        '',
        '            character = self.place.characters[person]',
        "            print('{} says: {}'.format(person, character.talk()))",
    ])
    rich(doc, [('也可以用 return 代替 else（原卷的写法是 else）。两种都对，'
                '关键是类型不对时不要再往下跑。', 'g')], space_before=4)

    page_break(doc)
    heading(doc, '三', 'Q4  take 标准答案', 'classes.py · Player.take')
    code_block(doc, [
        "        if type(thing) != str:",
        "            print('Thing should be a string.')",
        '        else:',
        '            if thing in self.place.things:',
        '                item = self.place.things[thing]',
        '                self.backpack.append(item)',
        "                print('Player takes the {}'.format(thing))",
        '                self.place.take(thing)      # 从原地移除',
        '            else:',
        "                print('{} is not here.'.format(thing))",
    ])
    rich(doc, [('常见错误 / common mistake：', 'b'),
               ('先 ', 'n'), ('self.place.take(thing)', 'code'),
               (' 再按键取对象 —— pop 之后字典里就没有这一项了，会报 KeyError。', 'n')],
         space_before=4)

    page_break(doc)
    heading(doc, '四', 'Q5  Key + unlock 标准答案', 'classes.py')
    code_block(doc, [
        'class Key(Thing):                   # 继承 Thing',
        '    def use(self, place):',
        '        place.locked = False        # 把这一扇门打开',
    ])
    code_block(doc, [
        "        if type(place) != str:",
        '            print("Place must be a string")',
        '            return',
        '        key = None',
        '        for item in self.backpack:',
        '            if type(item) == Key:',
        '                key = item',
        '',
        '        if key is None:',
        "            print(\"{} can't be unlocked without a key!\".format(place))",
        '            return',
        '',
        '        next_place = self.place.get_neighbor(place)',
        '        if next_place.locked == False:',
        "            print(place, 'is already unlocked!')",
        '            return',
        '',
        '        key.use(next_place)',
        "        print(place, 'is now unlocked!')",
    ])
    note_box(doc, [
        [('注意 / note：', 'b'),
         ('Key 只写 ', 'n'), ('use', 'code'), ('，不写 ', 'n'), ('__init__', 'code'),
         (' —— 它会自动继承 ', 'n'), ('Thing.__init__', 'code'),
         ('（接受 name 和 description 两个参数）。这也是 data.py 里 ', 'n'),
         ('Key(\'Skeleton Key\', \'...\')', 'code'), (' 能创建成功的原因。', 'n')],
    ], fill='F0F6F0')

    heading(doc, '五', '评分要点', 'marking points')
    two_col_table(doc, [
        ('Q2 go_to', '读 `destination_place.locked`；不变则 `self.place = destination_place`；'
                     '三种情况统一打印 `You are at <名>, <描述>.`'),
        ('Q3 talk_to', '类型不对要中止；`in` 判断在用 `characters` 字典；'
                       '找到后调用 `talk()` 并按规定格式打印'),
        ('Q4 take', '`in` 判断 → 取对象 → `append` → 打印 → `Place.take` 移除；'
                    '顺序错了会 KeyError'),
        ('Q5 Key', '继承 `Thing`，只重写 `use`；`place.locked = False`'),
        ('Q5 unlock', '三种情况（没钥匙 / 已开 / 有钥匙且锁着）各自返回或开锁；'
                      '必须用 `get_neighbor` 把名字变成对象'),
        ('格式分', '输出文字与 docstring 完全一致（含标点）—— 判分时会逐字比对'),
    ], widths=(3.2, 13.2), header=('项目 / item', '要求 / requirement'))

    page_break(doc)
    heading(doc, '六', '机检方式', 'how to check')
    heading(doc, '七', '常见错误', 'common mistakes')
    two_col_table(doc, [
        ('`self.place = destination_place` 写在 if 外面',
         '锁着的门也能进去，Q5 的锁失去意义'),
        ('打印位置那一行写在 `if` 里面',
         '门锁着 / 名字写错时没有输出，doctest 失败'),
        ('`talk_to` 类型不对时没有中止',
         '后面拿 `None` 去查字典会报 AttributeError'),
        ('`take` 里先 pop 再取对象',
         '`KeyError`；必须先取对象再移除'),
        ('`unlock` 里忘了 `get_neighbor`',
         '拿到的是字符串，`place.locked` 会报 AttributeError'),
        ('`Key` 里重写了 `__init__` 却忘了调用 `Thing.__init__`',
         '对象没有 `name` / `description`，背包打印时出错'),
        ('`use(place)` 的参数写成了字符串',
         '`place.locked = False` 会报错；unlock 传进去的是 Place 对象'),
    ], widths=(6.6, 9.8), header=('错误 / wrong', '现象 / what happens'))

    code_block(doc, [
        'python3 adventure.py                    # 文字版，手动玩一局',
        'python3 adventure_gui.py                # 图形版，点按钮',
        'python3 ok -q Player.go_to              # 官方 doctest（Q2）',
        'python3 ok -q Player.talk_to            # Q3',
        'python3 ok -q Player.take               # Q4',
        'python3 ok -q Player.unlock             # Q5',
        'python3 -m doctest classes.py -v        # 直接跑 docstring 里的 doctest',
    ])
    rich(doc, [('提示 / note：', 'b'),
               ('README 第 5 节提到过，', 'n'), ('ok', 'code'),
               (' 服务器上的旧测试文件可能还在用老字符串（', 'n'),
               ('You are at GBC, Golden Bear Cafe - Now with...', 'code'),
               ('）；以 ', 'n'), ('classes.py', 'code'), (' 里的 docstring 为准。', 'n')],
         space_before=4)

    page_break(doc)
    heading(doc, '八', '拓展题的思路（对应原卷的手写答案）', 'extension ideas')

    rich(doc, [('这一节给的是一种**做法思路**，不是唯一答案；学生的实现可以完全不同。', 'g')],
         space_after=6)

    subheading(doc, 'E1 + E2  隐藏物品与「拿到宝藏才现身」的钥匙')
    rich(doc, [('思路是「加一个属性当标记，再在已有方法里多一个判断」，不用改类的结构：', 'n')])
    code_block(doc, [
        '# 1) 给 Thing 加一个「还没解锁」的标记',
        'class Thing(object):',
        '    def __init__(self, name, description):',
        '        self.name = name',
        '        self.description = description',
        '        self.locked = False          # 普通物品默认都是可拿的',
        '',
        '# 2) 让「生物楼」里的钥匙一开始是隐藏的',
        "skeleton_key = Key('Skeleton Key', '万能钥匙')",
        'skeleton_key.locked = True          # 标记成「还不能拿」',
        '',
        '# 3) look() 里对未解锁的物品不显示真名',
        'for thing in self.things.values():',
        '    if thing.locked == False:',
        "        print('   ', thing.name, '-', thing.description)",
        '    else:',
        "        print('   ', '???', '-', '只有拿到综合楼深处的宝物的人才能碰它。')",
        '',
        '# 4) take() 里也要挡住未解锁的物品',
        'if thing in self.place.things and self.place.things[thing].locked == False:',
        '    ... 正常拿走 ...',
        'else:',
        "    print('{} is not here.'.format(thing))",
    ])
    rich(doc, [('「拿到宝藏」这一步本身不需要新方法：让 ', 'n'), ('Treasure', 'code'),
               (' 继承 ', 'n'), ('Thing', 'code'), ('、在 ', 'n'), ('take()', 'code'),
               (' 里判断 ', 'n'), ('type(item) == Treasure', 'code'),
               ('，然后设一个状态标记（例如 ', 'n'), ('self.key_show = True', 'code'),
               ('），下次进入生物楼时把钥匙的 ', 'n'), ('locked', 'code'),
               (' 翻过来就行。', 'n')], space_before=6)

    note_box(doc, [
        [('为什么这样做是对的 / why this is sound：', 'b'),
         ('整个扩展只用了两样东西 —— **一个新属性**（', 'n'), ('locked', 'code'),
         (' / ', 'n'), ('key_show', 'code'), ('）和**几处已有的判断**。'
          '这正是面向对象里「加数据、改行为」最常见的做法。', 'n')],
        [('可以追问学生 / ask the class：', 'b'),
         ('如果不用多一个属性，还能怎么实现？'
          '（例如把钥匙换成一个只有在特定条件下才被加进 things 字典的对象。）', 'n')],
    ], fill='F0F6F0')

    heading(doc, '九', '课时分配建议', 'suggested timing')
    two_col_table(doc, [
        ('0–8 分钟', '读参考卡片：五个类的关系、三种数据访问方式'),
        ('8–20 分钟', 'Q2 go_to（含四种情况的输出）'),
        ('20–30 分钟', 'Q3 talk_to（字典查找 + 三种情况）'),
        ('30–42 分钟', 'Q4 take（顺序：取对象 → 放进背包 → 移除）'),
        ('42–60 分钟', 'Q5 Key + unlock（继承、多态、三种情况）'),
        ('60–75 分钟', '玩一局通关；有余力的做 E1/E2 隐藏剧情'),
    ], widths=(3.6, 12.8))

    drop_trailing_empty(doc)
    doc.save(path)
    return path


def main():
    worksheet = build_worksheet(os.path.join(HERE, '校园冒险-作业纸.docx'))
    answers = build_answers(os.path.join(HERE, '校园冒险-参考答案.docx'))
    for path in (worksheet, answers):
        print('已生成 / written: {}  ({:.1f} KB)'.format(
            os.path.basename(path), os.path.getsize(path) / 1024.0))


if __name__ == '__main__':
    main()
