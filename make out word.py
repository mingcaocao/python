def make_out_word(out, word):
    if len(out) != 4:
        print 'bad input'
    else:
        s = out[:2] + word + out[2:]
    return s
