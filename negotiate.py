#ask the input for money vs location preference
salary = int(input('Enter salary offered: '))
bonus = int(input('Enter bonus offered: '))
if salary <= 100000:
   print('Depends on location')
   local =  input('Enter location of offered job: ')
   if local != ('Colorado' or 'Denver' or 'Co' or 'Denver, Co'):
      if salary <= 110000:
          increase = input('Can you increase the offer? ')
          if increase == ('yes' or 'yea' or 'yeah' or 'Yes' or 'Yea' or 'Yeah'):
              howMuch = int(input('How much?'))
              if howMuch >= 105000:
                  print('When can I start?')
              else:
                  print('Sorry, but I pass.')
          else:
              print('Sorry, but I pass.')
      else:
          print('When can I start?')
   else:
        if salary >= 90000:
            print('When can I start?')
        else:
            print('Sorry, but I pass.')
else:
  print('When can I start?')