
def called_function():
  print('called function')

def calling_function():
  print('Calling Function')
  called_function()

def main():
  calling_function()

main()
