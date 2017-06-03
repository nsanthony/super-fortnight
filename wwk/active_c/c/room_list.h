#include <string>
#include <iostream>
using namespace std;




class ROOM {
	public:
		string name, descript, size,people;
		int occupied,seen,coord;
		void set_name(string x),set_people(string x);
		void set_descript(string x);
		
};

void ROOM::set_name(string x){
	name = x;
};

void ROOM::set_descript(string x){
	descript = x;
};

void ROOM::set_people(string x){
	people = x;
};

//jump definition
void jump(ROOM r){
	cout << "Congrats, you jumped. Don't you feel special.\n";
//	cout << r.descript << endl;
}
