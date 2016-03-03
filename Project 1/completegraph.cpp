//
// Created by afro on 03.03.16.
//

#include "completegraph.h"
#include <cstdlib>
#include <iostream>
#include <ctime>

using namespace std;


CompleteGraph::CompleteGraph(unsigned int numberOfVertexes) : numberOfVertexes(numberOfVertexes)
{
    std::srand(std::time(nullptr));
    for(auto i = 0; i < numberOfVertexes; ++i)
    {
        graphVertexes.push_back(Vertex(i));
        for(auto j = 0; j < numberOfVertexes; ++j)
        {
            if(i != j)
            {
                Edge e(i, j, rand() % 100 + 1);
                graphEdges.push_back(e); // weight is a random number from range 1 to 100
                graphVertexes[i].addAdjacentEdge(e);
            }
        }
        graphVertexes[i].sortAdjacentList();
    }
}

CompleteGraph::~CompleteGraph()
{

}

void CompleteGraph::showGraph()
{
    cout << "Vertex number\tFirst vertex id\t Second vertex id\tEdge weight" << endl;
    for(auto i = 0; i < graphVertexes.size(); ++i)
    {

        cout << "\t" << i << "\t\t\t\t\t";
        for(auto j = 0; j < graphVertexes[i].getAdjacentEdgesNumber(); ++j)
        {
            if(j != 0 )
                cout << "\t\t\t\t\t\t";
            cout << graphVertexes[i].getAdjecentEdge(j).getV1Id() << "\t\t\t\t"
            << graphVertexes[i].getAdjecentEdge(j).getV2Id() << "\t\t\t\t"
            << graphVertexes[i].getAdjecentEdge(j).getWeight() << "\t\t\t\t";
            cout << endl;
        }
        cout << endl;
    }
}

std::vector<Vertex>* CompleteGraph::getMST()
{

}

std::vector<Vertex>* CompleteGraph::getEulerCycle()
{

}