#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isPalindrome(int x)
{
    string pharse = to_string(x);
    vector<char> words;
    vector<char> reverse;

    for (char word : pharse)
    {
        words.push_back(word);
    }

    for (vector<char>::reverse_iterator rit = words.rbegin(); rit != words.rend(); ++rit)
    {
        reverse.push_back(*rit);
    }

    size_t size = reverse.size() - 1;

    for (size_t i = 0; i <= size; i++)
    {
        if (reverse[i] != words[i])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    cout << isPalindrome(202);

    return 0;
}
