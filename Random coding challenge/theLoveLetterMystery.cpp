int theLoveLetterMystery(string s) {
    std::string::size_type i=0;
    int sum=0;
    while(i < (s.size()/2)){
        sum += std::abs(s[i]-s[s.size()-i-1]);
        i++;
    }

    return sum;
}