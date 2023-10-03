void kaprekarNumbers(int p, int q) {
    bool no_kaprekar = true;
    for(unsigned long long int i = p ; i<=q ; i++ ){
        
        unsigned long long int powi = i*i;
         
        string str_powi = to_string(powi);
        
        if(str_powi.length()>1){
            
            if(str_powi.substr(0,str_powi.length()/2).length() != 0 && str_powi.substr(str_powi.length()/2,str_powi.length()).length()!= 0){
                
                if(i == (stoll(str_powi.substr(0,str_powi.length()/2)) + stoll(str_powi.substr(str_powi.length()/2,str_powi.length())) ) ){
                    cout << i << " " ; 
                    no_kaprekar = false;
                }  
            }    
        }else{
            if(str_powi.substr(str_powi.length()/2,str_powi.length()).length() != 0 && stoll(str_powi.substr(str_powi.length()/2,str_powi.length())) == i ){
                    cout << i << " " ; 
                    no_kaprekar = false;     
            }
        }
    }
    
    if(no_kaprekar){
        cout << "INVALID RANGE";
    }
    
}