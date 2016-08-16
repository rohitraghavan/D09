x = 0
y = 1
names = ["Guido"]
try:
    this
except NameError as e:
    print("Debug Note: we haven't defined *this* yet.")
try:
    print(names[y])
except IndexError:
    print("You attempted to use an index larger than our list of names.")
    print("You attempted: {} Highest Index: {}".format(y, len(names)-1))
try:
    ans = 3/x
except ZeroDivisionError as e:
    print("x cannot be zero: you just attempted {}".format(e))
try:
    if x < 2:
        raise ValueError("this function requires x >= 2")
except ValueError as e:
    print("Raised ValueError:{e}".format(e=e))

except Exception as e:
    print("I wasn't prepared for this:")
    print(type(e), e)
