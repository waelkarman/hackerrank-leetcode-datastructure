string encryption(string s) {
    stringstream ss;
    for(size_t i = 0; i < s.size(); i++){
        if(s.at(i) != ' '){
            ss << s.at(i);
        } 
    }
    
    string nospace = ss.str();
    ss.str("");
    
    //cout << "ss vuota: " << ss.str() << endl;
    //cout << ceil(sqrt(nospace.size()));
    //cout << floor(sqrt(nospace.size()));
     
      
    for(int k = 0; k <= ceil(sqrt(nospace.size())); k++){
        for(size_t i = 0; i < nospace.size(); i++){
            //cout << i % static_cast<int>(ceil(sqrt(nospace.size()))) << endl ;
            if(k == i % static_cast<int>(ceil(sqrt(nospace.size())))){
                ss << nospace.at(i);
            }
        }
        ss << ' ';
    }
    
    return ss.str();   
}
