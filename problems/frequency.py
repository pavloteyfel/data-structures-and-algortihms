# Demonstrates usage of frequency counter 

def anagram_v2(s1, s2):
    s1_counter = {}
    s2_counter = {}

    for s in s1:
        s1_counter[s] = s1_counter.get(s, 0) + 1

    for s in s2:
        s2_counter[s] = s2_counter.get(s, 0) + 1

    return s1_counter == s2_counter

def anagram_v3(s1, s2):
    if len(s1) != len(s2):
        return False
    
    memory = {}

    for s in s1:
        memory[s] = memory.get(s, 0) + 1

    for s in s2:
        if memory.get(s, 0) == 0:
            return False
        else:
            memory[s] -= 1
    return True

assert anagram_v2('anagram', 'gramana') == True
assert anagram_v3('anagram', 'gramana') == True