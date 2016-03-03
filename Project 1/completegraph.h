//
// Created by afro on 03.03.16.
//

#ifndef PROJECT_1_COMPLETEGRAPH_H
#define PROJECT_1_COMPLETEGRAPH_H

#include "edge.h"
#include "vertex.h"
#include <vector>

class CompleteGraph {
    unsigned int numberOfVertexes;
    std::vector<Edge> graphEdges;
    std::vector<Vertex> graphVertexes;
public:
    CompleteGraph(unsigned int);
    virtual ~CompleteGraph();

    std::vector<Vertex>* getMST();
    std::vector<Vertex>* getEulerCycle();

    void showGraph();

    inline unsigned int getNumberOfVertexes()
    {
        return numberOfVertexes;
    }
};


#endif //PROJECT_1_COMPLETEGRAPH_H
