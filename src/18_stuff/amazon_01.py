def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    # n = 8
    for day in range(days):
        tmp_states = [0, 0, 0, 0, 0, 0, 0, 0]
        print("states 1", states)
        for i in range(len(states)):
            if i == 0:
                if states[i+1] == 0:
                    tmp_states[i] = 0
                else:
                    tmp_states[i] = 1

            elif i == 7:
                if states[i-1] == 0:
                    tmp_states[i] = 0
                else:
                    tmp_states[i] = 1

            else:
                if states[i-1] == states[i+1]:
                    tmp_states[i] = 0
                else:
                    tmp_states[i] = 1

        states = tmp_states
        print("states 2", states)


    return states


# if __name__ == '__main()__':
# inp = input()
#
# inp2 = list(map(int, inp.replace("[", " ").replace("]", " ").replace(",", " ").strip().split()))
#
# houses = inp2[:8]
# k = inp2[-1]
# print(inp2)
# print(houses)
# print(k)

t1 = [1, 0, 0, 0, 0, 1, 0, 0]
k1 = 1

t2 = [1, 0, 0, 0, 0, 1, 0, 0]
k2 = 2

t3 = [0, 1, 0, 0, 1, 0, 1, 0]
k3 = 1

# print(cellCompete(t1, k1))
print(cellCompete(t2, k2))
# print(cellCompete(t3, k3))




# print(houses)
# print(k)
'''
[1, 0, 0, 0, 0, 1, 0, 0], 1

[1, 1, 1, 0, 1, 1, 1, 1], 2
'''
