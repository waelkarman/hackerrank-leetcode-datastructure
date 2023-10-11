vector<string> weightedUniformStrings(string s, vector<int> queries) {
    std::string alphabet = "abcdefghijklmnopqrstuvwxyz"; // find +1 = w
    std::string::size_type i = 0,count = 1;
    char save = '\0';
    vector<int> weight;
    vector<std::string> sol; 
    
    while(i < s.size()){
        
        if(s[i]==save){
            count++;
            weight.push_back((alphabet.find(s[i])+1)*count);
            
            save=s[i];
            i++;
            continue;
        }    
        if(s[i]!=save){
            weight.push_back(alphabet.find(s[i])+1);
            count=1;
            save=s[i];
            i++;
            continue;
        }
        
    }
    
    for_each(queries.begin(), queries.end(), [&](int n){
        std::vector<int>::iterator it = std::find(weight.begin(), weight.end(),n);
        if(it != weight.end()){
            sol.push_back("Yes");
        }else{
            sol.push_back("No");
        }
        
    });
    
    return sol;
}