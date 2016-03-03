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

// comparing function for std::sort
struct {
    bool operator()(Edge a, Edge b)
    {
        return a.getWeight() < b.getWeight();
    }
} comparisonFunction;

void Vertex::sortAdjacentList()
{
    std::sort(adjacentEdges.begin(),adjacentEdges.end(), comparisonFunction);
}