def main():
  

  Double = 2.3
  

  intValue = 2
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(intValue + Double)
  print(Double *intValue)
  print(Double / intValue)
  print(intValue - Double)

  
  #populate this list
  myFriends = ["Rob","Mitch","Ben","Marty"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[1])
  print(myFriends[2])

  
  #populate this list with five numbers
  fiveNumbers = [1,2,3,4,5]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0]+fiveNumbers[1])
  print(fiveNumbers[2]-fiveNumbers[3])
  print(fiveNumbers[4]*fiveNumbers[0])
  print(fiveNumbers[2]/fiveNumbers[1])
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[1]=3
  #print out the list
  print(fiveNumbers)
  
main()
