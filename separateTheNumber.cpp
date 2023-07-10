void separateNumbers(string s) {
    std::string::size_type split_factor = 1;
    std::string::size_type temp_split_factor = 1;
    int starting_point = 0; 
    std::string isit = "NO";
    
    while(split_factor<=(s.size()/2)  && (starting_point+temp_split_factor) < s.size()){
        std::string starting_string = s.substr(starting_point,temp_split_factor);
        //std::cout << "STARTING" << starting_string << "- " << starting_point << "- "<< temp_split_factor << std::endl ;
        long int starting_number = std::stol(starting_string);
        
        //std::cout << starting_string << " starting  " << std::endl ;
        
        std::string str_to_search = std::to_string(starting_number+1);
        std::string temp_string = s.substr((starting_point+starting_string.size()),str_to_search.size());
        
        //std::cout << str_to_search << " == " << temp_string << std::endl ;
        
        if(str_to_search == temp_string){
            starting_point = starting_point + starting_string.size();
            temp_split_factor = str_to_search.size();
            isit="YES";
        }else{
            //std::cout << "aumento splitfactor e ripotvo" << std::endl ;
            split_factor++;
            starting_point = 0; 
            temp_split_factor = split_factor;
            isit="NO";
        }   
        
        
    }
    
    if(isit == "YES"){
        std::cout << isit << " " << s.substr(0,split_factor) << std::endl;
    }else{
        std::cout << isit << std::endl;
    }
}