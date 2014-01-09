// math_ex2.cpp How many ways can you arrange 6 different books, left to right, on a shelf? By: Caroline Gorham
#include <iostream>

int factorial(int);

int main () {
  int number;
  
  std::cout << "Please enter a positive integer of books: " ;
  std::cin >> number;
  if (number < 0)
     std::cout << "Please enter a positive integer.\n";
  else
    std::cout << "The books can be placed in " << factorial(number) << " ways from left to right." ;

return 0;
}

int factorial(int number){
int temp;

  if(number <=1) return 1;
  temp = number * factorial(number-1) ;
  return temp;
}

