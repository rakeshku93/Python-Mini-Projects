
# def boxPrint(symbol, width, height):
#     """In this code we're raising our own exceptions uisng raise keyword"""
#     print("--")
#     print(f"Creating Pattern with: {symbol=} {width=} {height=}")
    
#     if len(symbol) != 1:
#         raise Exception("Symbol must be a single character string.")
    
#     if width <= 2:
#         raise Exception("Width must be greater than 2")
    
#     if height <= 2:
#         raise Exception("Height must be greater than 2")
    
    
#     print(symbol*width)
#     for i in range(height-2):
#         print(symbol + (" " *(width-2)) + symbol)
#     print(symbol*width)
    

# if __name__ == "__main__":
    
#     for sym, w, h in (('*', 4, 4), ('x', 1, 3), ('O', 20, 5), ('ZZ', 3, 3)):
#         try:
#             boxPrint(sym, w, h)
            
#         except Exception as e:
#             print("An Error occured: ", str(e))
    
    
# # Note: try and except handles errors gracefully. 
# # Even when code fails for one set of (symbol, w, h); it raises error and runs for other parameters. 
# # But, this is not the case with `assert` keyword. If `assert` fails, it crash the program.

finalized_cols = ['units_lag06', 
                  'units_lag07', 
                  'units_lag08', 
                  'units_lag09', 
                  'emb0',
                  'emb1',
                  'emb2',
                  'emb3',
                  'emb4', 
                  'emb5', 
                  'emb6',
                  'emb7',
                  'emb8', 
                  'emb9',
                  'emb10',
                  'emb11',
                  'emb12',
                  'emb13', 'emb14', 'emb15', 'emb16', 'emb17',
       'emb18', 'emb19', 'emb20', 'emb21', 'emb22', 'emb23', 'emb24', 'emb25',
       'emb26', 'emb27', 'emb28', 'emb29', 'emb30', 'emb31', 'emb32', 'emb33',
       'emb34', 'Year_2016', 'Year_2017', 'Year_2018', 'Year_2019',
       'Year_2020', 'Year_2021', 'Year_2022', 'Month_Of_Year_1',
       'Month_Of_Year_2', 'Month_Of_Year_3', 'Month_Of_Year_4',
       'Month_Of_Year_5', 'Month_Of_Year_6', 'Month_Of_Year_7',
       'Month_Of_Year_8', 'Month_Of_Year_9', 'Month_Of_Year_10',
       'Month_Of_Year_11', 'Month_Of_Year_12', 'holiday_count_0',
       'holiday_count_1', 'holiday_count_2', 'holiday_count_3', 'half_0',
       'half_1', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4',
       'week_of_month_1', 'week_of_month_2', 'week_of_month_3',
       'week_of_month_4', 'week_of_month_5', 'week_of_month_6'
       ]