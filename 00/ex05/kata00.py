kata = (19,42,21)

size = len(kata)
formatted_num = [str(num) for num in kata] 
formatted_num_str = ', '.join(formatted_num)

output = f"The {size} numbers are: {formatted_num_str}"
print(output)
