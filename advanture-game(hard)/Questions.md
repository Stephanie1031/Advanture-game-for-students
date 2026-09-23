# Adventure Game 题目 / Assignment Questions（中英双语）

我们将会实现一个基于文本的冒险游戏。你可以通过执行 `adventure.py` 来开始游戏
（图形界面版是 `adventure_gui.py`，玩法一样，点按钮即可）。

We are going to implement a text-based adventure game. Run `adventure.py` to play
it (`adventure_gui.py` is the graphical version - same game, clickable buttons).

* 文字版用命令 `Ctrl-C` 或者 `Ctrl-D` 退出；图形版直接关窗口。
  Quit the text version with `Ctrl-C` / `Ctrl-D`; close the window for the GUI.
* 什么时候都可以用 `python3 ok -q <题目名>` 来自测（例如
  `python3 ok -q Player.go_to`）。
  Test yourself at any time with `python3 ok -q <question>`, e.g.
  `python3 ok -q Player.go_to`.
* 地名与角色名已经做了本地化处理，对照表见 [README.md](README.md) 第 3 节。
  Place and character names are localized; see section 3 of [README.md](README.md).

为了使得结果更加直观，仓库里还提供了完成后的 EXE 版本供参考，详情可点击
`adventure` 文件夹中的可执行文件进行游玩。
For reference, a finished `adventure.exe` (Windows) is included in this folder.

---

## Compulsory Questions 必做题

### Q1: Who am I? 我是谁？

首先，你需要为你自己在 `data.py` 中创建一个 `Player` 对象。看一下 `classes.py`
中 `Player` 类的定义，然后在 `data.py` 底部创建一个 `Player` 对象。

First, create a `Player` object for yourself in `data.py`. Read the definition of
the `Player` class in `classes.py`, then create a `Player` object at the bottom of
`data.py`.

`Player` 构造函数接收两个参数 / the constructor takes two arguments:

* `name` 是你喜欢的名字（string 类型）/ your name (a string)
* 开始的位置 `place` / the place you start in

你的玩家将会从**二校门**（变量名 `sather_gate`）开始，改动代码位置：
Your player should start at 二校门 (`sather_gate`):

```python
    Player:
    The Player should start at sather_gate.
    "*** YOUR CODE HERE ***"
    me = None
```

例如 / for example：`me = Player("小明", sather_gate)`

创建完成之后就可以启动游戏了 / then run the game:

```bash
python3 adventure_gui.py     # 图形界面 / graphical
python3 adventure.py         # 文字版 / text
```

你会看到下面这些输出（可能顺序有所不同）/ you should see something like:

```
    Welcome to the adventure game!
    欢迎来到冒险游戏！

    It's a bright sunny day.
    You are a bright and eager CS class student named xxx, wandering around the
    campus looking for some snacks before the study party.

    今天阳光明媚。你是一名聪明又好学的计算机系学生，名叫 xxx，
    正在校园里四处闲逛，想在学习聚会之前找到一些零食。

    Let's go to FSM (Free Speech Movement Cafe) and see what we can find there!
    让我们先去咖啡厅（FSM）看看能找到什么吧！

    There are 7 possible commands / 一共有 7 个命令:
        look                     # 看看周围
        go to [place]            # 去往某个地点
        take [thing]             # 拿走某个物品
        talk to [character]      # 和某个角色交谈
        check backpack           # 查看背包
        help                     # 显示命令列表
        unlock [place]           # 用钥匙解锁某个地点
```

最后玩家需到达 **大礼堂**（`HP Auditorium`）参加学习聚会，但在此之前，我们可以
指挥玩家在校内走动，为学习聚会准备一些零食与桌游 😊
The goal is to reach 大礼堂 (`hp`) for the study party - but first, walk around the
campus and collect some snacks and a board game.

目前你现在除了 `look` 什么都做不了，让我们来继续完善它！
Right now nothing works except `look`. Let's fix that.

### Q2: Where do I go? 我能去哪里？

