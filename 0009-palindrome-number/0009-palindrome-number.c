#include <stdbool.h>

bool isPalindrome(int x) {
    // Rule 1: Negative numbers matrum 0-il mudiyum numbers (except 0) palindrome illai
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    int original = x;
    long reversed = 0; // Overflow-ai thavirkka 'long' use seigirom

    // Number-ai reverse seiyum loop
    while (x > 0) {
        int remainder = x % 10;          // Kadaisi digit-ai edukka
        reversed = (reversed * 10) + remainder; // Reverse number-ai uruvakka
        x = x / 10;                      // Kadaisi digit-ai neekka
    }

    // Original number-um reverse number-um samama endru check seigirom
    return original == reversed;
}
