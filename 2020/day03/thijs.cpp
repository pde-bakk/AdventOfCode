#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

int main(void)
{
    vector<string>    map;
    while (1)
    {
        string buf;
        getline(cin, buf);
        map.push_back(buf);
        if (cin.eof())
            break ;
    }
    size_t width = map[0].size();
    size_t pos = 3;
    size_t trees[5] = {0};
    for (size_t i = 1; i < map.size(); i++)
    {
        if (map[i][i % width] == '#')
            trees[0]++;
        if (map[i][(3 * i) % width] == '#')
            trees[1]++;
        if (map[i][(5 * i) % width] == '#')
            trees[2]++;
        if (map[i][(7 * i) % width] == '#')
            trees[3]++;
        if (i * 2 < map.size() && map[(i * 2)][i % width] == '#')
            trees[4]++;
    }
    size_t sum = 1;
    for (size_t i = 0; i < 5; i++)
    {
//        dprintf(2, "trees[%ld] = %ld\n", i, trees[i]);
        sum *= trees[i];
    }
    std::cout << "sum: " << sum << std::endl;
    return (0);
}