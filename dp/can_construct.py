def can_construct(word, word_bank, memo={}):
    if word in memo:
        return memo[word]
    if word == '':
        return True

    for prefix in word_bank:
        if word.startswith(prefix):
            remaining = word.replace(prefix, '')
            if can_construct(remaining, word_bank, memo):
                memo[remaining] = True
                return True
    memo[word] = False
    return False


assert can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])  == True
assert can_construct('abcdefg', ['ab', 'abc', 'cd', 'def', 'abcd'])  == False
