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
    
    // using the for statement
    
    for (int fahr = 0; fahr <= 300; fahr = fahr + 20) {
        printf("%3d %6.1f \n", fahr, (5.0/9.0)* (fahr - 32));
    }
    
    // file copying
    int c;
//    c = getchar();
//    while(c != EOF) {
//        putchar(c);
//        c = getchar();
//    }
    
    // copying input v2
    while ( (c = getchar()) != EOF) {
        putchar(c);
    }
    
    // char counting with while
    long nc;
    nc = 0;
    while ( (getchar() != EOF) ) {
        ++nc;
    printf("%1d\n", nc);
    }
    // char counting with for
    // handling bigger numbers with double
    double nc2;
    for (nc2 = 0; getchar()  != EOF; ++nc2) {
        ;
    printf("%.0f", nc2);// 0 suppresses the decimal
    }
    
    // line counting
    int c, n1;
    n1 = 0;
    while ( (c = getchar()) != EOF ) {
        if(c == '\n') {
            ++n1;
        }
    printf("%d\n", n1);
    }
    
    
    // word counting
    #define IN 1
    #define OUT 0
    int c3, nlines, nwords, numchars, state;
    state = OUT;
    nlines = nwords = numchars = 0;
    while ( (c = getchar()) != EOF ) {
        ++nc;
        if (c == '\n') {
            ++nlines;
        }
        if (c == ' ' || c == '\n' || c == '\t') {
            state = OUT;
        }
        else if (state == OUT) {
            state = IN;
            ++nwords;
        }
    }
    printf("%d %d %d\n", nlines, nwords, numchars);
    
    
    
    
    
    
    
    
    
    
    
    return 0;
}
