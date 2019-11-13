#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：雍腾
日期：2019/11/14
"""
import random
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
	    num=0
    elif name=="史波克":
	    num=1
    elif name=="纸":
	    num=2
    elif name=="蜥蜴":
	    num=3
    elif name=="剪刀":
	    num=4
    else:
	    print("Error: No Correct Name")
    return num
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        comp_name="石头"	
    elif number==1:
        comp_name="史波克"	
    elif number==2:
        comp_name="纸"
    elif number==3:
        comp_name="蜥蜴"
    else:
        comp_name="剪刀"
    return comp_name
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("--------")
    player_choice=choice_name
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("计算机的选择为：%s"%comp_choice)
    if comp_number==0:
        if player_choice_number==1 or player_choice_number==2:
            print("你输了！")
        else:
            print("你输了！")
    elif comp_number==1:
        if player_choice_number==3 or player_choice_number==2:
            print("你赢了！")
        else:
            print("你输了！")
    elif comp_number==2:
        if player_choice_number==4 or player_choice_number==3:
            print("你赢了！")
        else:
            print("你输了！")   
    elif comp_number==3:
        if player_choice_number==4 or player_choice_number==0:
            print("你赢了！")
        else:
            print("你输了！")
    elif comp_number==4:
        if player_choice_number==1 or player_choice_number==0:
            print("你赢了！")
        else:
            print("你输了！")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


