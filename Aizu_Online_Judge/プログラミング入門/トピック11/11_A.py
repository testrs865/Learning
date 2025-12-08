class Dice:
    def __init__(self, dice_list):
        self.dice_list = dice_list

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

lst = list(map(int, input().split()))
dice1 = Dice(lst)
command = list(input())
command_len = len(command)

for i in range(command_len):
    if command[i] == "N":
        dice1.move_n()
        #print(dice1.dice_list)
    elif command[i] == "S":
        dice1.move_s()
        #print(dice1.dice_list)
    elif command[i] == "E":
        dice1.move_e()
        #print(dice1.dice_list)
    else:
        dice1.move_w()
        #print(dice1.dice_list)

print(dice1.dice_list[0])