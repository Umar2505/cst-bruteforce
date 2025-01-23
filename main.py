import argon2

hash_params = {
    'time_cost': 3,  # Adjust as needed (higher is more secure, slower)
    'memory_cost': 65536,  # Adjust as needed (higher is more secure, uses more memory)
    'parallelism': 20,  # Adjust as needed (higher for faster hashing on multi-core systems)
    'salt_length': 16,  # Adjust as needed (salt length in bytes)
}

# Create an Argon2 object with the specified parameters

ph = argon2.PasswordHasher()
ph.from_parameters(argon2.Parameters(argon2.Type.D,19,16,32,3,65536,20))
ph._parameters.parallelism = 20
ph._parameters.type = argon2.Type.D

# with open("passwords.txt", 'r') as file:
# 	for line in file:
# 		line = line.strip()
# 		for i in range(10):
# 			r = f"{i}{line}"
# 			for j in range(10):
# 				k = f"{r}{j}"
# 				with open('results.txt', "a") as f:
# 					f.write(f"{k}\n")
# 				ch = ph.hash(k)
# 				if ch == "$argon2id$v=19$m=65536,t=3,p=20$xCqJqeKm+gnXDA6mHCJL+g$fHtwZYpl2GxwRz1KTgVYuu+h4YoQeDw76+gcwHELums":
# 					print(k)
with open('results.txt', 'r') as fi:
	for line in fi:
		line = line.strip()
		ch = ph.hash(line)
		print(ch)
		ch = ph.hash(line)
		print(ch)
		break
		# with open('hashes.txt', 'a') as l:
		# 	l.write(f"{ch}\n")
		# if ch == "$argon2d$v=19$m=65536,t=3,p=20$xCqJqeKm+gnXDA6mHCJL+g$fHtwZYpl2GxwRz1KTgVYuu+h4YoQeDw76+gcwHELums":
		# 	print(line)
