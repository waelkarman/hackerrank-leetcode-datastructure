int jumpingOnCloudsRevisited(vector<int> c, int k) {
    int i=0,e=100;
    bool first=true;
    
    while(first || ((i*k)%c.size()) != 0){
        first=false;
        
        if ( c[((i*k)%c.size())] == 0){
            e--;
            i++;
        }else{
            e=e-3;
            i++;
        }
        
        if(e<0){break;}
    } 

    return e;   

}