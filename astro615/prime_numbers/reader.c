#include <stdio.h>


int main(void){
	FILE *fp = fopen("billionprimes.dat", "rb");
//	int primes[10000];
	int i = 0;
	while(!feof(fp)){
		fread(buf, 4, 1, fp); // read 4 bytes
    		int throw_away = do_some_magic_to_get_the_number(buf);
    		fseek(fp, throw_away, SEEK_CUR); // skip the given number of bytes
    		fread(buf, 1, 1, fp); // read one byte
	}


}




