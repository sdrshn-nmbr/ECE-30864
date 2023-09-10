def getStreaks(sequence, letters):
    result = []
    i = 0
    while i < len(sequence):
        if sequence[i] in letters:
            current = sequence[i]
            j = i + 1
            while j < len(sequence) and sequence[j] == sequence[i]:
                current += sequence[j]
                j += 1
            result.append(current)
            i = j
        else:
            i += 1
    return result

sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
print(getStreaks(sequence, "SAQT"))