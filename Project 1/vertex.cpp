//
// Created by afro on 03.03.16.
//

#include "vertex.h"
#include <algorithm>

Vertex::Vertex(unsigned int id) : id(id)
{

}

Vertex::~Vertex()
{

}

struct {
    bool operator()(Edge a, Edge b)
    {
        return a.getWeight() < b.getWeight();
    }
} comparisonFunction;

void Vertex::sortAdjacentList()
{
    std::sort(adjecentEdges.begin(),adjecentEdges.end(), comparisonFunction);
}