#include <stdio.h>
#include <math.h>

int prime_devisors(int *primes, int number2check, int prime_number_count);

int main(){
	int number_of_primes = 10000; //number of primes to be generated
	int primes[number_of_primes]; //creates the array that the primes are stored in
	int prime_number_count = 0; //number of primes found
	int i,j,k,devisable;
	
	
	for (i = 2; prime_number_count < number_of_primes; ++i) {
	//this checks to see if the current number is devisable by a prime. 
	//all non primes have a prime factorization so. If it isn't then it is prime.
		int devisable = 1;
		int k = 0;
		while (k < prime_number_count){
			if (i % primes[k] == 0){
				devisable = 0;
				break;
			}
			else {
				++k;
			}
		}
		if (devisable != 0){
			primes[prime_number_count] = i;
			prime_number_count++;
			printf("%i\n",i);
		}
	}
// 	printf("%i\n",primes[number_of_primes-1]);
	return 0;
}


