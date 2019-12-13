from matplotlib import pyplot as plt

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

frontend_salaries_y = [15000, 18000, 19500, 26000, 28000, 30000, 36000, 45000, 60000, 84000, 100000]
backend_salaries_y = [5000, 8000, 9500, 16000, 38000, 40000, 46000, 65000, 90000, 114000, 140000]
plt.title('Average salaries per age')
plt.xlabel('Ages')
plt.ylabel('Average Salaries in rupees')
plt.plot(ages_x, frontend_salaries_y, label="frontend developers")
plt.plot(ages_x, backend_salaries_y, label='backtend developers')
plt.legend()
plt.show()