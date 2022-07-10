def merge_the_tools(s, k):
    num_subsegments = int(len(s) / k)
    
    for index in range(num_subsegments):
        t = s[index * k : (index + 1) * k]
    
    # Subsequence string having distinct characters
        u = ""
    
    # If a character is not already in 'u', append
        for c in t:
            if c not in u:
                u += c

    # Print final converted string
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
