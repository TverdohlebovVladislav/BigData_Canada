import numpy as np
import pandas as pd

from data_generate_scripts.TableProductBase import TableProductBase

class Payment(TableProductBase):

    def __init__(self):
        self.dataFrame = self.get_df()

    def get_df(self) -> pd.DataFrame:
        # For generating data
        payment_methods = ['bank card', 'from terminal', 'from another phone']

        # ---
        # Create dataframe - Payment
        payment_id_PK: list  = [i for i in range(1, self.max_count_costed_payment)]
        customer_id_FK_in_payment: list = np.random.randint(1, self.max_count_customer, size=self.max_count_costed_payment - 1)

        # Payment method
        payment_method = np.random.choice(payment_methods, size=self.max_count_costed_payment-1, p=[0.7, 0.2, 0.1])

        # Amount
        middle = 0
        for i in range(1, self.max_count_product):
            if TableProductBase.get_df()['recurrent'][i] == 'regularly':
                middle += TableProductBase.get_df()['Price'][i]
        middle /= self.max_count_product
        amount_reg = np.random.normal(loc=middle, scale=2.5, size=self.max_count_costed_payment-1)
        amount_once = np.random.choice([0, 10, 15, 20, 50], size=self.max_count_costed_payment-1, p=[0.3, 0.25, 0.3, 0.1, 0.05])
        amount = amount_reg + amount_once

        PaymentDf = pd.DataFrame(
            {
                "payment_id_PK": pd.Series(payment_id_PK, name="payment_id_PK", dtype="int"),
                "customer_id_FK": pd.Series(customer_id_FK_in_payment, name="customer_id_FK", dtype="int"),

                "payment_method": pd.Series(payment_method, name="payment_method", dtype="str"),
                #"date": pd.Series(customer_id_FK_in_payment, name="customer_id_FK", dtype="int"),
                "amount": pd.Series(customer_id_FK_in_payment, name="customer_id_FK", dtype="int"),
            }
        )
        PaymentDf.set_index('payment_id_PK', inplace=True)
        return PaymentDf