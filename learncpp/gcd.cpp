// gcd.cpp By: Caroline Gorham
//computes the gcd for two integers

#include <iostream>

int gcd (int a, int b){
  int temp;
  while (b!=0){
  temp = a % b;
  a = b;
  b = temp; }
return(a);
}

int main () {
int x, y;

std::cout << "Enter two integers: " ;
if (!(std::cin>>x>>y)) {
  std::cout << "Please enter only integers" << std::endl ;}
  else {std::cout <<"gcd("<< x << ", " << y << ") = " << gcd(x,y) << std::endl ;}

return 0;
}
