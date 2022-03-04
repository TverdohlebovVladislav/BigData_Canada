import numpy as np
import pandas as pd

from data_generate_scripts.TableProductBase import TableProductBase

class Customer(TableProductBase):

    def __init__(self):
        self.dataFrame = self.get_df()

    def get_df(self) -> pd.DataFrame:
        customer_id_PK: list = [i for i in range(1, self.max_count_customer)]
        CustomerDf = pd.DataFrame(
            {
                "customer_id": pd.Series(customer_id_PK, name="customer_id", dtype="int"),
                # Add other columns here...
            }
        )
        CustomerDf.set_index('customer_id', inplace=True)
        return CustomerDf
    