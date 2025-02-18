tomato_yield = [0.30 * 10, 0.70 * 12]  
potato_yield = 10 
cabbage_yield = 14  
sunflower_yield = 0.7  
sugarcane_yield = 45 

tomato_price_per_kg = 7
potato_price_per_kg = 20
cabbage_price_per_kg = 24
sunflower_price_per_kg = 200
sugarcane_price_per_kg = 4000

tomato_sales=((tomato_yield[0]*16*1000)+(tomato_yield[1]*16*1000))*tomato_price_per_kg
cabbage_sales=(cabbage_yield*16*1000)*cabbage_price_per_kg
potato_sales=(potato_yield*16*1000)*potato_price_per_kg
sunflower_sales=(sunflower_yield*16*1000)*sunflower_price_per_kg
sugarcane_sales=(sugarcane_yield*16*1000)*sugarcane_price_per_kg

overall_sales=tomato_sales+potato_sales+cabbage_sales+sunflower_sales+sugarcane_sales
print("The overall sales achieved by Mahesh from the 80 acres of land :",overall_sales)

chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales 
print("Sales realisation from chemical-free farming at the end of 11 months :",chemical_free_sales)