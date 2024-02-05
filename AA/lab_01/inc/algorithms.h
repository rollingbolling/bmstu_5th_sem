#ifndef _ALGORITHMS_H_
#define _ALGORITHMS_H_

#include <iostream>
#include <algorithm>

using namespace std;

int LevNoRec(wstring &string1, wstring &string2, bool print=false);
int DemLevNoRec(wstring &string1, wstring &string2, bool print=false);
int DemLevNoCache(wstring &string1, wstring &string2, bool print=false);
int DemLevCache(wstring &string1, wstring &string2, bool print=false);

#endif
