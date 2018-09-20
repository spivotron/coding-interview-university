def sequence_calss(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls

seq = sequence_calss(immutable=True)
