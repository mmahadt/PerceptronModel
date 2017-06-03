#Implementation of perceptron model
#Only change the results and get the
#weights
w1 = w2 = 0 #initial weights

eta = 0.1 #it is the learning rate

def perceptron(x,y):
	if (x*w1 + y*w2) < 1:
		return 0
	else:
		return 1

#Comment out one of the following two results array at a time
#for desired functionality

results = [0,1,1,1] #expexted results array for OR

# results = [0,0,0,1] #expexted results array for AND

x_vals = [0,0,1,1]	#Truth table x-values

y_vals = [0,1,0,1]	#Truth table y-values

def tries():#One try of weight values to check against expected resuts
	perceptron_output = []
	for i in range(4):
		print perceptron(x_vals[i],y_vals[i])
		perceptron_output.append(perceptron(x_vals[i],y_vals[i]))
	print perceptron_output
	return perceptron_output


def trainer():#Trains the perceptron to adjust the weights to get the expected results
	global w1,w2
	# print results
	iteration = 0
	while (True):
		iteration = iteration+1;
		print iteration
		tries1 = tries()
		if( tries1 == results):
			print "w1: "+str(w1)
			print "w2: "+str(w2)
			return
		else:
			w1 = eta + w1
			w2 = eta + w2
			tries()

trainer()
