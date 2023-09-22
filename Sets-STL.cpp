int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int qn;
    cin >> qn ;
    int tmp0,tmp1;
    set<int> s;
    for(int i=0;i<qn;i++){
        cin >> tmp0 >> tmp1;
        if (tmp0==1){
            s.insert(tmp1);
        }else if(tmp0==2){
            s.erase(tmp1);
        }else if(tmp0==3){
            set<int>::iterator it=s.find(tmp1);
            if(it == s.end()){
                cout << "No" <<endl;
            }else{
                cout << "Yes" <<endl;
            }
        }
    }
    
    return 0;
}
