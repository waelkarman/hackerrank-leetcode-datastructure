int gemstones(vector<string> arr) {
    std::string sol = arr[0];
    for_each(arr.begin(), arr.end(), [&](std::string s){
        std::string::size_type i=0;
        while( i<sol.size() ){
            if(s.find(sol[i],0) == std::string::npos ){
                std::cout << "DA LEVARE: " << sol[i] << std::endl;
                sol.erase(i,1);
                i--;
            }
            i++;
        }
         
    });
    std::set<char> soluz;
    for_each(sol.begin(), sol.end(), [&](char c){
        soluz.insert(c);    
    });
    return static_cast<int>(soluz.size());
}