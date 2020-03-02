names = ["Akira", "Emmery", "Dia", "Erick", "Nadja"]
ages = [14, 16, 17, 14, 18, 15]

for i in range(6):
  print("Information about " + names[i] + ":")
  print("Age: " + str(ages[i]))
  print("Age in dog years: " + str(ages[i] * 7))
  print("----------------------------------------")