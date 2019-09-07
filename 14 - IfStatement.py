is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall")
elif is_male and not(is_tall):
    print("You are a male but not tall")
else:
    print("You are a female")