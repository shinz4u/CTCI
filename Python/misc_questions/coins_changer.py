def num_coins(total_cents):
    """
    Returns the number of coins given a change
    coins types : 25,10,5,1
    :return:
    """
    # coins = {"Quarter": 25, "dime": 10, "nickel": 5, "pennies": 1}
    returnable_coin = {25: 0, 10: 0, 5: 0, 1: 0}
    coins_to_return = {}
    for i in returnable_coin.keys():
        to_add = total_cents // i
        total_cents %= i
        coins_to_return[i] = to_add
    return coins_to_return

dict_coins = num_coins(100)
total_number_of_coins = 0
for key, val in dict_coins.items():
    total_number_of_coins += val
    print("Number of ", key, " coins is ", val)
print(total_number_of_coins)

def min_coins():
    """


    :return:
    """

class CashRegistry:

    def __init__(self, num_quarter, num_nickel, num_dime, num_penny):
        self.num_quarter = num_quarter
        self.num_nickel = num_nickel
        self.num_dime = num_dime
        self.num_penny = num_penny

    def give_change(self, change_amount):
        # different ways I can get to 31 using [25,10,5 and 1]
        # 31 = 1 * 31
        # 31 =
        # Permutations in coins
        returnable_coin = {25: 0, 10: 0, 5: 0, 1: 0}
        coins_to_return = {}
        for i in returnable_coin.keys():
            to_add = total_cents // i
            total_cents %= i
            coins_to_return[i] = to_add
        return coins_to_return

        pass


register = CashRegistry(5,5,5,5)



# What is there is not enough coins?
# OH NOMINI
# if no 5 and returning 32
# 25-1,  1-7 - tot - 8
# 10-3, 1-2 - tot - 5
#

