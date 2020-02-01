#include <bits/stdc++.h>
#include <fstream>
#include <string>
using namespace std;
vector<int> encoding(string s1)
{
    cout << "Encoding\n";
    unordered_map<string, int> table;
    for (int i = 0; i <= 255; i++)
    {
        string ch = "";
        ch += char(i);
        table[ch] = i;
    }

    string p = "", c = "";
    p += s1[0];
    int code = 256;
    vector<int> output_code;
    cout << "String\tOutput_Code\tAddition\n";
    for (int i = 0; i < s1.length(); i++)
    {
        if (i != s1.length() - 1)
            c += s1[i + 1];
        if (table.find(p + c) != table.end())
        {
            p = p + c;
        }
        else
        {
            cout << p << "\t" << table[p] << "\t\t"
                 << p + c << "\t" << code << endl;
            output_code.push_back(table[p]);
            table[p + c] = code;
            code++;
            p = c;
        }
        c = "";
    }
    cout << p << "\t" << table[p] << endl;
    output_code.push_back(table[p]);
    return output_code;
}

// void decoding(vector<int> op)
// {
//     cout << "\nDecoding\n";
//     unordered_map<int, string> table;
//     for (int i = 0; i <= 255; i++) {
//         string ch = "";
//         ch += char(i);
//         table[i] = ch;
//     }
//     int old = op[0], n;
//     string s = table[old];
//     string c = "";
//     c += s[0];
//     cout << s;
//     int count = 256;
//     for (int i = 0; i < op.size() - 1; i++) {
//         n = op[i + 1];
//         if (table.find(n) == table.end()) {
//             s = table[old];
//             s = s + c;
//         }
//         else {
//             s = table[n];
//         }
//         cout << s;
//         c = "";
//         c += s[0];
//         table[count] = table[old] + c;
//         count++;
//         old = n;
//     }
// }
int main()
{

    // string s = "WYS*WYGWYS*WYSWYSG";
    ifstream fin;
    fin.open("text.txt");
    string p = "";
    while (fin)
    {
        string line;
        getline(fin, line);
        p += line;
    }
    fin.close();

    vector<int> output_code = encoding(p);
    // cout << "Output Codes are: ";
    // for (int i = 0; i < output_code.size(); i++) {
    //     cout << output_code[i] << " ";
    // }

    ofstream fout;
    fout.open("lzwEnc.txt");
    for (int i = 0; i < output_code.size(); i++)
    {
        fout << (output_code[i]);
        fout << " ";
    }
    cout << "success";
    cout << endl;
    // decoding(output_code);
}
