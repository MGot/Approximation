//
// Created by afro on 03.03.16.
//

#ifndef PROJECT_1_EDGE_H
#define PROJECT_1_EDGE_H


class Edge {
    unsigned int v1Id;
    unsigned int v2Id;
    unsigned int weight;
public:

    Edge(unsigned int, unsigned int, unsigned int);
    virtual ~Edge();

    inline unsigned int getV1Id()
    {
        return v1Id;
    }

    inline unsigned int getV2Id()
    {
        return v2Id;
    }

    inline unsigned int getWeight()
    {
        return weight;
    }
};


#endif //PROJECT_1_EDGE_H
