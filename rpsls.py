#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�Ӻ��
���ڣ�2019/11/14
"""
import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
	    num=0
    elif name=="ʷ����":
	    num=1
    elif name=="ֽ":
	    num=2
    elif name=="����":
	    num=3
    elif name=="����":
	    num=4
    else:
	    print("Error: No Correct Name")
    return num
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        comp_name="ʯͷ"	
    elif number==1:
        comp_name="ʷ����"	
    elif number==2:
        comp_name="ֽ"
    elif number==3:
        comp_name="����"
    else:
        comp_name="����"
    return comp_name
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    print("--------")# ���"-------- "���зָ�
    player_choice=choice_name
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("�������ѡ��Ϊ��%s"%comp_choice)
    if comp_number!=player_choice_number:
        if comp_number==0:
            if player_choice_number==1 or player_choice_number==2:
                print("�����ˣ�")
            else:
                print("�����ˣ�")
        elif comp_number==1:
            if player_choice_number==3 or player_choice_number==2:
                print("��Ӯ�ˣ�")
            else:
                print("�����ˣ�")
        elif comp_number==2:
            if player_choice_number==4 or player_choice_number==3:
                print("��Ӯ�ˣ�")
            else:
                print("�����ˣ�")   
        elif comp_number==3:
            if player_choice_number==4 or player_choice_number==0:
                print("��Ӯ�ˣ�")
            else:
                print("�����ˣ�")
        elif comp_number==4:
            if player_choice_number==1 or player_choice_number==0:
                print("��Ӯ�ˣ�")
            else:
                print("�����ˣ�")
    else:
        print("���ͼ��������һ����")
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
