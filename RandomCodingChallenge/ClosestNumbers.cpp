vector<int> closestNumbers(vector<int> arr) {
    map<int,set<int>> num_map;
    for(int i = 0; i<arr.size();i++){
        for(int k = i+1; k<arr.size();k++){
            num_map[abs(arr[i]-arr[k])].insert(arr[i]);
            num_map[abs(arr[i]-arr[k])].insert(arr[k]);
        }
    }
    
    map<int,set<int>>::iterator it = num_map.begin();
    int min_key = it->first;

    std::vector<int> num_vect(num_map[min_key].begin(), num_map[min_key].end());
    return num_vect;
}