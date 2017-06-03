#include "room_list.h"
#include <iostream>
#include <map>
using namespace std;

 map <string, fuction> action_list;
 action_list["jump"] = jump();
 void action(ROOM r){
 	cout << "What would you like to do?" << endl;
 	string in;
 	cin >> in;
 	int act = 1;
 	for(map<string, function>::iterator 
 		it=action_list.begin(); 
 		it!=action_list.end();
 		++it;){};
 };



