
int lonelyinteger(vector<int> a) {
    sort(a.begin(),a.end());

    //[122344]

    int old = a[0];
    int counter = 1;
    for(size_t i=1; i < a.size(); i++){
        if(old!=a[i]){ 
            if(counter == 1){
                return old;
            }
            counter=1;
        }else{
            counter++;
        }
        old=a[i];
    }
    
    return a[a.size()-1];
}
