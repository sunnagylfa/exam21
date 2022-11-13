def main():
    file_name = input("Enter file name: ")
    file_object = open_file(file_name)
    # Your continue the program from here
    if file_object!=None:
        show_totals=input("Show totals per store (y/n)?: ")
        sales_list=readsales(file_object)
        sales_list=check_for_duplicates(sales_list)
        print_table(sales_list)

        if show_totals=="y":
            print_totals(sales_list)

def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    print("File",filename,"not found")
    return None
def readsales(file_object):
    """Input: File object with x lines. In each line there is a name and then number seperated by ";"
        Output: List of tuples. Each Tuple contains name and then a list of grades"""
    #Empty tuple and list for output
    icecream_tuple = ()
    icecream_list =[]
    #Read each line in file object
    for line in file_object:
        #empty list for sales
        sales =[]
        #make list from each line
        line = line.strip().split(";")
        #First item in line is name, so from line[1] and onwards
        for i in range(1, len(line)):
            if line[i] != "":
                #add sales to sale list
                sales.append(round(float(line[i]), 2))

        #Add tuples to list
        #calculate total sales for each flavor
        total=0
        for i in sales:
            total+=i
        total=round(total, 2)
        #Add name and sales to tuple
        icecream_tuple = [line[0], sales, total]
        icecream_list.append(icecream_tuple)
        icecream_list=sorted(icecream_list, 
       key=lambda x: x[0])
        
    return icecream_list
def print_table(icecream_list):
    """Function to print out a table with sales information
    Input: List: [flavor, (sales numbers), total sales]
    return: none"""
    #For each item in list print adjusted line
    for flavor in icecream_list:
        print(flavor[0].ljust(15), end="")
        for num in flavor[1]:
            print(f"{num:.2f}".rjust(12),end="")
        print(f"{flavor[2]:.2f}".rjust(12))
    return None
def print_totals(icecream_list):
    """Function to print totals from each store
    intake: icecream_list
    return: None"""
    #make empty lists
    all_sales_list=[]
    totals_list=[]
    #make list with only sale numbers
    for i in range(0,len(icecream_list)):
        all_sales_list.append(icecream_list[i][1])
    
    #calculate totals for each store
    for j in range(0, len(all_sales_list[1])):
        sum=0
        for i in all_sales_list:
            sum+=i[j]
        totals_list.append(sum)

    #print totals to table        
    print ("Total:".ljust(15), end="")
    for i in totals_list:
        print(f"{i:.2f}".rjust(12), end="")
    return None

def check_for_duplicates(icecream_list):
    """function to check if flavors appear more than once and
    fix list accordingly by adding total nums"""
    flav_list=[]
    item_list=[]
    dupl_list=[]
 
    for item in icecream_list:
        if item[0] not in flav_list:
            flav_list.append(item[0])
            item_list.append(item)
        else:
            dupl_list.append(item)
    for dupl in dupl_list:
    
        for item in item_list:
            if item[0]==dupl[0]:
                for i in range(0, len(item[1])):
                    item[1][i]+=dupl[1][i]
                item[2]=dupl[2]+item[2]


    return item_list
                    




    
# Main program starts here.  Do NOT change the starter code.
if __name__ == "__main__":
    main()