import time
import math
import matplotlib.pyplot as plt


def Eratosthenes_sieve(n):
	t1 = time.time()
	prime_list = list(range(n+1))
	prime_list[0], prime_list[1] = 0, 0
	for index in range(int(math.sqrt(n+1))):
		if prime_list[index]:
			for next_index in range(index*index, n+1, index):
				prime_list[next_index] = 0
	result = set(prime_list)
	result.remove(0)
	print(time.time() - t1, 'sec')
	return sorted(result)


def calculates_binary_shift(decimal):
	xp, yp = 0, 0
	b = bin(decimal)
	for step, i in enumerate(range(2, len(b) - 1)):
		turn = b[-i]
		if turn == '1':
			xp += s / (visualization_factor ** step)
		else:
			yp += s / (visualization_factor ** step)
		# print(step, xp, yp)
	return xp, yp


def calculate_paths(n, set_of_primes):
	prime_color, no_prime_color = 'red', 'white'
	s = 100  # base graph segment length
	x, y, color = [], [], []
	for i in range(n + 1):
		x.append(0), y.append(0), color.append(no_prime_color)

	for decimal in range(3, n+1, 2):
		if decimal in set_of_primes:
			color[decimal] = prime_color
			b = bin(decimal)
			for step, i in enumerate(range(2, len(b) - 1)):
				turn = b[-i]
				if turn == '1':
					x[decimal] += s / (visualization_factor ** step)
				else:
					y[decimal] += s / (visualization_factor ** step)
		# print(decimal, b, x[decimal], y[decimal])

	return x, y, color


def calculate_prime_paths(set_of_primes):
	x, y, color = [], [], []
	for i in range(len(set_of_primes)):
		x.append(0), y.append(0), color.append(prime_color)

	for p, decimal in enumerate(set_of_primes):
		x[p], y[p] = calculates_binary_shift(decimal)

	return x, y, color


if __name__ == '__main__':
	prime_color, no_prime_color = 'red', 'white'
	s = 100  # base graph segment length
	annotations = False
	n_annotations = 200
	visualization_factor = 1.1  # a 2-factor reduces squares to half
	power = 18
	n = 2**power
	reduction_factor = 2**(power-18) if power > 18 else 1
	plot_prime_numbers = True
	plot_exp_lines = False
	plot_horizon = True

	# calculates_binary_shift(262139), input()
	# calculates_binary_shift(1048573), input()

	primes_calculated = Eratosthenes_sieve(n)
	print('numero primi: ', len(primes_calculated))
	if reduction_factor > 1:
		primes_before_n = [x for i, x in enumerate(primes_calculated) if i % reduction_factor == 0]
	else:
		primes_before_n = primes_calculated
	n_primes = len(primes_before_n)
	print(primes_before_n)
	print('reducted values: ', n_primes)
	print('computing positions ... ')
	x, y, colors = calculate_prime_paths(primes_before_n)
	print('positions computed!')

	if annotations:
		step_annotations = n_primes**(1/n_annotations)
		set_annotations = [0]
		index_annotation = 1
		while index_annotation <= n_primes:
			set_annotations.append(int(index_annotation))
			index_annotation = index_annotation * step_annotations
			print(index_annotation)
			time.sleep(0)
		print('N annotations: ', len(set_annotations))
		set_annotations = sorted(list(set(set_annotations)))
		print('N annotations: ', len(set_annotations))
	for pp in range(power*15-1, power*15):
		fig, ax1 = plt.subplots()
		ax1.set_aspect('equal')
		if plot_prime_numbers:
			ax1.scatter(x, y, s=3, color=colors)
		if plot_horizon:		# disegna orizzonte degli eventi
			h = s/(1-1/visualization_factor)
			o_x, o_y = [0, h], [h, 0]
			ax1.plot(o_x, o_y)
		if annotations:
			for i in set_annotations:
				plt.annotate(primes_before_n[i], (x[i], y[i]), size=8)
		if plot_exp_lines:
			for k in range(pp):
				f = 1/visualization_factor
				h = s*(1 - f**k)/(1 - f)
				o_x, o_y = [0, h], [h, 0]
				ax1.plot(o_x, o_y, linestyle='--')
		plt.show()


