int makingAnagrams(string s1, string s2) {
    unordered_map<char,int> char_map;
    int counter=0;
    
    for(size_t i = 0; i<s1.size();i++){
        if(char_map.find(s1[i])!=char_map.end()){
            char_map[s1[i]]++;
        }else{
            char_map[s1[i]]=1;
        }
    }
    
    for(size_t i = 0; i<s2.size();i++){
        if(char_map.find(s2[i])!=char_map.end()){
            char_map[s2[i]]--;  
        }else{
            counter++;
        }
    }

    unordered_map<char,int>::iterator it;
    for(it=char_map.begin(); it != char_map.end();it++){
        if(it->second !=0){
            counter=counter+abs(it->second);
        } 
    }
    
    return counter;
}
