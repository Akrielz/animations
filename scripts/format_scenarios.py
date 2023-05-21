def format_overflow(file_path: str, max_len: int = 129):
    # open file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # For each line, check if its len > 127, if so, move the rest of the line to the next line
    i = 0
    while i < len(lines):
        line = lines[i]
        if len(line) < max_len:
            i += 1
            continue

        # find the last space before the max_len
        last_space = line.rfind(' ', 0, max_len)
        if last_space == -1:
            last_space = max_len

        # save the rest of the line
        rest_of_line = line[last_space + 1:]

        # remove the rest of the line from the current line
        lines[i] = line[:last_space] + '\n'

        # insert the rest of the line to the next line
        if i + 1 >= len(lines):
            lines.append("")

        # Remove the newline character from the rest of the line
        rest_of_line = rest_of_line.replace('\n', '')

        # Add a white to the end of the rest of the line
        rest_of_line += ' '

        # Insert the rest of the line to the next line
        lines[i+1] = rest_of_line + lines[i+1]

    # Save the file
    with open(file_path, 'w') as f:
        f.writelines(lines)


format_overflow("_2023/geometric_perspective_transformer/scenario.txt")