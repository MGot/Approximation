//
// Created by afro on 03.03.16.
//

#include "vertex.h"
#include <algorithm>

Vertex::Vertex(unsigned int id) : id(id), visited(false)
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
} cmpEdges;


void Vertex::sortAdjacentLists()
{
    std::sort(adjacentEdges.begin(),adjacentEdges.end(), cmpEdges);
}