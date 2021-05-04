def naive_str_matcher_2for(pattern: str, text: str):
    for t_idx in range(len(text) - len(pattern) + 1):
        p_idx = 0

        flag = True
        for check_idx in range(t_idx, t_idx + len(pattern)):
            if pattern[p_idx] != text[check_idx]:
                flag = False
                break
            p_idx += 1

        if flag:
            print('found pattern!')
            return


def naive_str_matcher(pattern: str, text: str):
    for t_idx in range(len(text) - len(pattern) + 1):
        flag = True
        check_idx = t_idx
        p_idx = 0
        while check_idx < t_idx + len(pattern):
            if pattern[p_idx] != text[check_idx]:
                flag = False
                break

            check_idx += 1
            p_idx += 1

        if flag:
            print('found pattern!')
            return


def naive_str_matcher_from_pseudo(pattern: str, text: str):
    n = len(text)
    m = len(pattern)

    for s in range(n - m + 1):
        j = 0
        while j < m and text[s + j] == pattern[j]:
            j += 1

        if j >= m:  # if match time >= the len of pattern
            print('found pattern!')
            return


T = 'eceyeye'
P = 'eye'
# naive_str_matcher(P, T)
naive_str_matcher_from_pseudo(P, T)
