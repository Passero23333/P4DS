import random


def meToSay():
    say = input("你想说啥：\n")


def robotToSay():
    replies = ["你真棒", "真的嘛？", "然后呢~"]
    print(replies[random.randint(0, 3)])


meToSay()
robotToSay()
