lucky_numbers=[4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]

#friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(2, "Kelly")
friends.remove("Jim")
#friends.clear()
friends.pop()
friends.index("Oscar")
friends.count("Oscar")
friends.sort()
friends.reverse()

friends2=friends.copy()

print(friends)