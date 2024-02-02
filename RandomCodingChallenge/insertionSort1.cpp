void insertionSort1(int n, vector<int> arr) {
    
    int val = arr[n-1];
    int i=n-1;
    while(i>0){
        
        if(val<arr[i-1]){
            arr[i]=arr[i-1];
            if(i == 1){
                for (const auto& element : arr) {
                    std::cout << element << " ";
                }
                cout << endl;
                arr[i-1]=val;
                break;
            }
        }else{
            arr[i]=val;
            break;
        }
        
        for (const auto& element : arr) {
            std::cout << element << " ";
        }
        cout << endl;
        
        i--;
    }
    
    for (const auto& element : arr) {
        std::cout << element << " ";
    }
    
}
