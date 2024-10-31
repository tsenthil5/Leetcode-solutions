bool isPalindrome(char* s) {
    int start = 0;
    int end = strlen(s)-1;
    while(start<end){
        if(!isalnum(s[start])){
            start++;
        }
        else if(!isalnum(s[end])){
            end--;
        }
        else{
            if(tolower(s[start]) != tolower(s[end])){
                return false;
            }
            else{
                start++;
                end--;
            }
        }
    
    }
    return true;
}