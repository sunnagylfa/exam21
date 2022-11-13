

def main():
    """Function to check the validity of passwords"""
    #Empty list to collect passwords
    valid_list=[]
    invalid_list=[]
    #Ask user for password
    password=input("Enter password: ")
    while password!="quit":
        
        #Start checking length of password
        is_valid=check_length(password)
        #If long enough, check if it contains three numbers
        if is_valid:
            is_valid, digits=check_nums(password)
        #If both long enough and contains three numbers, print messsage
        if is_valid:
            print("Password is valid")
            valid_list.append(password)
        else:
        #If either is missing, print message
            print("Password is invalid")
            invalid_list.append(password)
        password=input("Enter password: ")
    if len(valid_list)>=1:
        print("\nValid passwords:")
        
        info(valid_list)
    if len(invalid_list)>=1:
        print("\nInvalid passwords:")
        info(invalid_list)
def check_length(password):
    """Function to check if password is longer than 8 chars"""
    if len(password)>=8:
        #return true if password is long enough
        is_valid = True
    else:
        is_valid = False
    return is_valid
def count_digits(password):
        #initialize number counter
    count=0
    for i in password:
        #Check every character in password, 
        #if they are numeric, add one to counter
        if i.isnumeric()==True:
            count+=1
    return count
def check_nums(password):
    """Function to check if password contains at least three numbers"""
    #check number of digits
    count=count_digits(password)
    if count>=3:
        #if count is 3 or more, return true
        is_valid = True
    else:
        is_valid = False
    return is_valid, count
def info(list):
    """function to print information about entered passwords"""
    #initialize counters
    length_of_password=0
    num_digits=0
    for password in list:
        #print all passwords in list
        print(password, end=" ")
        #add lengths 
        length_of_password+=len(password)
        #add digit count
        num_digits+=count_digits(password)
    #calculate average
    average_len=round(length_of_password/len(list), 1)
    average_dig=round(num_digits/len(list), 1)
    #print info
    print("\nAverage length: {}".format(average_len))
    print("Average # of digits:{}".format(average_dig))
    

        




if __name__ == "__main__":
    main()