//
//  action_set.h
//  current
//
//  Created by Nathan Anthony on 5/30/17.
//  Copyright © 2017 Nathan Anthony. All rights reserved.
//

#ifndef action_set_h
#define action_set_h


#endif /* action_set_h */
#ifndef room_list_h
#define room_list_h
#endif
#include <string>
using namespace std;

void jump(ROOM r){
    cout << "Congrats, you jumped. Don't you feel special.\n";
}


map <string, function> action_list;
action_list["jump"] = jump();
ROOM action(ROOM r){
    cout << "What would you like to do?" << endl;
    string in;
    cin >> in;
    int act = 1;
    for(map<string, function>::iterator
        it=action_list.begin();
        it!=action_list.end();
        ++it;){};
    return r;
};

ROOM do(ROOM r){
    int act = 1;
    while(act !=0){
        
    }
    
    
};
