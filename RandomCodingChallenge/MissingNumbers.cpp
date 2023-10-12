vector<int> missingNumbers(vector<int> arr, vector<int> brr) {
    sort(arr.begin(),arr.end());
    sort(brr.begin(),brr.end());
    
    set<int> sol;
    while(arr.size()>0){
        if(arr.back()==brr.back()){
            arr.pop_back();
            brr.pop_back();
        }else{
            sol.insert(brr.back());
            brr.pop_back();
        }
    }
    
    while(brr.size()>0){
        sol.insert(brr.back());
        brr.pop_back();
    }
    
    vector<int> solvect(sol.begin(), sol.end());
    return solvect;
}