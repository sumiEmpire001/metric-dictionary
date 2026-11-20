#include "Core.h"
#include <cassert>
int main(){lord_sumi::MetricGraph<4,3> g;assert(g.add("visits"));assert(g.add("conversion"));assert(g.depend(1,0));size_t order[4]={};assert(g.order(order)&&order[0]==0&&order[1]==1);assert(g.depend(0,1));assert(!g.order(order));g.reset();assert(g.add("a"));assert(!g.add("a"));assert(g.fault());}