import numpy as np
import pandas as pd

from data_generate_scripts.TableProductBase import TableProductBase

class Charge(TableProductBase):

    def __init__(self):
        self.dataFrame = self.get_df()

    def get_df(self) -> pd.DataFrame:
        charge_id_PK: list  = [i for i in range(1, self.max_count_costed_charge)] 
        product_instance_id_FK_charge: list   = np.random.randint(1, self.max_count_product_inst, size=self.max_count_costed_charge - 1)
        ChargeDf = pd.DataFrame(
            {
                "charge_id_PK": pd.Series(charge_id_PK, name="charge_id_PK", dtype="int"),
                "product_instance_id_FK": pd.Series(product_instance_id_FK_charge, name="product_instance_id_FK", dtype="int"),
                # Add other columns here...
            }
        )
        ChargeDf.set_index('charge_id_PK', inplace=True)
        return ChargeDf
