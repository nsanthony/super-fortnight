//
//  main.cpp
//  current
//
//  Created by Nathan Anthony on 5/30/17.
//  Copyright © 2017 Nathan Anthony. All rights reserved.
//
#include "room_list.h"
//#ifndef action_set_h
//#define aciton_set_H
//#endif
#include "action_set.h"
#include <iostream>
#include <string>
using namespace std;

ROOM woods;


int main() {
    // 	declares the attributes of all the rooms
    woods.set_name("woods");
    woods.set_descript("You are alone in the woods");
    woods.set_people("Out of the corner of your eye you spot it *whisper* Shia LaBeouf");
    
    cout << woods.name << endl;
    cout << woods.descript << endl;
    cout << woods.people << endl;
    jump(woods);
}