首先，我们需要能够移动到不同的地方。如果你试着使用 `go to` 命令，你会发现什么也
没有发生。

First we need to be able to move around. Try `go to` and notice that nothing
happens.

在 `classes.py` 中，完成 `Player` 类的 `go_to` 方法，让地点**没有锁住**的情况下，
它能够将你的 `place` 属性更新成 `destination_place`，并且你还需要输出当前位置的名称。

In `classes.py`, finish `Player.go_to` so that, when the destination is **not
locked**, it updates your `place` attribute to `destination_place` and prints
where you are now.

代码框架 / the skeleton:

```python
    def go_to(self, location):
        """Go to a location if it's among the exits of player's current place.

        >>> sather_gate = Place('Sather Gate', 'Sather Gate', [], [])
        >>> gbc = Place('GBC', 'Golden Bear Cafe', [], [])
        >>> sather_gate.add_exits([gbc])
        >>> sather_gate.locked = True
        >>> gbc.add_exits([sather_gate])
        >>> me = Player('player', sather_gate)
        >>> me.go_to('GBC')
        You are at GBC, Golden Bear Cafe.
        >>> me.place is gbc
        True
        >>> me.place.name
        'GBC'
        >>> me.go_to('GBC')
        Can't go to GBC from GBC.
        Try looking around to see where to go.
        You are at GBC, Golden Bear Cafe.
        >>> me.go_to('Sather Gate')
        Sather Gate is locked! Go look for a key to unlock it
        You are at GBC, Golden Bear Cafe.
        """
        destination_place = self.place.get_neighbor(location)
        if destination_place.locked:
            print(destination_place.name, 'is locked! Go look for a key to unlock it')
        "*** YOUR CODE HERE ***"
```

提示 / Hints：

1. 只有当目的地没有上锁（`destination_place.locked` 是 `False`）时才移动：
   `self.place = destination_place`。写完 `if` 之后别忘了 `else`。
   Only move when the destination is not locked: `self.place = destination_place`.
2. 移动之后要打印玩家现在在哪里，统一格式是 `You are at <地点名>, <描述>.`
   （注意最后的句点，别漏掉）。例如 `You are at 二校门, Sather Gate - 一座谈不上有效的校门。`
   Print where the player is now. The unified format is
   `You are at <name>, <description>.` (do not forget the final period).
   注意：不管是成功了、地点不存在、还是门锁着，最后都要打印这一行。
   Whichever branch you take, that line is always printed at the end.
3. `get_neighbor` 在名字写错时会打印提示并返回**原地**，这时上面的输出同样要正确。
   `get_neighbor` returns the current place when the name is unknown.
4. 上锁的地点会在你完成 Q5 之后才能用钥匙打开。
   Locked places can only be opened with a key (Q5).

使用 `ok` 命令来进行测试 / test with ok：

```bash
python3 ok -q Player.go_to
```

当你完成了这个问题之后，你将可以移动到不同的位置并且进行查看（`look`）。为了完善
游戏的功能，包括和 NPC 交谈以及捡起东西，你需要完成以下可选问题。
After this you can move around and use `look`. The optional questions add talking
to characters, picking up things, and unlocking doors.

---

## Optional Questions 选做题

### Q3: How do I talk? 怎么和人说话？

现在你已经可以去你想去的地方了，试着去往 **阶梯教室**（`Wheeler`）。在那里你可以
找到 **杰瑞**（`Jerry`）。通过 `talk to` 命令和它对话。这现在仍然不会生效。

Now that you can move, go to 阶梯教室 (`Wheeler`) where you will find 杰瑞
(`Jerry`) and try `talk to`. It still does nothing.

接着，实现 `Player` 中的 `talk_to` 方法。`talk_to` 接收一个角色的名称，并且打印出
它的反应。查看下面代码获取更多细节。
Implement `Player.talk_to`. It receives the name of a character and prints its
reply.

提示 / Hints：

* `talk_to` 接收一个参数 `person`，它是一个字符串。
  `person` is a string.
