#include <string>
#include <vector>
#include <iostream>
#include<sstream>
#include<cmath>

using namespace std;

void moneti(string s) {
    std::stringstream ss(s);
    std::vector<std::string> v;

    while (getline(ss, s, ' ')) {

        v.push_back(s);
    }
    int med = stoi(v[2]) / ((stoi(v[0]) * stoi(v[1])) + stoi(v[1]) + 1);

    cout << med * stoi(v[1]) * stoi(v[0]) << " " << med * stoi(v[1]) << " " << med << endl;
}

int main()
{
    std::string str = "";
    getline(cin, str);
    moneti(str);
}