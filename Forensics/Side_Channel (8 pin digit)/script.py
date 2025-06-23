import time
import subprocess

flag = ["0"] * 8


# To run the cmd
def run_cmd(cmd, pin_no):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	out, _ = p.communicate(bytes(pin_no, encoding='ascii'))
	print(out.decode().strip())


# Loop through all 8 digit
for k in range(8):
	timings = []
	# Try num 0 ~ 9
	for i in range(10):
		flag[k] = str(i)
		now = time.time()
		run_cmd(["./pin_checker"], "".join(flag))
		run_time = time.time() - now
		timings.append((i, run_time))

	# Sorted by highest time taken
	timings	= sorted(timings, key=lambda x:x[1], reverse=True)
	flag[k] = str(timings[0][0])


here_you_go = "".join(flag)
print(here_you_go)
