def longestPalindrome(s: str) -> str:
    s_len = len(s)
    if len(s) <= 1:
        return s
    max_len = 1
    start = 0
    end = 0
#         for odd length plaindrome substring
    for i in range(s_len-1):
        m, n = i, i
        while (m >= 0 and n < s_len):
            if s[m] == s[n]:
                m -= 1
                n += 1
            else:
                break
        res_len = n-m-1
        if res_len > max_len:
            max_len = res_len
            start = m+1
            end = n-1
#                  for even th plaindrome substring
    for i in range(s_len-1):
        m = i
        n = i+1
        while (m >= 0 and n < s_len):
            if s[m] == s[n]:
                m -= 1
                n += 1
            else:
                break
        res_len = n-m-1
        if res_len > max_len:
            max_len = res_len
            start = m+1
            end = n-1
    print(start,end)
    return s[start:end+1]


print('longestPalindrome("asccc"): ', longestPalindrome("akccc"))
print('longestPalindrome("bbc"): ', longestPalindrome("khbbcd"))
print('longestPalindrome("babad"): ', longestPalindrome("fgbabad"))
