//guessing_game.cpp By: Caroline Gorham
// Description: play game with user, compare random number with cin

#include <iostream>
#include <cstdlib>
#include <time.h>
#undef  RAND_MAX 
#undef RAND_MIN
#define RAND_MAX 100
#define RAND_MIN 1
using namespace std;

int main (){
int kRandom;
int kUserNumber;
char play_again;
// initialize random seed.
srand(time(NULL));

//Generate random number between 1 and 100:: not the best, favoring numbers that have already been picked..


kRandom= rand() % RAND_MAX + RAND_MIN;

//cout << "Your random number:" << kRandom << endl;

do{
cout << "Guess our number ("<<RAND_MIN<< " to " <<RAND_MAX <<"), -1 to exit: " ;

if (!(cin>>kUserNumber)) {
cout<< "Please enter numbers only." << endl;
  cin.clear();
  cin.ignore(10000,'\n');}
 else if (kUserNumber != -1) {

if (kUserNumber < kRandom) cout << "The secret number is higher than " << kUserNumber << endl;

else if (kUserNumber > kRandom) cout << "The secret number is lower than " << kUserNumber << endl;

else  cout << "You guessed it! random number is: " << kRandom <<endl; }

} while (kUserNumber != -1);
cout << "You entered -1 to exit.";

return 0;
}
