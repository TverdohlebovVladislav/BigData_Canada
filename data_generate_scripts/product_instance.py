import numpy as np
import pandas as pd
from data_generate_scripts.TableProductBase import TableProductBase

class ProductInstance(TableProductBase):

    def __init__(self):
        self.dataFrame = self.get_df()

    def get_df(self) -> pd.DataFrame:
        product_instance_id_PK: list  = [i for i in range(1, self.max_count_product_inst)]
        customer_id_FK: list  = np.random.randint(1, self.max_count_customer, size=self.max_count_product_inst - 1)
        product_id_FK: list  = np.random.randint(1, self.max_count_product, size=self.max_count_product_inst - 1) 
        Product_instanceDf = pd.DataFrame(
            {
                "product_instance_id_PK": pd.Series(product_instance_id_PK, name="product_instance_id_PK", dtype="int"),
                "customer_id_FK": pd.Series(customer_id_FK, name="customer_id_FK", dtype="int"),
                "product_id_FK": pd.Series(product_id_FK, name="product_id_FK", dtype="int"),
                # Add other columns here...
            }
        )
        Product_instanceDf.set_index('product_instance_id_PK', inplace=True)
        return Product_instanceDf