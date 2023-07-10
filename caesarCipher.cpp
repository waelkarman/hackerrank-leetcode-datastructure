string caesarCipher(string s, int k) {
    std::string alphabet = "abcdefghijklmnopqrstuvwxyz";
    std::string sol = "";
    
    for_each(s.begin(), s.end(), [&](char c){
        if(std::isalpha(c)){
            if(std::isupper(c)){
                sol.push_back(std::toupper(alphabet[(alphabet.find(std::tolower(c))+k)%alphabet.size()]));    
            }else{
                std::cout << "VALORE TROVATO : " << alphabet[(alphabet.find(c)+k)%alphabet.size()] << std::endl;
                sol.push_back(alphabet[(alphabet.find(c)+k)%alphabet.size()]);    
            }
        }else{
            sol.push_back(c);
        }
    });
    
    return sol;
}