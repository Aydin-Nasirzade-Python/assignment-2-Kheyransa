#import libraries here

def main():
  month=input("Enter name of the month [ex. June]: ")
  day=int(input("Enter the day [ex. 5]: "))
  if (month=="March" and day>=20) or (month=="April" and 0<day<=30) or (month=="May" and 0<day<=31) or (month=="June" and 0<day<21):
      print(f'{month} {day} is in Spring')
  elif (month=="September" and day>=22) or (month=="October" and 0<day<=31) or (month=="November" and 0<day<=31) or(month=="December" and 0<day<=20):
      print(f'{month} {day} is in Fall')
  elif (month=="June" and 21<=day<=30) or (month=="July" and 0<day<=31) or (month=="August" and 0<day<31) or (month=="September" and 0<day<22):
      print(f"{month} {day} is in Summer")
  elif (month=="December" and 20<day<=31) or (month=="January" and 0<day<=31) or (month=="February" and 0<day<31) or (month=="March" and 0<day<20):
      print(f"{month} {day} is in Winter")
    
  pass

if __name__ == "__main__":
  main()
