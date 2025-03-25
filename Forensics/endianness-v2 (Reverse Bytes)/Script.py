with open('challengefile','rb') as f:
	data = f.read()
	data_hex = data.hex()
data = str(data_hex)

array_data = [data[i:i+8] for i in range(0,len(data),8)]
reversed_values = ["".join(reversed([h[i:i+2] for i in range(0, len(h), 2)])) for h in array_data]
reversed_values = "".join(reversed_values)

with open('reversedbytes.txt','w') as f:
	f.write(reversed_values)