* `self.place` 中的实例属性 `characters` 是一个字典，把角色的名称和角色对象映射起来。
  `self.place.characters` maps names to `Character` objects.
* 当你拿到角色对象之后，你需要用 `Character` 类中的什么方法来进行交谈呢？
  Which `Character` method gives you the message?

```python
    def talk_to(self, person):
        """Talk to person if person is at player's current place.

        >>> jerry = Character('Jerry', 'I am not the Jerry you are looking for.')
        >>> wheeler = Place('Wheeler', 'You are at Wheeler', [jerry], [])
        >>> me = Player('player', wheeler)
        >>> me.talk_to(jerry)
        Person has to be a string.
        >>> me.talk_to('Jerry')
        Jerry says: I am not the Jerry you are looking for.
        >>> me.talk_to('Tiffany')
        Tiffany is not here.
        """
        if type(person) != str:
            print('Person has to be a string.')

        "*** YOUR CODE HERE ***"
```

`Character` 类的定义 / the `Character` class:

```python
class Character(object):
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def talk(self):
        return self.message
```

### Q4: How do I take items? 怎么捡东西？

现在让我们实现 `take` 命令，让玩家可以往 `backpack` 中放入道具。目前，你没有背包
（`backpack`），所以让我们创建一个实例变量 `backpack`，将它初始化成空的 `list`。

Implement the `take` command so the player can put things into their `backpack`.
The player has no backpack yet, so create the instance variable `backpack` and
initialize it to an empty `list`.

当你初始化你的空背包之后，实现 `take` 方法，它接收一个物品的名称，检查你所在的位置
是否有这件道具（`Thing`），接着将它放入你的背包。查看代码获取更多细节。
`take` receives the name of a thing, checks whether it is at your current place,
and puts it into your backpack.

提示 / Hints：

* `things` 是 `Place` 类的实例属性，它将物品名称和对象映射起来。
  `Place.things` maps names to `Thing` objects.
* `Place` 类中的 `take` 方法也能派上用场，它的作用是使得物品被拿走后该地的物品被移除。
  `Place.take` removes the thing from the place.

```python
    def take(self, thing):
        """Take a thing if thing is at player's current place

        >>> lemon = Thing('Lemon', 'A lemon-looking lemon')
        >>> gbc = Place('GBC', 'You are at Golden Bear Cafe', [], [lemon])
        >>> me = Player('Player', gbc)
        >>> me.backpack
        []
        >>> me.take(lemon)
        Thing should be a string.
        >>> me.take('orange')
        orange is not here.
        >>> me.take('Lemon')
        Player takes the Lemon
        >>> me.take('Lemon')
        Lemon is not here.
        >>> isinstance(me.backpack[0], Thing)
        True
        >>> len(me.backpack)
        1
        """
        if type(thing) != str:
            print('Thing should be a string.')

        "*** YOUR CODE HERE ***"
```

使用 ok 命令来测试 / test with ok：

```bash
python3 ok -q Player.take
```

### Q5: No door can hold us back! 没有门能挡得住我们！

**咖啡厅**（`FSM`）锁上了，我们没有办法进去。而你已经对无法喝到甜美可口的咖啡
感到非常绝望了。

咖啡厅 (`FSM`) is locked and we cannot get in - and you are desperate for coffee.

为了进入咖啡厅并且摄入咖啡因，我们需要做两件事情。首先，我们需要创建一个新的类型
`Key`，它是 `Thing` 的子类，但重载了 `use` 方法来打开咖啡厅的门。
We need to do two things: create a new type `Key` that is a subclass of `Thing` but
overrides the `use` method to open the door, and then unlock the door.

提示 / Hints：

1. `Place` 有一个 `locked` 实例属性，你可能需要改动它。
   `Place` has a `locked` attribute you probably need to change.
