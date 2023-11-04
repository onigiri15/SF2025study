def check():
	answer=input()
	if answer=="c":
		print("command;")
		print("    restart;r")
		print("    all fanction;f")
		print("    print command;c")
		print("    setting;s")
		print("    cancel;0")
	if answer=="r":
		simulate()
	if answer=="f":
		print("basic forth setting;1")
		print("friction setting;2")
		print("rebound setting;3")
		answer2=input()
		if answer2=="1":
			print("basic forth setting")
			print("X")
			answer3_X=input("indefinite factors")
			if answer3_X=="0":
				print("defined factors")
				X_defined_factors=input()
			if answer3_X=="1":
				print("defined factors")
				X_indefinite_factors_range_from=input("random range from?")
				X_indefinite_factors_range_to=input("random range to?")
			print("Y")
			answer3_Y=input("indefinite factors")
			if answer3_Y=="0":
				print("defined factors")
				Y_defined_factors=input()
			if answer3_Y=="1":
				print("defined factors")
				Y_indefinite_factors_range_from=input("random range from?")
				Y_indefinite_factors_range_to=input("random range to?")
			print("basic forth setting")
			print("Z")
			answer3_Z=input("indefinite factors")
			if answer3_Z=="0":
				print("defined factors")
				Z_defined_factors=input()
			if answer3_Z=="1":
				print("defined factors")
				Z_indefinite_factors_range_from=input("random range from?")
				Z_indefinite_factors_range_to=input("random range to?")

		if answer2=="2":
			print("friction setting")
			most_friction_forse=input("most friction forse")
			moving_friction_forse=input("moving friction forse")
		if answer2=="3":
			print("rebound setting")
			
		while n<=object_count:
			input("object")
	if answer=="s":
		print("setting")
				
def simulate():
	t=0
	d_t=input("simulating precision of time?")
	time_limit=input("time limit?")
	object_location_X[n]= initial_object_location_X[n]
	object_location_Y[n]= initial_object_location_Y[n]
	object_location_Z[n]= initial_object_location_Z[n]
	while t<time_limit:
		t=t+d_t
		n=0
		while n<=(object_count-1):
			v_x[n]=v_x[n]+(F[n]/object_math[n])/d_t
			v_y[n]=v_y[n]+(F[n]/object_math[n])/d_t
			v_z[n]=v_z[n]+(F[n]/object_math[n])/d_t
			object_location_X[n]=object_location_X[n]+v_X[n]/d_t
			object_location_Y[n]=object_location_Y[n]+v_Y[n]/d_t
			object_location_Z[n]=object_location_Z[n]+v_Z[n]/d_t
			n=n+1

F_x=[]
F_y=[]
F_z=[]
v_x=[]
v_y=[]
v_z=[]
x=[]
y=[]
z=[] 
object_math=[]
object_count=input("how many objects")
n=0
while n<=(int(object_count)-1):
	object_math[n]=input("math? "+str(n)+" object")
	initial_object_location_X[n]=input("location_X"+string(n)+"object")
	initial_object_location_Y[n]=input("location_Y"+string(n)+"object")
	initial_object_location_Z[n]=input("location_Z"+string(n)+"object")
	initial_object_scale_X[n]=input("scale_X"+string(n)+"object")
	initial_object_scale_Y[n]= input("scale_Y"+string(n)+"object")
	initial_object_scale_Z[n]= input("scale_Z"+string(n)+"object")
	n=n+1
if input("if you want start,put “S”")=="S":
	print("start")
	simulate()
	check()
