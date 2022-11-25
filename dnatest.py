def is_vaild_sequence(dna):
    if dna[0] not in ['A','T','G','C']:
        return False
    if len(dna) == 1:
        return True
    return is_vaild_sequence(dna[1:])

print(is_vaild_sequence("BWRQRQ"))