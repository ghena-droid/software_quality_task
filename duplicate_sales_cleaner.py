sales_records = ["A001", "A002", "A001", "A003", "A002", "A004"]

unique_sales = []

for record in sales_records:

    is_duplicate = False
   
  for record in sales_records[:]:
        
        if record == item:
            
            is_duplicate = True
            
            break
    
    if is_duplicate == False:
        
        unique_sales.append(record)

print("Unique Sales Records:", unique_sales)
