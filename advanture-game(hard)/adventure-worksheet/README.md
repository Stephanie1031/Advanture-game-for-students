# 校园冒险游戏 · 打印用作业纸 / printable worksheet

这份作业纸是 **`../../student game/`（原校园冒险项目）的进阶任务**，
和简单版 `dino-pet-game/` 的作业纸配套：简单版练「一个类的数据」，
这一份练「**多个对象互相调用**」——`Player` 读 `Place`、查 `Character`、捡 `Thing`、用 `Key`。

**本文件夹完全独立**：里面的脚本只读取上级目录的 `classes.py` / `data.py` 用来做一致性检查，
不会改动原项目的任何文件。

| 文件 | 页数 | 用途 |
| --- | --- | --- |
| `校园冒险-作业纸.docx` | **6 页** | 学生用：参考卡片 + Q2 go_to + Q3 talk_to + Q4 take + Q5 unlock/Key + 预期输出对照 + 检查清单 + 拓展题 |
| `校园冒险-参考答案.docx` | **5 页** | 老师用：Q2–Q5 标准答案、评分要点、机检方式、常见错误、拓展题思路（对应原卷手写答案的思路）、课时分配 |
| `make_adventure_worksheet.py` | —— | 生成脚本 |
| `verify_docx.py` | —— | 自检脚本（见下） |
| `_docx_helpers.py` | —— | 和 `dino-pet-game/worksheet/` 共用的排版工具 |

## 版面 / layout

* **第 1 页** 姓名栏 + 参考卡片：五个类的关系图、三种数据访问方式
  （点号 / 方括号 / `get_neighbor`）、可直接调用的方法表。
* **第 2 页** Q2 `go_to` + Q3 `talk_to`：各含「已经给你的代码」「你要写什么」和书写横线。
* **第 3 页** Q4 `take`：三步提示 + 顺序注意事项 + 书写横线（留白较多，方便学生动笔）。
* **第 4 页** Q5 `unlock` + `Key`：继承与多态，两部分各自的分步提示。
* **第 5 页** 预期输出对照：Q2–Q5 的全部标准输出（含各种出错情况），来自 `classes.py` 的 docstring。
* **第 6 页** 检查清单 + 拓展题 E1–E7 + 课堂笔记横线。

## 拓展题思路 / extension ideas

`参考答案.docx` 第八节给了 E1/E2（隐藏物品、拿到宝藏才现身）的一种实现思路：
**加一个属性当标记 + 在已有方法里多一个判断**，不需要改类的结构。
原卷手写答案用的是 `Thing.locked` + `Player.key_show` + `Treasure` 子类这套组合，
作业纸只给了思路，学生可以用完全不同的做法实现。

## 重新生成与自检 / rebuild and verify

```bash
python3 -m pip install python-docx
python3 adventure-worksheet/make_adventure_worksheet.py    # 生成两份 docx
python3 adventure-worksheet/verify_docx.py                 # 自检
```

`verify_docx.py` 会检查：

1. docx 结构（18 个部件 XML 全部合法）
2. 每段中文都绑定了中文字体（作业纸 355 段 / 答案 228 段）
3. 分页后每页高度都在 A4 可打印区域内、没有空白页
4. **作业纸印出的 15 条预期输出，逐条都能在 `classes.py` 的 docstring 里找到**
5. **「已经给你的代码」6 处与实际 `classes.py` 原文一致**
6. 上级目录没有被新增文件、`classes.py` 仍是待完成的原状
