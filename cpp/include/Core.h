#pragma once
#include <cstddef>
namespace lord_sumi {
template<size_t N,size_t D> class MetricGraph {
 struct Item{const char* name;size_t deps[D];size_t count;};
 Item items_[N];size_t count_=0;bool fault_=false;
 static bool equal(const char*a,const char*b){if(!a||!b)return false;while(*a&&*b){if(*a++!=*b++)return false;}return *a==*b;}
public:
 bool add(const char* name){if(fault_)return false;if(!name||!*name||count_==N){fault_=true;return false;}for(size_t i=0;i<count_;++i)if(equal(items_[i].name,name)){fault_=true;return false;}items_[count_++]={name,{},0};return true;}
 bool depend(size_t item,size_t prerequisite){if(fault_)return false;if(item>=count_||prerequisite>=count_||items_[item].count==D){fault_=true;return false;}for(size_t i=0;i<items_[item].count;++i)if(items_[item].deps[i]==prerequisite){fault_=true;return false;}items_[item].deps[items_[item].count++]=prerequisite;return true;}
 bool order(size_t out[N])const{if(fault_)return false;bool placed[N]={};for(size_t k=0;k<count_;++k){bool found=false;for(size_t i=0;i<count_;++i){if(placed[i])continue;bool ready=true;for(size_t j=0;j<items_[i].count;++j)if(!placed[items_[i].deps[j]])ready=false;if(ready){placed[i]=true;out[k]=i;found=true;break;}}if(!found)return false;}return true;}
 size_t size()const{return count_;}bool fault()const{return fault_;}void reset(){count_=0;fault_=false;}
};
}