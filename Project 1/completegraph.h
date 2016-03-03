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

    std::vector<Vertex>* getMST(); // finding and returning minimum spanning tree
    std::vector<Vertex>* getEulerCycle(); // finding and returning euler cycle

    void showGraph();

    inline unsigned int getNumberOfVertexes()
    {
        return numberOfVertexes;
    }

    // here should be implemented finding the perfect match
    // for know I don't have idea, what type should be returned
    // maybe some c++ pair(Vertex, Vertex) object
    void getPerfectMatching();
};


#endif //PROJECT_1_COMPLETEGRAPH_H
