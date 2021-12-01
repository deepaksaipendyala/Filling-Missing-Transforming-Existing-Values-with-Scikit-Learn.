def p1(lis):
  a1 = 0
  for i in range(len(lis)-1):
      if int(lis[i+1]) > int(lis[i]):
            a1 += 1
  return a1

def p2(lis):
  a2 = 0
  for i in range(len(lis)-3):
      if int(lis[i+3]) > int(lis[i]):
            a2 += 1
  return a2


if __name__ == '__main__':

  with open('Day_1/day1_input.txt','r') as file:
      lis = file.readlines()
      print("answer for part 1:",p1(lis))
      print("answer for part 1:",p2(lis))