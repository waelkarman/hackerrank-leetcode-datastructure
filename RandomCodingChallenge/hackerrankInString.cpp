string hackerrankInString(string s) {
    std::string hackerrank = "hackerrank";
    std::string::size_type i,k = 0;
    while(i<s.size()){
        if(hackerrank[k] == s[i]){
            k++;
        }    
        i++;
    }
    
    if(k==hackerrank.size())
        return "YES";
    else
        return "NO";  
}