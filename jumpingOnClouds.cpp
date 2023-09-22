int jumpingOnClouds(vector<int> c) {
    vector<int>::iterator it= c.begin();
    int jumps=0;
    while(it != c.end()){
        if (*(it+2) == 0){
            if((c.size() - (it-c.begin()))>2 ){
                it=it+2;
            }else{
                if((c.size() - (it-c.begin()))>1 ){
                    it++;
                }
                else{
                    break;
                }
                jumps++;
                break;
            }
            jumps++;
        }else{
            if((c.size() - (it-c.begin()))>1 ){
                it++;
            }
            else{
                break;
            }
            jumps++;
        }
    } 

    return jumps;   
}