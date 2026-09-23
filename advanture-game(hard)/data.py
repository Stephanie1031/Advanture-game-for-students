# CS World Game Data / 游戏世界数据
#
# 这个文件里定义了游戏世界中的全部角色（Character）、物品（Thing）与地点（Place）。
# 学生通常不需要修改它：只需要在文件最后一行创建你自己的 Player 对象（见 Q1）。
#
# This file defines every character, thing and place of the game world.
# You normally do not need to edit it: only `me = ...` at the very bottom (see Q1).
#
# 本地化说明 / Localization
#   1. 地点名与角色名已本地化为中文校园场景（描述里保留原英文名，便于和英文题面对照）。
#      Place and character names are localized to Chinese campus scenes; the original
#      English names are kept inside the descriptions for reference.
#   2. 物品名保持英文，因为胜利条件会用到 'Smoothie' 和 'Lemon'。
#      Item names stay in English because the win condition checks
#      for 'Smoothie' and 'Lemon'.
#   3. 文件末尾的 ALIASES 表让你仍然可以输入英文或缩写，例如
#      `go to GBC`、`talk to Gibbes`、`take lemon`。
#      The ALIASES table at the bottom lets you keep typing English names.
from classes import *

# Characters / 角色：

james = Character('詹姆斯',
                  '我在计算机系馆那边看到吉布斯拿着一杯奶昔，去那儿应该能找到他。\n'
                  '(EN) I saw Gibbes near Soda with a smoothie. '
                  'You can probably find him there.')
gibbes = Character('吉布斯',
                   '这杯奶昔也太让人失望了！真希望有人能给我带一杯不让人失望的奶昔。\n'
                   '(EN) This smoothie is so disappointing! '
                   'I wish someone would bring me a non-disappointing smoothie.')
jen = Character('珍',
                '没人带吃的来学习聚会！也许学生食堂还开着，我们可以去那儿弄点吃的。\n'
                '(EN) No one brought food to the potluck! '
                'Maybe the Golden Bear Cafe (GBC) is open; we can get food there.')
jerry_113 = Character('杰瑞',
                      '你刚刚在阶梯教室看到我？可我一直在这儿啊！\n'
                      "(EN) You just saw me in Wheeler? But I've been here all along!")
tiffany = Character('蒂凡尼',
                    '我的马克笔没墨了，所以没法在这座塔上涂鸦了！\n'
                    "(EN) My marker ran out of ink, so I can't vandalize this tower!")
jerry = Character('杰瑞',
                  '听说你喜欢游戏，所以我把游戏放进了这个游戏里。你去过商业街的游戏店吗？\n'
                  '(EN) I heard you like games, so I put some games in this game. '
                  'Have you gone to Games on Shattuck?')
allen = Character('艾伦',
                  '嘿！想一起玩飞盘吗？\n'
                  '(EN) Hey! Want to play ultimate frisbee?')
student = Character('同学',
                    '我有一次走进综合楼，结果迷路了三天！那地方就是个迷宫！\n'
                    '(EN) I once went into Dwinelle and got lost for 3 days! '
                    'That place is a maze!')
scared_student = Character('迷路的同学',
                           '我已经在综合楼里迷路好几个星期了……\n'
                           "(EN) I've been lost in Dwinelle for weeks.")
spooked_student = Character('吓坏的同学',
                            '救命……\n'
                            '(EN) Help')

# Things / 物品：
smoothie = Thing('Smoothie',
                 '一杯奶昔（Smoothie）- 看起来一点也不让人失望，吉布斯应该会想要它。')
lemon = Thing('Lemon',
              '一个柠檬（Lemon）- 嗯……也许可以带给助教（TA）？')
coffee = Thing('Coffee',
               '咖啡（Coffee）- 甜美、提神的咖啡因甘露。')
monopoly = Thing('大富翁',
                 '桌游《大富翁》（Monopoly）- 学习间隙玩正合适！')
strange_skull = Thing('Strange Skull',
                      '奇怪的骷髅（Strange Skull）- 恐龙？长颈鹿？谁知道呢。')

# Keys / 钥匙：
try:
    skeleton_key = Key('Skeleton Key', '万能钥匙（Skeleton Key）- 可以打开很多扇门的钥匙')
except NameError as e:
    skeleton_key = Thing('Not a Skeleton Key',
                         'You must first implement the Key class / 你需要先在 classes.py 里实现 Key 类')

# Places / 地点：
# 描述的形式是「英文原名 — 中文说明」：既方便和英文题面对照，又不会和地点名重复
# （Player.go_to 会打印 `You are at <名称>, <描述>.`）。
# Descriptions read "<English original> - <Chinese note>", so they never repeat the
# place name itself (go_to prints `You are at <name>, <description>.`).

sather_gate = Place('二校门', 'Sather Gate - 一座谈不上有效的校门。',
                    [], [])
fsm = Place('咖啡厅', 'FSM / Free Speech Cafe - 咖啡因之神的圣殿。',
            [], [smoothie, coffee])
vlsb = Place('生物楼', 'VLSB - 你见过楼里那只恐龙骨架吗？',
             [james], [skeleton_key])
