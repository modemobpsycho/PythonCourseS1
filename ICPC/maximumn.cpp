#include <string>
#include <vector>
#include <iostream>
#include<sstream>
#include<cmath>

using namespace std;

void proizv(string s) {
    stringstream ss(s);
    vector<string> v;

    while (getline(ss, s, ' ')) {

        v.push_back(s);
    }

    char const* a = v[0].data();
    char const* b = v[1].data();
    char const* c = v[2].data();

    long double x = sqrt(atof(b) / atof(c));
    long double max = atof(a) * x / (atof(b) + atof(c) * x * x);

    cout << x << " " << max;
}

int main()
{
    std::string str = "";
    getline(cin, str);
    proizv(str);
}