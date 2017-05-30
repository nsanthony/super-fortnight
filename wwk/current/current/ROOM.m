//
//  ROOM.m
//  current
//
//  Created by Nathan Anthony on 5/30/17.
//  Copyright © 2017 Nathan Anthony. All rights reserved.
//

#import "ROOM.h"

@implementation ROOM
ROOM {
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
@end
