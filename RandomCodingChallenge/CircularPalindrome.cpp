// TO OPTIMIZE



bool checkPalindrome(string s){
    std::string original = s;
    std::reverse(s.begin(), s.end());

    if (original == s) {
        return true;
    } else {
        return false;
    }
}


vector<int> circularPalindromes(string s) {
    
    vector<int> solution;
    
    for(size_t k=0; k<=s.size(); k++){
        size_t start = k;
        size_t end = (start+s.size()-1)%s.size();
        
        stringstream tmp;
        size_t i = start;
        while((i)%s.size()!=end){
            tmp << s[(i)%s.size()];
            i++;
        }
        tmp << s[(i)%s.size()];
        
        string tmpstr = tmp.str(); 
        //FIND BIGGEST PALINDROME
        size_t maxsize=0;
        for(size_t j = 0; j<tmpstr.size(); j++){
            size_t p = tmpstr.size();
            while(j<p){
                if(tmpstr[j]==tmpstr[p]){
                    //MIGHT DEFINE A PALINDROME
                    string substr = tmpstr.substr(j, p-j+1);
                    if(checkPalindrome(substr)){
                        if(substr.size()>maxsize)
                            maxsize=substr.size();
                    }
                }
                p--;
            }
        }    
        solution.push_back(maxsize);
    }
    
    solution.pop_back();
    return solution;
}