### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #syntax error, should be ==
      return True
    else #else needs a colon afterwards
      return False
   

  dif highest_card(self, card1 card2): #needs a comma between card1 and card2
  if card1.value > card2.value: #no indent here (all lines below will need indented also)
    return card # card is undefined should be card1
  else:
    return card2
  


def cards_total(self, cards): #line should be indented
  total #total should be = 0 to start with
  for card in cards:
    total += card.value
    return "You have a total of" + total #total should be str(total) and there should be a space after 'of' in string 
  
```
