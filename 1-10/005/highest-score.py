scores = input("Input a list of student scores ").split()
for n in range(0, len(scores)):
  scores[n] = int(scores[n])


max = 0
for s in scores:
  if s > max:
    max = s
    
print (f'The highest score in the class is {max}')
