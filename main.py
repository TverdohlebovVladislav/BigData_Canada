# import numpy as np
# import pandas as pd
# from pandas.io.excel import ExcelWriter
# import os
# import matplotlib.pyplot as plt

from data_generate_scripts import TableProductBase
# import _1_product as prod
from data_generate_scripts import customer as cust
from data_generate_scripts import product_instance as prod_inst
from data_generate_scripts import costed_event as cost_ev
from data_generate_scripts import charge as charge
from data_generate_scripts import payment

def main():

    # Don't change the order!
    cust.Customer().save_to_csv()
    prod_inst.ProductInstance().save_to_csv() 
    cost_ev.CostedEvent().save_to_csv() 
    charge.Charge().save_to_csv()
    payment.Payment().save_to_csv()
    

    # for table in tables:
    #     table.save_to_csv()
    
main()