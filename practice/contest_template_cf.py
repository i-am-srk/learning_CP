import sys

def is_good(x: int, d: int) -> bool:
    """
    Checks if x can be transformed into a set of d-multiples.
    O(1) check.
    """
    # 1. Too small to be a d-multiple
    if x < d:
        return False
    
    # 2. Already a d-multiple
    if x % d == 0:
        return True
        
    # 3. Not a d-multiple, and too small to split (d < x < 2d)
    if x < 2 * d:
        return False
        
    # 4. Complex case: x > 2d and not a d-multiple
    # We need to find a d-multiple x3 in the range [ceil((x-d)/2), x-2d]
    
    # Calculate lower bound for x3
    # (x - d + 1) // 2 is equivalent to ceil((x-d)/2)
    lower_bound = (x - d + 1) // 2
    
    # Calculate upper bound for x3
    upper_bound = x - 2 * d
    
    # Check if the range is valid
    if lower_bound > upper_bound:
        return False
        
    # Find the smallest d-multiple >= lower_bound
    # (lower_bound + d - 1) // d gives the multiplier
    first_multiple = ((lower_bound + d - 1) // d) * d
    
    # Check if this multiple is within the valid range
    return first_multiple <= upper_bound

def solve():
    # Read all input data at once for fast I/O
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    t = int(input_data[0])
    results = []
    
    ptr = 1
    for _ in range(t):
        n = int(input_data[ptr])
        k = int(input_data[ptr+1])
        ptr += 2
        
        a = []
        max_val = 0
        for i in range(n):
            val = int(input_data[ptr + i])
            a.append(val)
            max_val = max(max_val, val)
        ptr += n
        
        # Count frequency of each number up to max_val
        max_idx = max_val + 1
        counts = [0] * max_idx
        for x in a:
            counts[x] += 1
            
        max_beauty = 1
        
        # Iterate d from max_val down to 1.
        # Total complexity is Sum over t of (N log N)
        for d in range(max_val, 0, -1):
            
            erased_count = 0
            
            # This inner loop is O(max_val) = O(N)
            for x in range(1, max_idx):
                if counts[x] == 0:
                    continue
                
                # Check the O(1) condition
                if not is_good(x, d):
                    erased_count += counts[x]
            
            if erased_count <= k:
                max_beauty = d
                break
                
        results.append(str(max_beauty))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()