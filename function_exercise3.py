#Order Invoice Generator
#Cover Concepts of *args & **kwargs



def generate_invoice(customer_name="Guest",*items,**charges):

    total = 0.0

    invoice_line = [f"\nInvoice for :{customer_name}"]

    if items:
        invoice_line.append("\nItems:")
        for item in items:
            invoice_line.append(f"-{item}")

            
    
    if charges:
        invoice_line.append("\nCharges:")
        for label,amount in charges.items():
            invoice_line.append(f"{label.capitalize()}:{amount}")
            total +=amount
        
    invoice_line.append(f"\nTotal amount due:{total}\n")
    return "\n".join(invoice_line)


print(generate_invoice("Riya","pizza","vadapav",tax=20,service=29))
    

