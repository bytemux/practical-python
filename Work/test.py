height = 100.0
bounce_factor = 0.6
bounce_times = 10

while bounce_times > 0:
  height = height * bounce_factor
  bounce_times -= 1
  print(bounce_times, ' ', round(height, 4))
