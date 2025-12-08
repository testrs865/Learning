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
    yes_flag = 0               #1回だけyesを出力させるためのフラグ
    for i in range(6):              #上面の設定を変えるためのループ
        for j in range(4):
            if dice1.dice_list == dice2.dice_list and yes_flag == 0:
                print("Yes")
                yes_flag = 1
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
    if yes_flag == 0:
        print("No")

dice1 = Dice(list(map(int, input().split())))
dice2 = Dice(list(map(int, input().split())))

dice_check(dice1, dice2)