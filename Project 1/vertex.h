//
// Created by afro on 03.03.16.
//

#ifndef PROJECT_1_VERTEX_H
#define PROJECT_1_VERTEX_H

#include "edge.h"
#include <vector>

class Vertex {
    unsigned int id;
    std::vector<Edge> adjecentEdges;

public:
    Vertex(unsigned int);
    virtual ~Vertex();

    inline void addAdjecentEdge(Edge e)
    {
        adjecentEdges.push_back(e);
    }

    inline Edge getAdjecentEdge(int i)
    {
        return adjecentEdges[i];
    }

    inline unsigned long getAdjecentEdgesNumber()
    {
        return adjecentEdges.size();
    }
};


#endif //PROJECT_1_VERTEX_H
