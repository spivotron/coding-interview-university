//
//  main.c
//  chap2
//
//  Created by Henry Spivey on 16/7/18.
//  Copyright © 2018 Henry Spivey. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
int _htoi(char s[]);
enum hex {A = 10, B, C, D, E, F};
int main(int argc, const char * argv[]) {
  
    
    _htoi("c5f990d0");
    
    return 0;
}

/* defining strlen(s) */
int strlen2(char s[]) {
    int i;
    i = 0;
    while(s[i] != '\0')
        ++i;
    return i;
}


// convert s to an integer
int _atoi (char s[]) {
    int i, n;
    n = 0;
    for (i =0; s[i] >= '0' && s[i] <= '9'; ++i) {
        n = 10*n + (s[i] - '0');
    }
    return n;
}


int _htoi(char s[]) {
    int num;
    
    sscanf(s, "%x", &num);
    // &num gets the address of num
    printf("0x%x %i\n", num, num);
    return num;
}


