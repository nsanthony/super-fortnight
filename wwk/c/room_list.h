#include <string>
using namespace std;


class ROOM {
	public:
		string name, descript, size,people;
		int occupied,seen,coord;
};

extern ROOM woods;

void call_info();