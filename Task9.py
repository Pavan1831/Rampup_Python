def full_justify(words, maxWidth):
    result, current_line, current_width = [], [], 0

    for word in words:
        if current_width + len(word) + len(current_line) > maxWidth:
            for i in range(maxWidth - current_width):
                current_line[i % (len(current_line) - 1 or 1)] += ' '

            result.append(''.join(current_line))
            current_line, current_width = [], 0

        current_line += [word]
        current_width += len(word)

    result.append(' '.join(current_line).ljust(maxWidth))

    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = full_justify(words, maxWidth)

# Output the formatted text
for line in output:
    print(line)
