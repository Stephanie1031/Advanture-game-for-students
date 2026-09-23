# A "simple" adventure game.
#
# 这个文件是作业的主要文件：你需要补全 Player 类里标着 YOUR CODE HERE 的
# 四个方法（go_to / talk_to / take / unlock），并实现 Key 类。
# This is the assignment's main file: complete the four Player methods marked
# "*** YOUR CODE HERE ***", and implement the Key class.
#
#   classes.py        类定义（需要你修改的文件）  Class definitions (the file you edit)
#   data.py           游戏数据（只有最后一行要改） Game data (only the last line changes)
#   adventure.py      文字版游戏入口（不要修改）   Text-mode entry point (do not edit)
#   adventure_gui.py  图形版游戏入口（不要修改）   GUI entry point (do not edit)
#   README.md / Questions.md  题目与双语提示        Questions and bilingual hints
#
# 每个方法的 docstring 里都写了 doctest，它说明了老师期望的输出格式。
# 写完以后可以用 `python3 ok -q Player.go_to` 这样的命令来测试。
# Each docstring contains doctests that show the expected output.  Test your work
# with commands such as `python3 ok -q Player.go_to`.

class Player(object):
    def __init__(self, name, place):
        """Create a player object."""
        self.name = name
        self.place = place
        self.backpack = []

    def look(self):
        self.place.look()

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
        # 提示 / Hints:
        #   1) 只有目的地没有上锁（not locked）时才移动：self.place = destination_place
        #      Only move when the destination is not locked.
        #   2) 移动之后要打印玩家现在在哪里，格式是 `You are at <地点名>, <描述>.`
        #      （注意句点；上面的 doctest 就是标准答案）。
        #      Print where the player is now, in the format
        #      `You are at <name>, <description>.` (the doctest above is the spec).
        #   3) 名字不存在时 get_neighbor 会返回原地，这时上面的输出同样要正确。
        #      get_neighbor returns the current place when the name is unknown.
        "*** YOUR CODE HERE ***"



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
        # 提示 / Hints:
        #   1) 先判断参数类型：只有 person 是字符串时才继续（参考上面的 if 和 doctest）。
        #      Only continue when person is a string.
        #   2) 用 self.place.characters 这个字典，通过名字拿到 Character 对象。
        #      Look the name up in self.place.characters to get the Character object.
        #   3) 找不到就说明这个人不在当前地点，打印 "<名字> is not here."
        #      If the name is not there, print '<name> is not here.'
        #   4) 找到了就调用 Character 中返回台词的那个方法，并打印 "<名字> says: <台词>"
        #      Otherwise call the Character method that returns the message and print
        #      '<name> says: <message>'

        "*** YOUR CODE HERE ***"




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
        # 提示 / Hints:
        #   1) 同样先判断参数类型，只有 thing 是字符串时才继续。
        #      Only continue when thing is a string.
        #   2) 用 self.place.things 这个字典判断这件物品是否就在当前地点。
        #      Check whether the thing is here with self.place.things.
        #   3) 不在就打印 "<名字> is not here."
        #      If it is not here, print '<name> is not here.'
        #   4) 在的话，把物品放进 self.backpack；Place 类的 take 方法可以帮你把物品
        #      从原地移除；再打印 "<玩家名> takes the <物品名>"，注意 doctest 里的顺序。
        #      Otherwise put it into self.backpack (the Place.take method removes it
        #      from the place) and print '<player name> takes the <thing name>'.
            
        "*** YOUR CODE HERE ***"
        

    def check_backpack(self):
        """Print each item with its description and return a list of item names.

        >>> cookie = Thing('Cookie', 'A huge cookie')
        >>> donut = Thing('Donut', 'A huge donut')
        >>> cupcake = Thing('Cupcake', 'A huge cupcake')
        >>> gbc = Place('GBC', 'You are at Golden Bear Cafe',
        ...             [], [cookie, donut, cupcake])
        >>> me = Player('Player', gbc)
        >>> me.check_backpack()
        In your backpack:
            there is nothing.
        []
        >>> me.take('Cookie')
        Player takes the Cookie
        >>> me.check_backpack()
        In your backpack:
            Cookie - A huge cookie
        ['Cookie']
        >>> me.take('Donut')
        Player takes the Donut
        >>> food = me.check_backpack()
        In your backpack:
            Cookie - A huge cookie
            Donut - A huge donut
        >>> food
        ['Cookie', 'Donut']
        """
        print('In your backpack:')
        if not self.backpack:
            print('    there is nothing.')
        else:
            for item in self.backpack:
                print('   ', item.name, '-', item.description)
        return [item.name for item in self.backpack]

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
        # 提示 / Hints:
        #   1) 上面已经帮你找出了背包里的钥匙（key）。如果 key 是 None，
        #      说明没有钥匙：打印 "<地点> can't be unlocked without a key!" 并返回。
        #      key is None means there is no key in the backpack: print
        #      '<place> can\'t be unlocked without a key!' and return.
        #   2) 如果目的地已经解锁（not locked），打印 "<地点> is already unlocked!"
        #      If the destination is not locked, print '<place> is already unlocked!'
        #   3) 否则，用 self.place.get_neighbor(place) 拿到要解锁的 Place 对象，
        #      再调用钥匙的 use 方法把它打开，最后打印 "<地点> is now unlocked!"
        #      Otherwise get the Place object with self.place.get_neighbor(place),
        #      call the key's use method on it, then print '<place> is now unlocked!'
        #   4) 注意：在你实现 Key 之前，上面那句 `type(item) == Key` 会报 NameError，
        #      这正说明你需要先去实现 Key 类。
        #      Until you implement Key, `type(item) == Key` raises NameError - that is
        #      your reminder to go implement the Key class.
        "*** YOUR CODE HERE ***"



