import numpy as np
import pandas as pd

from data_generate_scripts.TableProductBase import TableProductBase

class CostedEvent(TableProductBase):

    def __init__(self):
        self.dataFrame = self.get_df()

    def get_df(self) -> pd.DataFrame:
        # For generate data
        event_types = ['call', 'sms', 'data']
        direction_variations = ['incoming', 'outgoing']

        # ---
        # Generation columns for dataset 
        event_id_PK: list  = [i for i in range(1, self.max_count_costed_event)] 
        product_instance_id_FK_from_ce: list  = np.random.randint(1, self.max_count_product_inst, size=self.max_count_costed_event - 1)

        # From
        calling_msisdn: list = np.random.randint(1, self.max_count_customer, size=self.max_count_costed_event - 1)

        # To
        called_msisdn = []
        for i in range(len(calling_msisdn)):
            called_msisdn_el = np.random.randint(1, self.max_count_customer)
            while i == called_msisdn:
                called_msisdn_el = np.random.randint(1, self.max_count_customer)
            called_msisdn.append(called_msisdn_el)

        # Event type
        event_type = np.random.choice(event_types, size=self.max_count_costed_event-1, p=[0.6, 0.15, 0.25])

        # Direction
        direction = np.random.choice(direction_variations, size=self.max_count_costed_event-1)

        # Roaming
        roaming = np.random.choice([0, 1], size=self.max_count_costed_event-1, p=[0.7, 0.3])

        # Duration of call
        duration = []
        for i in range(len(event_type)):
            # if is CALL
            if event_type[i] == event_types[0]:
                duration.append(np.random.randint(1, 1800))
            else: 
                duration.append(np.NaN)

        # Number_of_sms
        max_lenght_sms = 150                # Max simb in one sms
        simbols = np.random.normal(loc=90, scale=2.5, size=800)
        number_of_sms = []
        for i in range(self.max_count_costed_event - 1):
            rand_simb = np.random.choice(simbols)
            # If is SMS
            if event_type[i] == event_types[1]:
                if rand_simb > max_lenght_sms:
                    number_of_sms_el = int(rand_simb // 150 + 1)
                else:
                    number_of_sms_el = 1
                number_of_sms.append(number_of_sms_el)
            else:
                number_of_sms.append(np.NaN)

        # Date 
        # 1. Сгенерировать диапазон дат по каждлму дню недели
        # 2. Слить в один список [mondeys, tusdays, ..] и генерить для каждой записи таблицы по вероятностям [0.4, 0.7,  ...]
        # 3. Внутри цикла вытягивать из массивов дней недели рандомную дату 
        # 4. Сохранять эту рандомную дату в массив Date
        # 5. Еще раз пробежаться по массиву дат и приплести для каждой даты время из вспомогательного кода Романа
        date = []

        # Number of data (instead of total value)
        number_of_data = []
        for i in range(len(event_type)):
            # if is DATA
            if event_type[i] == event_types[2]:
                number_of_data.append(np.random.randint(500, 5000))
            else: 
                number_of_data.append(np.NaN)

        # Cost
        cost = []
        # for i in range(len(event_type)):

        #     # if is CALL
        #     if event_type[i] == event_types[0]:
        #         pr_inst = product_instance_id_FK_from_ce[i]
        #         number_of_data.append(np.random.randint(500, 5000))

        #     # if is SMS
        #     if event_type[i] == event_types[1]:
        #         number_of_data.append(np.random.randint(500, 5000))

        #     # if is DATA
        #     if event_type[i] == event_types[2]:
        #         number_of_data.append(np.random.randint(500, 5000))
        #     else: 
        #         number_of_data.append(np.NaN)


        Costed_eventDf = pd.DataFrame(
            {
                "event_id_PK": pd.Series(event_id_PK, name="event_id_PK", dtype="int"),
                "product_instance_id_FK": pd.Series(product_instance_id_FK_from_ce, name="product_instance_id_FK", dtype="int"),
                
                "calling_msisdn": pd.Series(calling_msisdn, name="calling_msisdn", dtype="int"),
                "called_msisdn": pd.Series(called_msisdn, name="called_msisdn", dtype="int"),

                # "date": [1, 2, 3, 4, 5],
                # "cost": [1, 2, 3, 4, 5],
                "duration": pd.Series(duration, name="duration", dtype=pd.Int64Dtype()),
                "number_of_sms": pd.Series(number_of_sms, name="number_of_sms", dtype=pd.Int64Dtype()),
                "number_of_data": pd.Series(number_of_data, name="number_of_data", dtype=pd.Int64Dtype()),
                "event_type": pd.Series(event_type, name="event_type", dtype="str"),
                "direction": pd.Series(direction, name="direction", dtype="str"),
                "roaming": pd.Series(roaming, name="roaming", dtype="int"),
                
                # Add other columns here...
            }
        )
        Costed_eventDf.set_index('event_id_PK', inplace=True)
        return Costed_eventDf

    