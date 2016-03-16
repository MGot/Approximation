#include <iostream>
#include "completegraph.h"

using namespace std;

int main() {
    cout << "Complete graphs simulator" << endl;

    CompleteGraph graph(5);

    graph.showGraph();
    graph.findMST();

    vector<Vertex*> mst = graph.getMST();

    cout << "=================MST=================" << endl;
    for(auto i = 0; i<mst.size(); ++i)
    {
        cout << mst[i]->getId() << "    ";
    }

    cout << endl;
    cout << "=================END=================" << endl;
    return 0;
}