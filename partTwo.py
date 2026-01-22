import math  

def main():
    A = int(input("Enter 1st num: "))
    B = int(input("Enter 2nd num: "))
    C = pythag(A,B)
    print(C)

def pythag(A,B):
  C = math.sqrt(A ** 2 + B ** 2)
  return C

main()
