# Test python env
def print_hello():
    animals = ['dog', 'cat', 'hamster']
    foods = [
            'SSSpagetti',
            'PPizza'
    ] # w/o trailing comma
    names = [
            'John',
            'Jane',
            'Gill-dong',
    ]# w/ trailing comma
    for f_name in names:
        print (f"hello, {f_name}")

if __name__ == '__main__':
    print_hello()        
