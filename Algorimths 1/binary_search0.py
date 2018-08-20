#python3

def run():
  print('Think of a whole positive number')
  min = 1 
  max = int(input('Your number is between 1 and? : '))
  number = int((max+min)/2)
  p_number = None
  def edit(_min,_max):
    number = int((_max+_min)/2)
    return number
  count = 1
  while True:
    if p_number != number:
      find= input('{count}. your number is {number} , "1"=Yes / "0"=Not : '.format(count=str(count),number = str(number)))
      count+=1
      if find == '0':
        find = input(r'Your number is: "<" o ">" ==> ')
        if find == '>':
          min=number+1
        elif find == '<':
          max = number-1
        else: 
          print('we cannot understood your input :(')
        p_number = number
        number = edit(min,max)
      elif find == '1':
        print('Your Number Is: '+str(number))
        return False
      else:
        print('we cannot understood your input :(')
  else:
    print('we cannot find your number :(')
    return False

run()
