import numpy as np
import pandas as pd

from data_generate_scripts.TableProductBase import TableProductBase

class Charge(TableProductBase):

    def __init__(self):
        self.dataFrame = self.get_df()

    def get_df(self) -> pd.DataFrame:
        charge_id_PK: list  = [i for i in range(1, self.max_count_costed_charge)] 
        product_instance_id_FK_charge: list   = np.random.randint(8, self.max_count_product_inst + 1, size=self.max_count_costed_charge - 1)
        
        # ––––––––––––––––– charge_counter ––––––––––––––––––
        charge_counter = []
        for i in range(len(product_instance_id_FK_charge)):
            # We count and add to the charge_counter list the number of times the current element occurs
            charge_counter.append(np.count_nonzero(product_instance_id_FK_charge[:i] == product_instance_id_FK_charge[i]) + 1)

        # –––––––––––––––––––––– Date ––––––––––––––––––––––
        import datetime
        import random


        def random_date(start, end):
            """Generate a random datetime between `start` and `end`"""
            return start + datetime.timedelta(
                # Get a random amount of seconds between `start` and `end`
                seconds=random.randint(0, int((end - start).total_seconds())))

        date = []
        d1 = datetime.date(2020, 1, 1)
        d2 = datetime.date(2021, 12, 31)

        for i in range(len(product_instance_id_FK_charge)):
            rnd = random_date(d1, d2)
            date.append(rnd.strftime("%d/%m/%Y").replace('/', '.'))

        date.sort(key=lambda lst: (lst[-1], lst[2:5], lst[0:2]))
        
        # –––––––––––––––––––––– cost ––––––––––––––––––––––
        cost = []
        with open("data_source/Product.csv") as Product:
            ProductDf = pd.read_csv(Product, delimiter=',')
            for i in product_instance_id_FK_charge:
                cost.append(ProductDf['Price'][i - 1])

        # –––––––––––––––––– event_type ––––––––––––––––––––
        event_type = [True if i < 13 else False for i in product_instance_id_FK_charge]
        
        ChargeDf = pd.DataFrame(
            {
                "charge_id_PK": pd.Series(charge_id_PK, name="charge_id_PK", dtype="int"),
                "product_instance_id_FK": pd.Series(product_instance_id_FK_charge, name="product_instance_id_FK", dtype="int"),
                "charge_counter": pd.Series(charge_counter, name="charge_counter", dtype="int"),
                "date": pd.Series(date, name="date", dtype="str"),
                "cost": pd.Series(cost, name="cost", dtype="int"),
                "event_type": pd.Series(event_type, name="event_type", dtype="bool")
                # Add other columns here...
            }
        )
        
        ChargeDf.set_index('charge_id_PK', inplace=True)
        return ChargeDf
