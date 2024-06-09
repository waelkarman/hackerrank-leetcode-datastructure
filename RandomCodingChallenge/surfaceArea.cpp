int surfaceArea(vector<vector<int>> A) {
    
    int surface = 0;
    
    for(int i = 0; i<A.size(); i++){
        for(int j = 0; j<A[0].size(); j++){
            if(A[i][j] != 0){
                surface++;
            }
        }
    }
    surface += surface;
    
    //cout << "A:" << surface;
    
    for(int i = 0; i<A.size(); i++){
        for(int j = 0; j<A[0].size(); j++){
            if(i == 0 || j == 0 || i == A.size()-1 || j == A[0].size()-1 ){
                if((i+1)>(A.size()-1))
                    surface += A[i][j];
                if((i-1)<0)
                    surface += A[i][j];
                if((j+1)>(A[0].size()-1))
                    surface += A[i][j];
                if((j-1)<0)
                    surface += A[i][j];     
            }
        }   
    }
    
    //cout << "B:" << surface;
    
    for(int i = 0; i<A.size(); i++){
        for(int j = 0; j<A[0].size(); j++){
            if((i+1)<=(A.size()-1)){
                if(A[i][j]-A[i+1][j]>0){
                    surface += A[i][j]-A[i+1][j];
                }
            }
            if((i-1)>=0){
                if(A[i][j]-A[i-1][j]>0){
                    surface += A[i][j]-A[i-1][j];
                }
            }
            if((j+1)<=(A[0].size()-1)){
                if(A[i][j]-A[i][j+1]>0){
                    surface += A[i][j]-A[i][j+1];
                }
            }
            if((j-1)>=0){
                if(A[i][j]-A[i][j-1]>0){
                    surface += A[i][j]-A[i][j-1];
                }
            }
        }   
    }  
    
    //cout << "C:" << surface;
    
    return surface;
}
