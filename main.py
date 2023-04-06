def convert_base(num, from_base, to_base):
	digits = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
	base_10_num = 0

	for i, digit in enumerate(num[::-1]):
		if digit.isdigit():
			base_10_num += int(digit) * (from_base ** i)
		else:
			base_10_num += (ord(digit.upper()) - 55) * (from_base ** i)

	new_num = ''
	while base_10_num >= to_base:
		remainder = base_10_num % to_base
		if remainder >= 10:
			new_num += digits[remainder]
		else:
			new_num += str(remainder)
		base_10_num //= to_base
	if base_10_num >= 10:
		new_num += digits[base_10_num]
	else:
		new_num += str(base_10_num)
	return new_num[::-1]


def input_base():
	while True:
		base = input()
		if base.isdigit():
			base = int(base)
			if 2 <= base <= 16:
				return base
		print('Введите число от 2 до 16 включительно')


def input_number():
	while True:
		number = input()
		if number.isdigit():
			return number
		print('Введите любое целое число')


print('Добро пожаловать в калькулятор систем счисления')
while True:
	print('Введите систему счисления (от 2 до 16):')
	base0 = input_base()
	print('Введите конвертируемое число:')
	number = input_number()
	print('Введите систему счисления, в которую будем конвертировать число (от 2 до 16):')
	base1 = input_base()
	converted_number = convert_base(number, base0, base1)
	print(f'Число {number} в {base0}-ной системе счисления это число {converted_number} в {base1}-ной системе счисления')
	print('Нужно ещё сконвертировать число? (да/нет)')
	if input().startswith('н'):
		break
print('Ещё увидимся!')