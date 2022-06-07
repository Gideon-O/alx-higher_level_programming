#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    str_first = sentence[0]
    data = ()
    if str_len <= 0:
        data = str_len, None
    else:
        data = str_len, str_first
    return data


if __name__ == "__main__":
    multiple_returns(sentence)
