/*
Write a program that outputs the string representation of numbers from 1 to n, however:

If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.

Suppose you are given the following code:

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
Implement a multithreaded version of FizzBuzz with four threads. The same instance of FizzBuzz will be passed to four different threads:

Thread A will call fizz() to check for divisibility of 3 and outputs fizz.
Thread B will call buzz() to check for divisibility of 5 and outputs buzz.
Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and outputs fizzbuzz.
Thread D will call number() which should only output the numbers.
*/


#include <semaphore.h>

using namespace std;
class FizzBuzz {
protected:
    sem_t numberLock;
    sem_t fizzLock;
    sem_t buzzLock;
    sem_t fizzbuzzLock;

private:
    int n;

public:
    FizzBuzz(int n) {
        this->n = n;
        sem_init(&fizzLock, 0, 0);
        sem_init(&buzzLock, 0, 0);
        sem_init(&fizzbuzzLock, 0, 0);
        sem_init(&numberLock, 0, 1);

    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        for(int i = 1; i <= this->n; i ++){
            if (i % 3 == 0 && i % 5 != 0){
                sem_wait(&fizzLock);
                printFizz();
                sem_post(&numberLock);
            }
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        for(int i = 1; i <= this->n; i ++){
            if (i % 5 == 0 && i % 3 != 0){
                sem_wait(&buzzLock);
                printBuzz();
                sem_post(&numberLock);
            }
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        for(int i = 1; i <= this->n; i ++){
            if (i % 15 == 0){
                sem_wait(&fizzbuzzLock);
                printFizzBuzz();
                sem_post(&numberLock);
            }
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        for (int i = 1; i <= this->n; i ++) {
            sem_wait(&numberLock);
            if( i % 15 == 0) {
                sem_post(&fizzbuzzLock);
            }
            else if (i % 3 == 0) {
                sem_post(&fizzLock);
            }
            else if (i % 5 == 0) {
                sem_post(&buzzLock);
            }
            else {
                printNumber(i);
                sem_post(&numberLock);
            }
        }
        sem_post(&fizzbuzzLock);
        sem_post(&fizzLock);
        sem_post(&buzzLock);
    }
};