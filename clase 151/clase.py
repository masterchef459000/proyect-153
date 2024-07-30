
month = ("enero" , "febrero" , "marzo" , "abril" , "mayo" , "junio" , "julio" , "agosto ", "septiembre" , "octubre" , "noviembre" , "diciembre")

profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,9000)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("la ganancia maxima de" + str (max_profit)+ "se registro en el mes de " + str(max_profit_month))



min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("la ganancia maxima de" + str (min_profit)+ "se registro en el mes de " + str(min_profit_month))
