int beautifulBinaryString(string b) {
    std::string target = "010";
    std::string::size_type i = 0;
    int count =0;
    int k=0;
    bool enter = false;
    while(i<b.size()){
        //std::cout << "INIZIO enter:"<< enter << "   k:"<< k << "   b[i]:"<< b[i] <<target[k]<< std::endl;
        if(b[i]=='0' && k==1){
            enter=true;
            k=0;
        }
        
        if(b[i]=='0' && !enter){
            //std::cout << "CONTA " << std::endl;
            enter=true;
            k=0;
        }
        
        
        if(enter){
            
            if(b[i]==target[k]){
                if(k==2){
                    //b.replace(i,1,"R");
                    count++;
                    enter = false;
                }
                k++;
            }else{
                enter = false;
            }
            
        }
        
        std::cout << b << std::endl;
        //std::cout << "FINE enter:"<< enter << "   k:"<< k << "   b[i]:"<< b[i]<<target[k] << std::endl;
        i++;
    }
    return count;
}