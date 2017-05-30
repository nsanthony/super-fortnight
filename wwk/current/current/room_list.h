//
//  room_list.h
//  current
//
//  Created by Nathan Anthony on 5/30/17.
//  Copyright © 2017 Nathan Anthony. All rights reserved.
//

#ifndef room_list_h
#define room_list_h


#endif /* room_list_h */
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

