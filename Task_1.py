#import libraries here

def main():
  a=input("Enter a letter of the alphabet: ")
  if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
      print("Entered alphabet is a consonant!")
  elif a=="y":
      print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else:
      print("Entered alphabet is a vowel!")
  pass

if __name__ == "__main__":
  main()