2. 我们拿到的是要开启的地点的 string，而不知道这个名称对应的对象。这需要我们使用
   `Place` 的 `get_neighbor`（或 `get_neighbour`）函数。
   We get the *name* of the place as a string; use `Place.get_neighbor` to turn it
   into a `Place` object.

```python
    def unlock(self, place):
        """If player has a key, unlock a locked neighboring place.

        >>> key = Key('SkeletonKey', 'A Key to unlock all doors.')
        >>> gbc = Place('GBC', 'Golden Bear Cafe', [], [key])
        >>> fsm = Place('FSM', 'Home of the nectar of the gods', [], [])
        >>> gbc.add_exits([fsm])
        >>> fsm.locked = True
        >>> me = Player('Player', gbc)
        >>> me.unlock(fsm)
        Place must be a string
        >>> me.go_to('FSM')
        FSM is locked! Go look for a key to unlock it
        You are at GBC, Golden Bear Cafe.
        >>> me.unlock(fsm)
        Place must be a string
        >>> me.unlock('FSM')
        FSM can't be unlocked without a key!
        >>> me.take('SkeletonKey')
        Player takes the SkeletonKey
        >>> me.unlock('FSM')
        FSM is now unlocked!
        >>> me.unlock('FSM')
        FSM is already unlocked!
        >>> me.go_to('FSM')
        You are at FSM, Home of the nectar of the gods.
        """
        if type(place) != str:
            print("Place must be a string")
            return
        key = None
        for item in self.backpack:
            if type(item) == Key:
                key = item
        "*** YOUR CODE HERE ***"
```

```python
class Thing(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, place):
        print("You can't use a {0} here".format(self.name))

""" Implement Key here! """
```

提示 / Hints：

* `Key` 是 `Thing` 的子类：写出它的 `__init__` 和 `use` 方法，`__init__` 里用
  `Thing.__init__(self, name, description)` 初始化。
  `Key` subclasses `Thing`: give it an `__init__` (calling `Thing.__init__`) and a
  `use` method.
* `use` 会在玩家解锁某个地点时被调用。想想：`use` 的参数是地点名（字符串）还是
  `Place` 对象？两种写法都可以，但要和 `unlock` 里调用它的方式一致。
  `use` is called when the player unlocks a place; decide whether it takes a name
  or a `Place`, and keep `unlock` consistent with that choice.
* 在你实现 `Key` 之前，`data.py` 里的 `skeleton_key` 会退化成普通 `Thing`
  （`data.py` 用 `try/except NameError` 做了保护），`unlock` 也会报 `NameError`——
  这正是提醒你该写 `Key` 了。
  Until `Key` exists, `data.py` falls back to a plain `Thing` and `unlock` raises
  `NameError` - your reminder to implement `Key`.
* 钥匙在 **生物楼**（`VLSB`）。
  The key is in 生物楼 (`VLSB`).

使用 ok 命令来测试 / test with ok：

```bash
python3 ok -q Player.unlock
```

### Q6: 最简单的一集 / The easiest one

现在你可以在校园里到处走动以及尝试着赢得游戏了。和各个地方的人交谈来获取提示。
你能拯救这一天并且赶上学习聚会吗？

Now you can walk around campus and try to win the game. Talk to people everywhere
to get hints. Can you save the day and make it to the study party?

* 目标：带上一杯奶昔（`Smoothie`）和一个柠檬（`Lemon`），到达 **大礼堂**。
  Goal: bring a `Smoothie` and a `Lemon` to 大礼堂.
* 奖励：`Coffee`（咖啡）、桌游《大富翁》、`Strange Skull`……
  Extras: coffee, a board game, a strange skull…

Have a great time! 玩得开心！

<details>
<summary>轻度剧透：一条可行路线 / mild spoiler: one working route</summary>

```
二校门 → 学生食堂 (take Lemon) → 二校门 → 综合楼 → 生物楼
      → 生物楼 (take Skeleton Key) → unlock 咖啡厅 → 咖啡厅 (take Smoothie)
      → 生物楼 → 计算机系馆 → 大礼堂  🏆
```

</details>
