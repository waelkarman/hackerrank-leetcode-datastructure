int simpleArraySum(vector<int> ar) {
    int temp = 0;
    std::vector<int>::iterator it = ar.begin();
    for(int i = 0; i<ar.size();i++){
        temp = temp + *it;
        it++;
    }
    return temp;
}
