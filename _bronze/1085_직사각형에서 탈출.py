x,y,w,h=map(int, input().split())
temp=[x,y]
temp.append(w-x)
temp.append(h-y)
print(min(temp))