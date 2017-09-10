CC = gcc
CFLAGS = -O2

primes: primes.o
	$(CC) $(CFLAGS) -o primes primes.o

primes.o: Makefile

clean:
	-rm -f primes.o
