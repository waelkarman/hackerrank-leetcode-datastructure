string balancedSums(vector<int> arr) {
    
    bool not_found=true;
    int i=0;
    int j=arr.size()-1;
    int lsum=0;
    int rsum=0;
    
    while(not_found){
        
        if(lsum<rsum){
            lsum=lsum+arr[i];
            i++;
        }
        
        if(lsum>rsum){
            rsum=rsum+arr[j];
            j--;
        }
        
        if(lsum==rsum && i==j){
            not_found=false;
        }else if(lsum==rsum && arr[i]<arr[j]){
            lsum=lsum+arr[i];
            i++;
        }else if(lsum==rsum && arr[i]>=arr[j]){
            rsum=rsum+arr[j];
            j--;
        }
        if(i>j){
            break;
        }
    }
    
    if(not_found){
        return "NO";
    }else{
        return "YES";
    }    
    return "YES";
}