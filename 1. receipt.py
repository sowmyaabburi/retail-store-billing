reatil_store={"total_cost":float(),"items":list(),"grand_total":float()}
def inputs():
    while True:
        price=input("Enter the next item cost... ")
        price=float(price)
        yield price
        process=input("Please type yes to continue or No to exit... ").lower()
        if process!="yes":
            break

iterator_obj=inputs()
for obj in iterator_obj:
    reatil_store["total_cost"]+=obj
    reatil_store['items'].append(obj)
after_zero_values=reatil_store["items"]
discount_for_items=(sum(after_zero_values)*5)/100
govt_tax=(6.5*sum(after_zero_values))/100
if len(after_zero_values)>=5:
    reatil_store["grand_total"]=sum(after_zero_values)+govt_tax
else:
    reatil_store["grand_total"]=sum(after_zero_values)-discount_for_items+govt_tax
print("Number of items: "+str(len(reatil_store["items"])))
print(f"Discount eligible items: "+str(len(after_zero_values)))
print(f"Subtotal: ",sum(after_zero_values))
print(f"Discount: ",discount_for_items)
print(f"Tax : ",govt_tax)
print(f"Grand Total : ",reatil_store["grand_total"])
