import random
def handler(event, context):
  thisweek = []
  while thisweek.count(3) == 0:
      thisweek = []
      num1 = random.randint(1,10)
      num2 = random.randint(11,20)
      num3 = random.randint(21,30)
      num4 = random.randint(31,40)
      num5 = random.randint(41,50)
      num6 = random.randint(51,60)
      num7 = random.randint(61,70)
      num8 = random.randint(71,80)
      num9 = random.randint(81,90)
      raw10 = []
      for rand in (num1, num2, num3, num4, num5, num6, num7, num8, num9):
          raw10.append(rand)
      something, something2, something3, something4, something5 = random.sample(raw10, 5)
      for num in (something, something2, something3, something4, something5):
          thisweek.append(num)                      
  else:
      hululu = str(sorted(thisweek))
      return {'body': hululu,
      'statusCode': 200
      }