def load(filename):
    # Load and store a 3 value file.
    # Multipurpose beyond ('samples, values errors')
    # I know I'm bad.
    samples = []
    values = []
    errors = []
    with open(filename, 'r') as f:
        lines = list(f)
    f.close()
    for line in lines[1:]:
        line = line.split('\t')
        samples.append(float(line[0]))
        values.append(float(line[1]))
        errors.append(float(line[2]))

    return samples, values, errors
