#import libraries here

def main():
  wave=int(input("Enter the wavelength in nm: "))
  if 380<=wave<450:
      print("The relevant color is Violet")
  elif 450<=wave<495:
      print("The relevant color is Blue")
  elif 495<=wave<570:
      print("The relevant color is Green")
  elif 570<=wave<590:
      print("The relevant color is Yellow")
  elif 590<=wave<620:
      print("The relevant color is Orange")
  elif 620<=wave<=750:
      print("The relevant color is Red")
  else:
      print("Invalid input!")
  
  
  pass

if __name__ == "__main__":
  main()
