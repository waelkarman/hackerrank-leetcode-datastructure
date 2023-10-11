string superReducedString(string s) {
    if(s.empty()){
        return "Empty String";
    }
    
    char save;
    int count = 0;
    std::string::size_type i = 0;
    
    while(i < s.size()){
        std::cout << "count == " << count << "s = "<< s[i] << std::endl;
        if(save != s[i]){
            count++;
            save = s[i];
            i++;
            continue;
        }
        if(count > 0 && save == s[i]){
            std::cout << s <<"  --trovato duplicato da rimuovere  "<< i-1 << " -- " << s[i-1] << " - " << s[i] << std::endl;
            s.erase(i-1, 2);
            std::cout << s << "  --oltre la rimozione;" << std::endl;
            count=0;
            i=0;
            save = '\0';
            continue;
        }
        
        save = s[i];
        count=0;
        i++;
    }
    
    if(s.empty()){
        return "Empty String";
    }
    
    return s;
}
