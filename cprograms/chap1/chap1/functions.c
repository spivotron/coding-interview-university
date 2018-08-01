//
//  functions.c
//  chap1
//
//  Created by Henry Spivey on 11/7/18.
//  Copyright © 2018 Henry Spivey. All rights reserved.
//

#include <stdio.h>

int power(int m, int n);
void convertMe(float);
void lineCounter(void);
void i2o(void);
void i2o_v2(void);

int main() {
//    int i;
//    for (i = 0; i< 10; ++i) {
//        printf("%d %d %d\n", i, power(2,i), power(-3, i));
//    }
//    convertMe(-10.0);
//    lineCounter();
//    i2o();
    i2o_v2();
    return 0;
}

int power(int base, int n) {
    int i, p;
    p = 1;
    for (i = 1; i <= n; ++i) {
        p = p * base;
    }
    return p;
}

// power function with call by value
int power2(int base, int n) {
    int p;
    for (p=1; n>0; --n) {
        p *= base;
    }
    return p;
}

// line counting
void lineCounter() {
    int c2, nl, nt;
    nl = nt = 0;
    while( (c2 = getchar()) != EOF ) {
        if(c2== '\n') {
            ++nl;
        }
        else if (c2 == '\t') {
            ++nt;
        }
    }
    printf("%d\n", nl);
    printf("%d\n", nt);
}

//Exercise 1-9. Write a program to copy its input to its output, replacing each string of one or more blanks by a single blank
void i2o() {
    int c;
    while ( (c = getchar()) != EOF) {
        if ( c == ' ') {
            while( (c = getchar()) == ' ' );
            putchar(' ');
        }
        putchar(c);
    }
}

void i2o_v2() {
    int c;
    while( (c =getchar()) != EOF ) {
        if(c == '\t') {
            while ( (c=getchar()) == '\t' );
            putchar('\t');
        }
        else if(c == '\b') {
            while ( (c=getchar()) == '\b' );
            putchar('\b');
        }
        else if (c  == '\\') {
            while ( (c=getchar()) == '\\' );
            putchar('\\');
        }
        putchar(c);
    }
}


void convertMe(float c) {
    printf("Enter numbers in Celsius to convert to Fahrenheit. Enter STOP to end program \n");
    float f = (9.0/5.0 *c) + 32;
    printf("%.1f Celsius in Fahrenheit is %.1f \n", c, f);
}
