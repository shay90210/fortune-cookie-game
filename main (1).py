import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,4)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'You will have a great day!'
if fortune_number == 2:
  fortune_text = 'The rain will calm the storm - be patient.'
if fortune_number == 3:
  fortune_text = 'Have faith - things will get better.'
if fortune_number == 4:
  fortune_text = 'You will get married this year!'

print(f"{fortune_text} Your lucky Number is: {lucky_number}")