#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

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
#��дִ�д���,������ɺ�passɾ��


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
 #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    print("--------")# ���"-------- "���зָ�
    player_choice=choice_name# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    comp_number=random.randrange(0,5)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    comp_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("�������ѡ��Ϊ��%s"%comp_choice)# ����Ļ����ʾ�����ѡ����������

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

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