class Character(object):
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def talk(self):
        return self.message


class Thing(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, place):
        print("You can't use a {0} here".format(self.name))

""" Implement Key here! """
# 提示 / Hints:
#   Key 是 Thing 的子类，你需要自己写出它的 __init__ 和 use：
#   Key is a subclass of Thing; write its own __init__ and use:
#     * __init__(self, name, description)：可以直接调用 Thing.__init__ 来初始化，
#       或者像下面的 Treasure 类一样用父类名调用父类构造函数。
#       Call Thing.__init__ (see the Treasure class below for the pattern).
#     * use(self, place)：玩家执行 unlock 时会调用它，参数 place 是一个字符串（地点名）。
#       use(self, place) is called when the player unlocks a place; place is a string.
#       先判断类型，再用 get_neighbor（或 get_neighbour）把名字变成 Place 对象，
#       最后把它的 locked 改成合适的状态。想一想：为什么钥匙需要 "地点" 而不是直接改 booleans？
#       Turn the name into a Place object, then change its locked attribute.
#   在实现 Key 之前，data.py 里的 skeleton_key 会退化成普通 Thing
#   （data.py 用 try/except NameError 做了保护），所以你拿不到真正的钥匙。
#   Until Key exists, data.py falls back to a plain Thing (see its try/except).



class Treasure(Thing):
    def __init__(self, name, description, value, weight):
        Thing.__init__(self, name, description)
        self.value = value
        self.weight = weight

class Place(object):
    def __init__(self, name, description, characters, things):
        self.name = name
        self.description = description
        self.characters = {character.name: character for character in characters}
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {} # {'name': (exit, 'description')}

    def look(self):
        print('You are currently at ' + self.name + '. You take a look around and see:')
        print('Characters:')
        if not self.characters:
            print('    no one in particular')
        else:
            for character in self.characters:
                print('   ', character)
        print('Things:')
        if not self.things:
            print('    nothing in particular')
        else:
            for thing in self.things.values():
                print('   ', thing.name, '-', thing.description)
        self.check_exits()

    def get_neighbor(self, exit):
        """
        >>> sather_gate = Place('Sather Gate', 'You are at Sather Gate', [], [])
        >>> gbc = Place('GBC', 'You are at Golden Bear Cafe', [], [])
        >>> gbc.add_exits([sather_gate])
        >>> place = gbc.get_neighbor('Sather Gate')
        >>> place is sather_gate
        True
        >>> place = gbc.get_neighbor('FSM')
        Can't go to FSM from GBC.
        Try looking around to see where to go.
        >>> place is gbc
        True
        """
        if type(exit) != str:
            print('Exit has to be a string.')
            return self
        elif exit in self.exits:
            exit_place = self.exits[exit][0]
            return exit_place
        else:
            print("Can't go to {} from {}.".format(exit, self.name))
            print("Try looking around to see where to go.")
            return self

    def take(self, thing):
        return self.things.pop(thing)

    def check_exits(self):
        print('You can exit to:')
        for exit in self.exits:
            print('   ', exit)

    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)
