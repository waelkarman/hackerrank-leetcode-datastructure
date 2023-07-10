vector<int> compareTriplets(vector<int> a, vector<int> b) {
    std::vector<int>::iterator ita = a.begin();
    std::vector<int>::iterator itb = b.begin();
    int ascore = 0;
    int bscore = 0;    
    
    for(int i =0; i<3; i++){
        if(*ita==*itb){
            ita++;
            itb++;
            continue;
        }
        
        if(*ita<*itb){
            bscore += 1;
        }else{
            ascore += 1;
        }
        ita++;
        itb++;
        
    }

    std::vector<int> s = {ascore,bscore};
    return s;
    
}
