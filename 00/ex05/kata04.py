kata = (0, 4, 132.42222, 10000, 12345.67)

formatted_str = "module_{:02d}, ex_{:02d} : {:.2f}, {:.2e}, {:.2e}".format(kata[0], kata[1], kata[2], kata[3], kata[4])
print(formatted_str)
