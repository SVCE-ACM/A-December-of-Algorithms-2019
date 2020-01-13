def sevenish(n):
  last_power_index = 0
  add_index = 0
  mem = [1] * n

  for i in range(1, n):
    if add_index == last_power_index:
      add_index = 0
      mem[i] = mem[last_power_index] * 7
      last_power_index = i
    else:
      mem[i] = mem[last_power_index] + mem[add_index]
      add_index += 1

  x = mem[n-1]
  print(x)

sevenish(6)