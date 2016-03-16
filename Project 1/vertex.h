//
// Created by afro on 03.03.16.
//

#ifndef PROJECT_1_VERTEX_H
#define PROJECT_1_VERTEX_H

#include "edge.h"
#include <vector>

class Vertex {

public:
    Vertex(unsigned int);
    virtual ~Vertex();

    void sortAdjacentLists();

    inline void addAdjacentEdge(Edge e)
    {
        adjacentEdges.push_back(e);
    }

    inline Edge getAdjecentEdge(int i) const
    {
        return adjacentEdges[i];
    }

    inline unsigned long getAdjacentEdgesNumber() const
    {
        return adjacentEdges.size();
    }

    inline unsigned int getId() const
    {
        return id;
    }

    inline bool getStatus() const
    {
        return visited;
    }

    inline bool setStatus(bool status) {
        visited = status;
    }


private:
    unsigned int id;
    bool visited;
    std::vector<Edge> adjacentEdges;
    std::vector<Vertex> adjacentVertices;
};


#endif //PROJECT_1_VERTEX_H
