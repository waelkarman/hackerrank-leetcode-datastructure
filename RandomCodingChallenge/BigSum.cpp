// CORRECT NOT OPTIMIZED

bool compare_values(string a,string b){
    if(a.length()>b.length()){
        return false;
    }
    if(a.length()<b.length()){
        return true;
    }
    
    bool ans = false;
    if(a.length() == b.length()){ 
        for(size_t i = 0; i < a.size(); i++){
            if((int)(a[i]) == (int)(b[i])){
                continue;
            }
            if((int)(a[i]) < (int)(b[i])){
                return true;
            }else{
                return false;
            }  
        }
    }
    return true;
}

void insert_in_order(vector<string> &sorted, string it){

    bool bigger=false;
    size_t i=0;
    while( i < sorted.size()){
        bigger=compare_values(sorted[i],it);
        if( ! bigger ){
            break;        
        }
        i++;
    }
    sorted.insert(sorted.begin()+i,it);        
}

vector<string> bigSorting(vector<string> unsorted) {
    vector<string> sorted;
    
    for(int i = 0; i < unsorted.size() ; i++){
        insert_in_order(sorted,unsorted[i]); 
    }
    return sorted;
}
