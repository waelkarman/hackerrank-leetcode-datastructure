int marsExploration(string s) {
    std::string::size_type i = 0;
    std::string sos = "SOS";
    int count = 0;
    while(i < s.size()){
        if(sos[i%3] != s[i]){
            count++;
        }
        i++;
    }
    return count;
}