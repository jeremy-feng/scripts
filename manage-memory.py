import numpy as np
import pandas as pd

# from line_profiler import profile
from memory_profiler import profile

np.random.seed(0)

class TestMemory:
    def __init__(self):
        dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
        items_data1 = list(range(1, 501))
        items_data2 = list(range(201, 1001))

        index_data2 = pd.MultiIndex.from_product(
            [dates, items_data2], names=["date", "item"]
        )

        self.data_1 = pd.DataFrame(
            np.random.rand(len(dates), 500), index=dates, columns=items_data1
        )
        self.data_1.index.name = "date"
        self.data_2 = pd.DataFrame(
            np.random.rand(len(index_data2), 800),
            index=index_data2,
            columns=items_data2,
        )

    @profile
    def multiply_and_sum_data_pd(self):
        result = (self.data_1 * self.data_2).sum(axis=1)
        return result

    @profile
    def multiply_and_sum_data_np(self):
        index = self.data_2.index
        columns = self.data_2.columns
        self.data_2 = self.data_2.to_numpy().reshape(
            index.get_level_values("date").nunique(),
            index.get_level_values("item").nunique(),
            -1,
        )
        result = pd.Series(
            np.nansum(
                np.vstack(
                    (self.data_1.reindex(columns=columns).to_numpy()[:, np.newaxis, :])
                    * self.data_2
                ),
                axis=1,
            ),
            index=index,
        )
        return result

test_memory = TestMemory()
print(test_memory.multiply_and_sum_data_pd())
print(test_memory.multiply_and_sum_data_np())
