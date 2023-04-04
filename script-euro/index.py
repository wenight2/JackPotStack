import random
def handler(event, context):
  thisweeksfive = []
  while thisweeksfive.count(3) == 0:
      thisweeksfive = []
      thisweekstwo = []
      num1 = random.randint(1,10)
      num2 = random.randint(11,20)
      num3 = random.randint(21,30)
      num4 = random.randint(31,40)
      num5 = random.randint(41,50)
      num6 = random.randint(1,6)
      num7 = random.randint(7,12)
      for num in (num1, num2, num3, num4, num5):
          thisweeksfive.append(num)
      for othernum in (num6, num7):
          thisweekstwo.append(othernum)
    
  else:
      hululu = str(sorted(thisweeksfive))
      hululu2 = str(sorted(thisweekstwo))
      return {'body': hululu+" & "+hululu2,
      'statusCode': 200
      }

print(handler("soemthing", "some"))
  

