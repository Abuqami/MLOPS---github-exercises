

'''
As a gift store owner, My task here is to find the costs of
giving away the people their wishlist which are under 25$.
'''

import time
import numpy as np


def calculate_cost():
    '''
    attrs:

    returns:
    '''
    # The following line opens the gift_costs file and converts it into a list
    with open('gift_costs.txt', encoding='UTF-8') as file:
        gift_costs = file.read().split('\n')
    # The following variable is converting the costs.txt into an array
    gift_costs = np.array(gift_costs).astype(int)  # convert string to int
    # The following variable applies a formula to calculate the costs in terms
    # of assigned taxes
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

    return total_price


gifts_costs = calculate_cost()

if __name__ == "__main__":
    start = time.time()
    print('My offer costs is : ', gifts_costs, start, '\n')
