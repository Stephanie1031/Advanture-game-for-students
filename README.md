[README.md](https://github.com/user-attachments/files/32544563/README.md)
# Adventure Game 冒险游戏

**中英双语作业说明 / Bilingual assignment guide**

我们要实现一个校园冒险游戏，练习 Python 里 **类（class）** 的写法。
题目原本来自国外大学的本科项目（伯克利的校园），为了方便理解，地名与角色名
已经做了**本地化**处理，并保留了英文原名方便对照。

We are going to write a campus adventure game to practise writing
**classes** in Python. The original project comes from an undergraduate
course abroad (a Berkeley campus); the place and character names have been
**localized** for clarity, with the original English names kept for reference.

> 题目正文（Q1 – Q6，中英双语）见 **[Questions.md](Questions.md)**。
> The questions themselves (Q1 – Q6, bilingual) live in **[Questions.md](Questions.md)**.

---

## 1. 怎么运行 / How to run

| 命令 Command | 说明 Description |
| --- | --- |
| `python3 adventure_gui.py` | **图形界面版**：点按钮就能玩，中文界面，可选双语。Graphical version - play by clicking buttons. |
| `python3 adventure.py` | **文字版**：在终端里输入命令。Text version - type commands in the terminal. |
| `python3 ok -q Player.go_to` | 用 ok 自动测试（`Player.talk_to` / `Player.take` / `Player.unlock` 同理）。Run the ok tests. |

文字版用 `Ctrl-C` 或 `Ctrl-D` 退出；图形版直接关窗口就行。
Quit the text version with `Ctrl-C` / `Ctrl-D`; just close the window for the GUI.

为了方便对照，仓库里还提供了完成版的 `adventure.exe`（Windows 可执行文件）。
For reference, a finished `adventure.exe` (Windows) is included as well.

### 图形界面里都有什么 / What the GUI gives you

* **当前位置 / Current place**：地点名 + 描述，还有「查看 Look」「检查背包
  Check backpack」按钮。
* **出口 Exits**：每个可以去的地方一个按钮，点一下就等于输入 `go to <地点>`；
  上锁的地方会显示 🔒，旁边多一个「解锁 Unlock」按钮。
* **这里的物品 Things here**：一件物品一个「拿走 Take」按钮（等于 `take <物品>`）。
* **这里的人 People here**：一个人一个「交谈 Talk to」按钮（等于 `talk to <角色>`）。
* **背包 Backpack**：实时显示背包里的东西。
* **游戏日志 Game log**：你代码里 `print` 出来的内容都会原样出现在这里，报错也会用红色显示。
* **命令输入框 Command box**：也可以直接敲命令，还支持英文别名（例如 `go to GBC`）。
* **提示 Hint / 命令列表 Help**：双语提示；如果某个方法还没写完，会告诉你
  它是 `classes.py` 的第几行。
* **重新加载代码 Reload code**：改完 `classes.py` / `data.py` 以后不用重启程序。
* **语言 Language**：`双语 Both` / `中文` / `English`。

图形界面只是外壳：**它调用的是你自己写的 `Player.go_to` / `talk_to` / `take` /
`unlock`**。所以作业没写完时界面也能打开，只是点了按钮不会有反应——那正是提醒你
「这个方法还没写完」。

The GUI is only a shell: it calls **your** `Player.go_to` / `talk_to` / `take` /
`unlock`. It opens fine even when the assignment is unfinished - clicking just
does nothing, which is your cue that the method is still empty.

---

## 2. 文件说明 / Files

| 文件 File | 要不要改？Edit? | 作用 Purpose |
| --- | --- | --- |
| `classes.py` | ✅ **要改 / yes** | 类的定义：补全 `Player.go_to / talk_to / take / unlock`，实现 `Key`。 |
| `data.py` | ✅ 只改最后一行 / last line only | 游戏数据（角色/物品/地点），以及你自己创建的 `Player` 对象。 |
| `adventure.py` | ❌ 不要改 / no | 文字版入口：解析命令 + 游戏主循环。 |
| `adventure_gui.py` | ❌ 不要改 / no | 图形版入口：把游戏画成按钮和面板。 |
| `Questions.md` | ❌ 不要改 / no | 题目与提示（Q1 – Q6，中英双语）。 |
| `README.md` | ❌ 不要改 / no | 你正在看的这个文件。 |

> `classes.py` 里每个方法都带着 **docstring + doctest**，它说明了老师期望的输出格式，
> 也就是「题目要求」。实现完以后用 `python3 ok -q <方法名>` 检查。
> Every method in `classes.py` carries a docstring with doctests - that is the
> specification of the expected output. Test your work with
> `python3 ok -q <question name>`.

---

## 3. 本地化对照表 / Localization map

地名按「中国大学校园场景」改写，变量名（`sather_gate`、`fsm`……）保持不变，
这样作业说明和代码仍能对应上。描述里保留了原英文名。
Place names were re-themed as a Chinese campus scene; the Python variable names
(`sather_gate`, `fsm`, …) are unchanged so the instructions still match the code.

| 变量名 Variable | 原地名 Original | 本地化名 Localized | 有什么 What is there |
| --- | --- | --- | --- |
| `sather_gate` | Sather Gate | **二校门** | 出发点，玩家的起始位置 |
| `fsm` | FSM (Free Speech Movement Cafe) | **咖啡厅** | 🔒 上锁；里面有 `Smoothie`、`Coffee` |
| `vlsb` | VLSB | **生物楼** | 恐龙骨架；`Skeleton Key`；詹姆斯 |
| `soda` | Soda Hall | **计算机系馆** | 吉布斯、珍、另一个杰瑞 |
| `gbc` | GBC (Golden Bear Cafe) | **学生食堂** | `Lemon` |
| `campanile` | Campanile | **钟楼** | 蒂凡尼 |
| `shattuck` | Shattuck Avenue | **商业街** | 通往游戏店 |
| `game_store` | Games on Shattuck | **游戏店** | 桌游《大富翁》 |
| `wheeler` | Wheeler Hall | **阶梯教室** | CS 上课的地方；杰瑞 |
| `dwinelle` | Dwinelle Hall | **综合楼** | 迷宫；迷路的同学 |
| `deep_dwinelle` | Deep in Dwinelle | **综合楼深处** | 两位迷路的同学、`Strange Skull` |
| `memorial_glade` | Memorial Glade | **大草坪** | 艾伦 |
| `hp` | HP Auditorium | **大礼堂** | 🏁 终点：学习聚会，带 `Smoothie` + `Lemon` 到这里就赢了 |

角色 / Characters：James → 詹姆斯，Gibbes → 吉布斯，Jen → 珍，Jerry → 杰瑞（
咖啡厅和阶梯教室各有一个，这是个梗），Tiffany → 蒂凡尼，Allen → 艾伦，
Student → 同学，Terrified / Spooked Student → 迷路的同学 / 吓坏的同学。

物品名保持英文 / Item names stay English（`Smoothie`、`Lemon`、`Coffee`、
`Skeleton Key`、`Strange Skull`、`大富翁`），因为胜利条件里会检查
`'Smoothie'` 和 `'Lemon'`。物品的描述里有中文说明。

### 英文别名 / English aliases

`data.py` 末尾新增了一张 `ALIASES` 表，所以下面的写法都合法，喜欢英文的同学不用改任何代码：
`data.py` also ships an `ALIASES` table, so all of these work:

```text
go to GBC          ==  go to 学生食堂
go to Soda         ==  go to 计算机系馆
go to Deep Dwinelle==  go to 综合楼深处
talk to Gibbes     ==  talk to 吉布斯
take lemon         ==  take Lemon
unlock FSM         ==  unlock 咖啡厅
```

---

## 4. 常见问题 / FAQ

**Q: 游戏打不开，提示 `Oh no! You need to create a player...`**
还没完成 Q1：请在 `data.py` 最后一行创建 `Player` 对象，例如
`me = Player("你的名字", sather_gate)`。图形界面里创建完点「重新加载代码」即可。

**Q: 调用 `unlock` 时报 `NameError`**
这是正常的：`Player.unlock` 里用到了 `Key`，你还没实现 `Key` 类。先完成 Q5。
In English: that is expected - `Player.unlock` refers to the `Key` class you have
not written yet. Finish Q5.

**Q: 按钮点了没反应？**
看日志窗口的蓝色提示，它会指出对应方法是不是还没写完（会给出 `classes.py` 的行号）。
Check the blue hints in the log - they point at the unfinished method and line.

**Q: 关于 `go_to` 应该打印什么？**
统一格式是 `You are at <地点名>, <描述>.`（例如
`You are at 二校门, Sather Gate - 一座谈不上有效的校门。`）。注意三件事：
目的地没上锁时要更新 `me.place`；门锁着时不要移动；无论哪种情况最后都要打印这一行。
The unified format is `You are at <name>, <description>.`: update `self.place` when
the destination is unlocked, stay put when it is locked, and always print that line.

---

## 5. 给老师 / 助教的说明 Notes for instructors

* 新增 `adventure_gui.py`：图形界面外壳，学生不需要修改。它通过 `importlib`
  载入 `classes.py` / `data.py`，捕获学生代码里 `print` 的输出显示到日志区，
  并用「状态指纹」判断一次操作有没有真的生效，从而给出「这个方法还没写完」的提示。
  It loads `classes.py` / `data.py`, captures `print` output into the log, and
  detects no-op actions to hint at unimplemented methods.
* 新增双语提示：`README.md` 与 `Questions.md` 改为中英双语；`classes.py` 只增加了
  注释，并把 `Player.go_to` 的期望输出统一（见下一条），其余 docstring 与代码未动。
  Bilingual docs were added; inside `classes.py` only comments were added, plus the
  `Player.go_to` expected output was unified (next bullet). Nothing else changed.
* 新增 `data.py` 的 `ALIASES` 别名表，`adventure.py` 的 `adv_parse` 会在解析后
  做一次「别名 → 中文名」的转换（不改变命令语法）。
* 题目已统一输出格式 / unified output format：`Player.go_to` 的规则是
  `You are at <地点名>, <描述>.`。原先 `go_to` 与 `unlock` 两处 doctest 的期望输出
  互相矛盾（一个带描述、一个只有地名），现在 `classes.py`、`Questions.md` 与
  `README.md` 都已按这个规则改好，并验证过可以用同一个实现同时通过。
  The `go_to` / `unlock` doctests used to disagree; both now expect
  `You are at <name>, <description>.`, and a single reference implementation passes
  every doctest in `classes.py`.
  提醒：如果服务器上的 `ok` 测试文件里写的是旧字符串（例如
  `You are at GBC, Golden Bear Cafe - Now with (healthy?) food.`），需要同步更新；
  本地的 `.ok_storage.db` 是加密的，无法在这里核对。
* 如果想调整本地化用词，只改 `data.py` 里的名字（以及 `ALIASES`）即可，
  `adventure_gui.py` 会自动跟着变。
