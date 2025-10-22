import sys

q = int(sys.stdin.readline().strip())

s_list = []
balance = 0
min_prefix_balance = [0] 
output = []

for _ in range(q):
    line = sys.stdin.readline().strip().split()
    query_type = int(line[0])

    if query_type == 1:
        # Append character c
        char_c = line[1]
        s_list.append(char_c)
        
        # pdate running balance
        if char_c == '(':
            balance += 1
        else:
            balance -= 1
            
        # Update minimum prefix balance stack
        # The new minimum is min(minimum of previous prefixes, current total balance)
        new_min = min(min_prefix_balance[-1], balance)
        min_prefix_balance.append(new_min)
        
    elif query_type == 2:
        # Remove last character (guaranteed not empty)
        
        if not s_list:
            continue 

        char_to_remove = s_list.pop()
        
        # everse update balance
        if char_to_remove == '(':
            balance -= 1
        else:
            balance += 1
        
        # Remove the corresponding minimum prefix balance
        min_prefix_balance.pop()
    
    if balance == 0 and min_prefix_balance[-1] >= 0:
        output.append("Yes")
    else:
        output.append("No")

# Print all results separated by newlines
sys.stdout.write("\n".join(output) + "\n")