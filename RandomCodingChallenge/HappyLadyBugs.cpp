string happyLadybugs(string b) {
    
    if(b.size()<2){
        if(b == "_"){
            return "YES";
        }
        return "NO";
    }
    
    char tmp=b[0];
    int counter=0;
    bool unhappy=false;
    map<char,int> char_map;
    int us_counter=0;
    for(int i = 0; i<b.size(); i++){
        // count the underscore
        if(b[i] == '_'){
            us_counter++;
        }        
        // count the number of occurrence
        if(b[i]!='_'){
            if(char_map.find(b[i]) != char_map.end()){
                char_map[b[i]]++;   
            }else{
                char_map[b[i]]=1;
            }
        }
        //happy unhappy check
        if(b[i] != '_'){
            if(b[i] == tmp){
                counter++;
            }else if(tmp != b[i] && counter>1){
                tmp = b[i];
                counter=1;
            }else{
                tmp=' ';
                unhappy=true;
            }
        }
    }
    
    if(us_counter == 0 && unhappy){
        return "NO";
    }else{
        for(map<char,int>::iterator it = char_map.begin(); it != char_map.end() ;it++){
            if(char_map.find(it->first) != char_map.end() && char_map[it->first]<2){
                return "NO";
            }
        }
        return "YES";
    }
    
   return "NO"; 
}