long marcsCakewalk(vector<int> calorie) {
    sort(calorie.begin(),calorie.end());
    long int sum=0;
    for(size_t i = 0;i<calorie.size();i++){
        sum = sum+pow(2,i)*calorie[calorie.size()-1-i];
    }
    return sum;
}