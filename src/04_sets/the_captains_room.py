K = int(input().strip())
rooms = list(map(int, input().strip().split()))
unique_rooms = set(rooms)

print(
    (sum(unique_rooms)*K - sum(rooms))/(K-1)
)

#
# for _ in unique_rooms:
#     rooms.remove(_)
#
# print(unique_rooms.difference(set(rooms)).pop())
#
# print(
#     (sum(unique_rooms)*K - sum(rooms))/(K-1)
# )
