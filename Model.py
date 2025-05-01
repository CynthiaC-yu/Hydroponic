"""
This script defines a function for drawing a diagram by using PyGMT library.

Functions:
- test_draw_diagram(value_type, cal_start1, cal_end1, pot_id): Draws a diagram based on the specified value type,
  start and end dates, and pot ID. It queries data from the database, processes it, and generates a diagram using PyGMT.

Dependencies:
- dbMethods: Module containing database query methods.
- pandas (pd): Library for data manipulation and analysis.
- numpy (np): Library for numerical computing.
- pygmt: Python interface for the Generic Mapping Tools (GMT).

Args:
- value_type: Type of value to plot.
- cal_start1: Start date for data retrieval.
- cal_end1: End date for data retrieval.
- pot_id: ID of the pot for which data is retrieved.

Returns:
- The diagram is displayed using PyGMT.
"""

from databaseOperations import dbMethods
import pandas as pd
import numpy as np
import pygmt

def test_draw_diagram(value_type, cal_start1, cal_end1, pot_id):
    """Draws a diagram using PyGMT."""
    print("Start:", cal_start1)
    print("End:", cal_end1)
    print("Value Type:", value_type)
    print("Pot ID:", pot_id)

    # Query data from the database
    value_row = dbMethods.query_data_between_two_dates('HydroponicDB.db', 'pot', value_type, cal_start1, cal_end1, pot_id)
    date_row = dbMethods.get_date_between_two_dates('HydroponicDB.db', 'pot', cal_start1, cal_end1, pot_id)

    # Extract data from tuples
    value_row_list = [i[0] for i in value_row]
    date_row_list = [i[0] for i in date_row]

    # Extract date and datetime components
    date_only_row_list = [date[:10] for date in date_row_list]
    datetime_only_row_list = [date[:16] for date in date_row_list]

    # Find the maximum y-value for graph range
    value_float_list = pd.array(value_row_list, dtype=np.float32)
    y_range = max(value_float_list)

    # Merge date and value lists
    def mergeDate(date_only_row_list, value_row_list):
        return [[a] + [str(b)[:10]] for (a, b) in zip(date_only_row_list, value_row_list)]

    def mergeDatetime(datetime_only_row_list, value_row_list):
        return [[a] + [str(b)[:10]] for (a, b) in zip(datetime_only_row_list, value_row_list)]

    # Convert to DataFrame
    data = mergeDatetime(datetime_only_row_list, value_row_list)
    df = pd.DataFrame(data, columns=["Date", "Score"])
    df.Score = pd.array(df["Score"], dtype=np.float32)
    df.Date = pd.to_datetime(df["Date"], format="%Y-%m-%d-%H:%M")

    # Plot using PyGMT
    fig = pygmt.Figure()
    region = pygmt.info(data=df[["Date", "Score"]], per_column=True, spacing=(800, y_range), coltypes="T")

    fig.plot(
        region=region,
        projection="X15c/10c",
        frame=["WSen", "afg","xaf+lTIme Change", "yaf+lValue Change"],
        x=df.Date,
        y=df.Score,
        style="c0.4c",
        pen="1p",
        fill="green3",
    )

    fig.show()