soda = Place('计算机系馆', 'Soda Hall - 一栋不许喝汽水的楼。',
             [gibbes, jen, jerry_113], [])
gbc = Place('学生食堂', 'GBC / Golden Bear Cafe - 现在也有（据说）健康的饭了。',
            [], [lemon])
campanile = Place('钟楼', 'Campanile - 一座很棒的塔！',
                  [tiffany], [])
game_store = Place('游戏店', 'Games on Shattuck - 游戏中心！',
                   [], [monopoly])
hp = Place('大礼堂', 'HP Auditorium - 学习聚会就在这里举行。',
           [], [])
shattuck = Place('商业街', 'Shattuck Avenue - 学校旁边的商业街。',
                 [], [])
wheeler = Place('阶梯教室', 'Wheeler Hall - CS 的课都在这里上。',
                [jerry], [])
dwinelle = Place('综合楼', 'Dwinelle Hall - 一座迷宫。',
                 [student], [])
deep_dwinelle = Place('综合楼深处', 'Deep in Dwinelle Hall - 你已经迷路好多天了。',
                      [scared_student, spooked_student], [strange_skull])
memorial_glade = Place('大草坪', 'Memorial Glade - 天气真不错的草地。',
                       [allen], [])


# Exits / 出口：
sather_gate.add_exits([gbc, wheeler, dwinelle, memorial_glade])
gbc.add_exits([sather_gate])
wheeler.add_exits([sather_gate, campanile])
deep_dwinelle.add_exits([deep_dwinelle, dwinelle])
dwinelle.add_exits([sather_gate, vlsb, wheeler, deep_dwinelle])
memorial_glade.add_exits([sather_gate, fsm, campanile, soda])
campanile.add_exits([memorial_glade, wheeler])
vlsb.add_exits([fsm, soda, shattuck, dwinelle])
shattuck.add_exits([vlsb, game_store])
fsm.add_exits([vlsb, memorial_glade])
soda.add_exits([hp, vlsb, memorial_glade])
hp.add_exits([soda])
game_store.add_exits([shattuck])

# Locked Buildings / 上锁的建筑
fsm.locked = True

# Player / 玩家：
# 玩家应该从二校门开始。The Player should start at sather_gate.
"*** YOUR CODE HERE ***"
me = None


# ---------------------------------------------------------------------------
# 别名表 / Alias table
# ---------------------------------------------------------------------------
# 图形界面和终端都会先查这张表，所以下面这些写法都可以：
#   go to GBC  ==  go to 学生食堂        go to Soda  ==  go to 计算机系馆
#   talk to Gibbes == talk to 吉布斯     take lemon  ==  take Lemon
# 也就是说：地名、角色名本地化成中文之后，你依然可以用原来的英文来输入。
# The parser looks names up in this table first, so both the English original
# and the Chinese name always work.
ALIASES = {
    # Places / 地点
    'sather gate': '二校门',
    'sather': '二校门',
    'gate': '二校门',
    'gbc': '学生食堂',
    'golden bear cafe': '学生食堂',
    'cafeteria': '学生食堂',
    'fsm': '咖啡厅',
    'free speech cafe': '咖啡厅',
    'free speech movement cafe': '咖啡厅',
    'vlsb': '生物楼',
    'valley life sciences building': '生物楼',
    'soda': '计算机系馆',
    'soda hall': '计算机系馆',
    'campanile': '钟楼',
    'the campanile': '钟楼',
    'tower': '钟楼',
    'games': '游戏店',
    'game store': '游戏店',
    'games on shattuck': '游戏店',
    'shattuck': '商业街',
    'shattuck avenue': '商业街',
    'wheeler': '阶梯教室',
    'wheeler hall': '阶梯教室',
    'dwinelle': '综合楼',
    'dwinelle hall': '综合楼',
    'deep dwinelle': '综合楼深处',
    'deep in dwinelle': '综合楼深处',
    'deep in dwinelle hall': '综合楼深处',
    'memorial glade': '大草坪',
    'glade': '大草坪',
    'lawn': '大草坪',
    'hp': '大礼堂',
    'hp auditorium': '大礼堂',
    'auditorium': '大礼堂',
    # Characters / 角色
    'james': '詹姆斯',
    'gibbes': '吉布斯',
    'jen': '珍',
    'jerry': '杰瑞',
    'tiffany': '蒂凡尼',
    'allen': '艾伦',
    'student': '同学',
    'scared student': '迷路的同学',
    'terrified student': '迷路的同学',
    'spooked student': '吓坏的同学',
    # Things / 物品
    'smoothie': 'Smoothie',
    'lemon': 'Lemon',
    'coffee': 'Coffee',
    '奶昔': 'Smoothie',
    '柠檬': 'Lemon',
    '咖啡': 'Coffee',
    '钥匙': 'Skeleton Key',
    '骷髅': 'Strange Skull',
    'skeleton key': 'Skeleton Key',
    'key': 'Skeleton Key',
    'strange skull': 'Strange Skull',
    'skull': 'Strange Skull',
    'monopoly': '大富翁',
}
