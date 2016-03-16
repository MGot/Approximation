//
// Created by afro on 03.03.16.
//

#include "completegraph.h"
#include <cstdlib>
#include <iostream>
#include <ctime>
#include <bits/stl_algo.h>
#include <queue>

using namespace std;


CompleteGraph::CompleteGraph(unsigned int numberOfVertexes) : numberOfVertexes(numberOfVertexes)
{
    std::srand(std::time(nullptr));
    for(auto i = 0; i < numberOfVertexes; ++i)
    {
        graphVertices.push_back(Vertex(i));
        for(auto j = 0; j < numberOfVertexes; ++j)
        {
            if(i != j)
            {
                Edge e(i, j, rand() % 100 + 1);
                graphEdges.push_back(e); // weight is a random number from range 1 to 100
                graphVertices[i].addAdjacentEdge(e);
            }
        }
        graphVertices[i].sortAdjacentLists();
    }
}

CompleteGraph::~CompleteGraph()
{

}

void CompleteGraph::showGraph()
{
    cout << "Vertex number\tFirst vertex id\t Second vertex id\tEdge weight" << endl;
    for(auto i = 0; i < graphVertices.size(); ++i)
    {

        cout << "\t" << i << "\t\t\t\t\t";
        for(auto j = 0; j < graphVertices[i].getAdjacentEdgesNumber(); ++j)
        {
            if(j != 0 )
                cout << "\t\t\t\t\t\t";
            cout << graphVertices[i].getAdjecentEdge(j).getV1Id() << "\t\t\t\t"
            << graphVertices[i].getAdjecentEdge(j).getV2Id() << "\t\t\t\t"
            << graphVertices[i].getAdjecentEdge(j).getWeight() << "\t\t\t\t";
            cout << endl;
        }
        cout << endl;
    }
}

void CompleteGraph::findMST()
{
    class PriorityQueueCMP
    {
    public:
        bool operator() (Vertex* a, Vertex* b)
        {
            return a->getAdjecentEdge(0).getWeight() > b->getAdjecentEdge(0).getWeight();
        }
    };
    priority_queue<Vertex*, std::vector<Vertex*>, PriorityQueueCMP> pQueue;
    std::vector<Vertex*> mstVect;
    std::vector<Vertex*> vertexNeighbors;

     // pushing first node into the priority queue
    vertexNeighbors = getVertexNeighbors(graphVertices[0]);
    mstVect.push_back(&graphVertices[0]);

/*    for(auto i = 0; i<vertexNeighbors.size(); ++i)
    {
        cout << vertexNeighbors[i]->getId() << "    ";
    }*/

    for(auto i = 0; i < vertexNeighbors.size(); ++i)
    {
        pQueue.push(vertexNeighbors[i]);
    }
/*
    int size = pQueue.size();
    cout << endl;
    for(auto i = 0; i<size; ++i)
    {
        cout << pQueue.top()->getId() << "   ";
        pQueue.pop();
    }
*/

    while(mstVect.size() != graphVertices.size())
    {
        Vertex* tmp = pQueue.top();
        pQueue.pop();
        if(tmp->getStatus() == false) {
            tmp->setStatus(true);
            mstVect.push_back(tmp);
            vertexNeighbors = getVertexNeighbors(*tmp);
            /*for (auto i = 0; i < vertexNeighbors.size(); ++i) {
                pQueue.push(vertexNeighbors[i]);
            }*/

            /*int size = pQueue.size();
            cout << endl;
            for (auto i = 0; i < size; ++i) {
                cout << pQueue.top()->getId() << "   ";
                pQueue.pop();
            }*/
        }
        //cout << "MST" << endl;
       /* for(auto i = 0; i<mstVect.size(); ++i)
        {
            cout << mstVect[i]->getId() << "   ";
        }
        cout << endl;*/
    }
    /*for(auto i = 0; i < mstVect.size(); ++i)
    {
        cout << mstVect[i]->getId() << "    ";
    }
    cout << endl ;*/

    mst = mstVect;
}

vector<Vertex *> CompleteGraph::getVertexNeighbors(Vertex v)
{
    std::vector<Vertex*> result;
    for(auto i = 0; i < v.getAdjacentEdgesNumber(); ++i)
    {
        if(v.getAdjecentEdge(i).getV1Id() == v.getId()) {
            result.push_back(findVertex(v.getAdjecentEdge(i).getV2Id()));
        }
        else
        {
            result.push_back(findVertex(v.getAdjecentEdge(i).getV1Id()));
        }
    }

    return result;
}

Vertex* CompleteGraph::findVertex(int id)
{
    for(auto i = 0; i<graphVertices.size(); ++i)
    {
        if(graphVertices[i].getId() == id) {
            return &graphVertices[i];
        }
    }
}

std::vector<Vertex>* CompleteGraph::getEulerCycle()
{

}