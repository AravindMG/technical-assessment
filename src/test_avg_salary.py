from avg_salary import *
import pytest
import pandas as pd


# test cases
def test_filter_necessary_cols():
    test_df = {
        "userId": ['rirani', 'rirani', 'rirani', 'rirani', 'rirani', 'rirani', 'rirani', 'rirani', 'rirani', 'rirani'],
        "jobTitleName": ['Developer', 'Developer', 'Program Directory', 'ProductOwner', 'ProductOwner', 'Developer',
                         'Developer', 'ProductOwner', 'ProductOwner', 'ProductOwner'],
        "region": ['CA', 'CA', 'CA', 'SA', 'SA', 'FA', 'YA', 'SA', 'YA', 'CA'],
        "salary": ['20000', '30000', '15000', '45000', '25000', '10000', '20000', '25000', '17000', '2000']
    }
    actual_df = pd.DataFrame(test_df, columns=['userId', 'jobTitleName', 'region', 'salary'])

    actual = filter_necessary_cols(actual_df)

    test_df_2 = {
        "jobTitleName": ['Developer', 'Developer', 'Program Directory', 'ProductOwner', 'ProductOwner', 'Developer',
                         'Developer', 'ProductOwner', 'ProductOwner', 'ProductOwner'],
        "region": ['CA', 'CA', 'CA', 'SA', 'SA', 'FA', 'YA', 'SA', 'YA', 'CA'],
        "salary": ['20000', '30000', '15000', '45000', '25000', '10000', '20000', '25000', '17000', '2000']
    }
    expected = pd.DataFrame(test_df_2, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')

    # assertion

    pd.testing.assert_frame_equal(actual, expected)
