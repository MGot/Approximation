//
// Created by afro on 03.03.16.
//

#ifndef PROJECT_1_VERTEX_H
#define PROJECT_1_VERTEX_H

#include "edge.h"
#include <vector>

class Vertex {
    unsigned int id;
    std::vector<Edge> adjacentEdges;

public:
    Vertex(unsigned int);
    virtual ~Vertex();

    void sortAdjacentList();

    inline void addAdjacentEdge(Edge e)
    {
        adjacentEdges.push_back(e);
    }

    inline Edge getAdjecentEdge(int i)
    {
        return adjacentEdges[i];
    }

    inline unsigned long getAdjacentEdgesNumber()
    {
        return adjacentEdges.size();
    }
};


#endif //PROJECT_1_VERTEX_H
