string organizingContainers(vector<vector<int>> container) {
   
    vector<int> row(container.size(),0);
    vector<int> column(container.size(),0);
   
    for(size_t i = 0; i<container.size();i++){
        for(size_t j = 0; j<container[0].size();j++){
           //cout << container[i][j];
           row[i]+=container[i][j];
           column[j]+=container[i][j];
        }
        //cout << endl;
    }

    sort(row.begin(),row.end());
    sort(column.begin(),column.end());
    
    for(int i = 0; i<row.size(); i++){
        if(row[i]!=column[i]){
            return "Impossible";
        }
    }
    
    return "Possible";
}
