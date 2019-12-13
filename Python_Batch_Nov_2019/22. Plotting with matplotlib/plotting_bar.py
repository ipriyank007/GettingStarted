from matplotlib import pyplot as plt

width = 0.25
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

frontend_salaries_y = [15000, 18000, 19500, 26000, 28000, 30000, 36000, 45000, 60000, 84000, 100000]
backend_salaries_y = [5000, 8000, 9500, 16000, 38000, 40000, 46000, 65000, 90000, 114000, 140000]
plt.title('Average salaries per age')
plt.xlabel('Ages')
plt.ylabel('Average Salaries in rupees')

plt.xticks([i - width/2 for i in range(1, len(ages_x)+1)], ages_x)

plt.bar([i - width/2 for i in range(1, len(ages_x)+1)], backend_salaries_y, width=width, label="Backend Devs")

plt.bar([i + width/2 for i in range(1, len(ages_x) + 1)], frontend_salaries_y, width=width, label="Frontend Devs")

plt.legend()
plt.show()