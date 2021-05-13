
def main():
  query = input("> ")


  # Modes
  if not query.find("+") == -1: # Addition
    mode = 1

  if not query.find("-") == -1: # Subtraction
    mode = 2

  if not query.find("/") == -1: # Division
    mode = 3

  if not query.find("*") == -1: # Multiplication 
    mode = 4


  # Output
  if mode == 1:
    nums = query.rsplit("+")
    print(int(nums[0]) + int(nums[1]))

  if mode == 2:
    nums = query.rsplit("-")
    print(int(nums[0]) - int(nums[1]))

  if mode == 3:
    nums = query.rsplit("/")
    print(int(nums[0]) / int(nums[1]))

  if mode == 4:
    nums = query.rsplit("*")
    print(int(nums[0]) * int(nums[1]))

while True:
  main()
