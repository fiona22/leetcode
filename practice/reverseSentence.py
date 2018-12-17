def reverseSentense(inputSen):
    inputSen = inputSen.split()
    inputSen.reverse()
    return inputSen


if __name__ == '__main__':
    for str_out in reverseSentense(raw_input()):
        print str_out,


