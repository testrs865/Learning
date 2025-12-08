class Dice:
    def __init__(self, dice_list):
        self.dice_list = dice_list
        #self.dice_list_cpy = dice_list[:]

    def move_n(self):
        self.dice_list[0], self.dice_list[1], self.dice_list[4], self.dice_list[5] = self.dice_list[1], self.dice_list[5], self.dice_list[0], self.dice_list[4]
        return self.dice_list

    def move_s(self):
        self.dice_list[0], self.dice_list[1], self.dice_list[4], self.dice_list[5] = self.dice_list[4], self.dice_list[0], self.dice_list[5], self.dice_list[1]
        return self.dice_list

    def move_e(self):
        self.dice_list[0], self.dice_list[2], self.dice_list[5], self.dice_list[3] = self.dice_list[3], self.dice_list[0], self.dice_list[2], self.dice_list[5]
        return self.dice_list

    def move_w(self):
        self.dice_list[0], self.dice_list[2], self.dice_list[5], self.dice_list[3] = self.dice_list[2], self.dice_list[5], self.dice_list[3], self.dice_list[0]
        return self.dice_list
    

def dice_check(dice1, dice2):
    move_n_flag = 0            #北へ転がしたかどうかの判定
    no_flag = 0               #全てのサイコロが異なる場合
    for i in range(6):              #上面の設定を変えるためのループ
        for j in range(4):
            if dice1.dice_list == dice2.dice_list and no_flag == 0:
                no_flag = 1
                return no_flag
            dice1.move_s()
            dice1.move_e()
            dice1.move_n()

        #dice1.reset()
        #print(dice1.dice_list)

        if move_n_flag == 0:
            dice1.move_n()
            move_n_flag = 1
        else:
            dice1.move_e()
            move_n_flag = 0
    if no_flag == 0:
        return no_flag

n = int(input())
dice = []
no_flag_array = []
for i in range(n):
    dice.append(Dice(list(map(int, input().split()))))
    if i >= 1:
        no_flag_array.append(dice_check(dice[0], dice[i]))

# print(no_flag_array)

if 1 in no_flag_array:
    print("No")
else:
    print("Yes")