from data import *

try:
    import readline
except ImportError:
    pass

##################################
# Name aliases / 名称别名
##################################

def localize_name(name):
    """把英文（或缩写）的名字换成 data.py 里的标准名字。

    Convert an English alias (e.g. 'GBC', 'Gibbes') into the canonical name used
    in data.py (e.g. '学生食堂', '吉布斯').  Unknown names are returned unchanged,
    so Chinese names and names defined by students keep working as before.
    """
    aliases = globals().get('ALIASES') or {}
    if name in aliases:
        return aliases[name]
    return aliases.get(name.lower(), name)

###########
# Parsing #
###########

def adv_parse(line):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    command = tokens.pop(0)
    if command in ('talk', 'go'):
        if not tokens or tokens[0] != 'to':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        operator, operand = command + '_to', ' '.join(tokens[1:])
    elif command == 'check':
        if not tokens or tokens[0] != 'backpack':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS['check backpack']))
        operator, operand = 'check_backpack', ''
    elif command == 'unlock':
        operator, operand = 'unlock', ' '.join(tokens)
    else:
        operator, operand = command, ' '.join(tokens)
    if operator in ('go_to', 'talk_to', 'take', 'unlock'):
        operand = localize_name(operand)
    return (operator, operand)

##############
# Evaluation #
##############

def adv_eval(exp):
    operator, operand = exp[0], exp[1]
    if operator not in COMMAND_NUM_ARGS:
        help()
        raise SyntaxError('Invalid command: {}'.format(operator))
    elif operator in SPECIAL_FORMS:
        function = SPECIAL_FORMS[operator]
    else:
        function = getattr(me, operator)

    if COMMAND_NUM_ARGS[operator] == 0:
        function()
    else:
        function(operand)

def help():
    print('There are {} possible commands / 一共有 {} 个命令:'.format(
        len(COMMAND_FORMATS), len(COMMAND_FORMATS)))
    for usage in COMMAND_FORMATS.values():
        print('   ', usage)

def check_win_state(player):
    """Checks if the player is in a winning state."""
    if player.place != hp:
        return False

    print()
    player_backpack = player.check_backpack()
    if 'Smoothie' in player_backpack and 'Lemon' in player_backpack:
        return True
    else:
        print()
        print("Looks like you're missing some items. Can't go to the study party yet!")
        print('你好像还缺一些东西，现在还不能去参加学习聚会！')
        print('(需要带上 Smoothie 奶昔 和 Lemon 柠檬。)')
        return False

########
# REPL #
########

def read_eval_print_loop():
    print(WELCOME_MESSAGE)
    if not isinstance(me, Player):
        print('Oh no! You need to create a player at the bottom of data.py to start the game.')
        print('糟糕！你需要在 data.py 的最后创建一个 Player 对象才能开始游戏。')
        return

    help()
    while True:
        if check_win_state(me):
            print(WIN_MESSAGE)
            return
        print()
        try:
            line = input('adventure> ')
            exp = adv_parse(line)
            adv_eval(exp)
        except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
            print('\nGood game. Bye!')
            return
        # If the player input was badly formed or if something doesn't exist
        except SyntaxError as e:
            print('ERROR:', e)

#################
# Configuration #
#################

COMMAND_FORMATS = {
    'look': 'look                     # 看看周围',
    'go': 'go to [place]             # 去往某个地点',
    'take': 'take [thing]             # 拿走某个物品',
    'talk': 'talk to [character]      # 和某个角色交谈',
    'check backpack': 'check backpack           # 查看背包',
    'help': 'help                     # 显示命令列表',
    'unlock': 'unlock [place]           # 用钥匙解锁某个地点',
}

COMMAND_NUM_ARGS = {
    'look': 0,
    'go_to': 1,
    'take': 1,
    'talk_to': 1,
    'check_backpack': 0,
    'help': 0,
    'unlock': 1,
}

SPECIAL_FORMS = {
    'help': help,
}

WELCOME_MESSAGE = """
Welcome to the adventure game!
欢迎来到冒险游戏！

It's a bright sunny day.
You are a bright and eager CS class student named {},
wandering around the campus looking for some snacks
before the study party.

今天阳光明媚。
你是一名聪明又好学的计算机系学生，名叫 {}，
正在校园里四处闲逛，想在学习聚会之前找到一些零食。

Let's go to FSM (Free Speech Movement Cafe)
and see what we can find there!

让我们先去咖啡厅（FSM）看看能找到什么吧！

（小提示：也可以运行 `python3 adventure_gui.py` 用图形界面来玩这个游戏。）
(Tip: you can also run `python3 adventure_gui.py` to play with a graphical interface.)
""".format(me.name if isinstance(me, Player) else '______',
           me.name if isinstance(me, Player) else '______')

WIN_MESSAGE = """
You arrive at the Auditorium just in time for the study party!
你正好赶上大礼堂的学习聚会！

Gibbes thanks you for bringing a non-disappointing smoothie.
Jen is pleased by the lemon you brought; now she can make lemonade!

吉布斯非常感谢你带来的那杯不让人失望的奶昔。
珍也很喜欢你带来的柠檬，现在她可以泡柠檬水了！

Congratulations! You won the adventure game!
恭喜你！你通关了冒险游戏！
"""


if __name__ == '__main__':
    read_eval_print_loop()
    input("Press enter to close the window...")
