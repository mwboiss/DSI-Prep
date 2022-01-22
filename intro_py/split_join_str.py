def split_then_join(string, delimiter, new_delimiter):
    spltstring = string.split(delimiter)
    njstr = new_delimiter.join(spltstring)
    return njstr