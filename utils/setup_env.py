def setup_env():
    variables = []
    with open('.env', 'r') as env:
        for line in env:
            variables.append(line.split('=')[1])
    return variables



if __name__ == '__main__':
    ...