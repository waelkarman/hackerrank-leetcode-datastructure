string funnyString(string s) {
    std::string rev_s;
    for_each(s.rbegin(),s.rend(), [&](char c){
        rev_s.push_back(c);
    });
    
    for(std::string::size_type i = 0;i<(s.size()-1); i++ ){
        
        if( std::abs(s[i]-s[i+1]) == std::abs(rev_s[i]-rev_s[i+1]) ){
            ;
        }else{
            return "Not Funny";
        }
    }
    
    return "Funny";
    
}