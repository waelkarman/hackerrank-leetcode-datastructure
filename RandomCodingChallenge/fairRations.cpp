string fairRations(vector<int> B) {
    vector<int>::iterator it;
    int update=0;
    for(it = B.begin(); it != B.end();it++){
        if(*it%2!=0){
            *it=*it+1;
            if((it+1) != B.end())
                *(it+1)=*(it+1)+1;
            else
                return "NO";
            update=update+2;
        }
        
        for(int a : B){
            cout << a ;
        }
        cout << endl;
    }
    
   return to_string(update); 
}