password = "jU5t_a_s1mpl3_an4gr4m_4_u_c79a21"
   
buffer = [''] * 32  # Initialize an empty character list of size 32

# First loop (copy first 8 characters directly)
for i in range(8):
    buffer[i] = password[i]

# Second loop (reverse select from index 23 - i)
for i in range(8, 16):
    buffer[i] = password[23 - i]

# Third loop (select characters from 46 - i, skipping every 2)
for i in range(16, 32, 2):
    buffer[i] = password[46 - i]

# Fourth loop (copy characters directly from index 17 to 31, decrementing by 2)
for i in range(31, 16, -2):
    buffer[i] = password[i]

transformed_password = ''.join(buffer)


print(transformed_password)
