'''
23280666446042

23280666446042

'''

# lst = list()
    # dict = {}
    # i = 0
    # for (x, y) in allLocations:
    #     dict[i] = x ** 2 + y ** 2
    #     ## lst.append(x ** 2 + y ** 2)
    #
    # print(lst)


def nearestVegetarianRestaurant0(totalRestaurants, allLocations, numRestaurants):
    # WRITE YOUR CODE HERE
    if not allLocations:
        return

    allLocations.sort(key=lambda dist: dist[0] ** 2 + dist[1] ** 2)

    return allLocations[:numRestaurants]

print(nearestVegetarianRestaurant0(3, [[1, -3],
                                [1, 2],
                                [3, 4]],
                            1))

print(nearestVegetarianRestaurant0(3, [[1, -3],
                                [1, 2],
                                [3, 4]],
                            3))

from heapq import nsmallest


def nearestVegetarianRestaurant(totalRestaurants, allLocations, numRestaurants):
    # WRITE YOUR CODE HERE
    return nsmallest(numRestaurants, allLocations, lambda dist: dist[0] ** 2 + dist[1] ** 2)

print(nearestVegetarianRestaurant(3, [[1, -3],
                                [1, 2],
                                [3, 4]],
                            1))

print(nearestVegetarianRestaurant(3, [[1, -3],
                                [1, 2],
                                [3, 4]],
                            3))