string twoStrings(string s1, string s2) {

    unordered_map<char,int> char_map;
    for(int i = 0; i<s1.size(); i++ ){
        if(char_map.find(char_map[s1[i]])==char_map.end()){
            char_map[s1[i]]=1;
        }
    }
    
    for(int i = 0; i<s2.size(); i++ ){
        if(char_map.find(char_map[s2[i]])==char_map.end()){
            if(char_map[s2[i]]+1>1){
                return "YES";
            }
        }
    }
    return "NO";
}