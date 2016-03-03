#include <iostream>
#include "completegraph.h"

using namespace std;

int main() {
    cout << "Complete graphs simulator" << endl;

    CompleteGraph graph(5);

    graph.showGraph();



    cout << "=================END=================" << endl;
    return 0;
}