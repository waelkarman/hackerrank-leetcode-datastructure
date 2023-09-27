vector<int> dynamicArray(int n, vector<vector<int>> queries) {
    
    vector<vector<int>> arr(n,vector<int>());
    int last = 0;
    vector<int> ans;
    
    for(auto a : queries){
        int x = a[1];
        int y = a[2];
        
        //cout << "Q:"<<a[0]<<" x:"<<x<<" y:"<<y<<" L:"<<last<<" n:"<<n<<" idx:"<<(x^last)%n<<endl;
        if(a[0]==1){
            int idx = (x^last)%n;
            arr[idx].push_back(y);
            //for(auto v : arr){
            //    for(auto i : v){
            //        cout<<i<<" ";   
            //    }
            //    cout<<endl;
            //}
        }
        
        if(a[0]==2){
            int idx = (x^last)%n;
            last = arr[idx][y%arr[idx].size()];
            ans.push_back(last);
        }
    }
    return ans;
}