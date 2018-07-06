//
//  main.c
//  chap1
//
//  Created by Henry Spivey on 5/7/18.
//  Copyright © 2018 Henry Spivey. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    printf("Hello, World!\n");
    
    float fahr, celsius;
    int lower, upper, step;
    lower = 0;
    upper = 300;
    step = 20;
    
    fahr = lower;
    printf("Fahrenheit Celsius \n");
    while (fahr <= upper) {
//        celsius = 5 * (fahr - 32) / 9;
        celsius = (5.0/9.0) * (fahr - 32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
    
    celsius = lower;
    fahr = lower;
    printf("Celsius Fahrenheit \n");
    while (celsius <= upper) {
        //        celsius = 5 * (fahr - 32) / 9;
        fahr = (9.0/5.0 * celsius ) +  32.0;
        printf("%3.0f %6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
    return 0;
}
