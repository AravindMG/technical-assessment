from avg_salary import *
import pytest
import pandas as pd


@pytest.fixture()
def original_df():
    test_df = {
        "userId": ['rirani', 'nirani', 'thanks', 'catherine', 'Ben', 'sarah', 'james', 'liam', 'jen', 'roar'],
        "jobTitleName": ['Developer', 'Developer', 'Program Directory', 'ProductOwner', 'ProductOwner', 'Developer',
                         'Developer', 'ProductOwner', 'ProductOwner', 'ProductOwner'],
        "firstName": ['Romin', 'Neil', 'Tom', 'Catherine', 'Ben', 'Sarah',
                      'James', 'Liam', 'Jenifer', 'Pat'],
        "lastName": ['Irani', 'Irani', 'Hanks', 'Blank', 'Geller', 'Poland',
                     'Waters', 'Brass', 'Fold', 'Roam'],
        "preferredFullName": ['Romin Irani', 'Neil Irani', 'Tom Hanks', 'Catherine Blank', 'Ben Geller',
                              'Sarah Polland',
                              'James Waters', 'Liam Brass', 'Jenifer Fold', 'Pat Roam'],
        "employeeCode": ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10'],
        "region": ['CA', 'CA', 'CA', 'SA', 'SA', 'FA', 'YA', 'SA', 'YA', 'CA'],
        "phoneNumber": ['408-1234567', '408-1111111', '408-2222222', '408-23333322', '402-125867322', '402-125867653',
                        '502-1276543653', '602-1111117322', '602-111000074343', '408-1545634511'],
        "emailAddress": ['CA', 'CA', 'CA', 'SA', 'SA', 'FA', 'YA', 'SA', 'YA', 'CA'],
        "salary": ['20000', '30000', '15000', '45000', '25000', '10000', '20000', '25000', '17000', '2000']
    }
    actual_df = pd.DataFrame(test_df, columns=['userId', 'jobTitleName', 'region', 'salary'])
    return actual_df


@pytest.fixture()
def filtered_df():
    test_df_2 = {
        "jobTitleName": ['Developer', 'Developer', 'Program Directory', 'ProductOwner', 'ProductOwner', 'Developer',
                         'Developer', 'ProductOwner', 'ProductOwner', 'ProductOwner'],
        "region": ['CA', 'CA', 'CA', 'SA', 'SA', 'FA', 'YA', 'SA', 'YA', 'CA'],
        "salary": ['20000', '30000', '15000', '45000', '25000', '10000', '20000', '25000', '17000', '2000']
    }
    expected = pd.DataFrame(test_df_2, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    return expected


# test cases

# In this test case we are checking whether we have filtered all the necessary columns needed to generate our output
# Also, this test case checks whether the actual and expected dataframes have similar dtypes

def test_filter_necessary_cols(original_df, filtered_df):
    actual = filter_necessary_cols(original_df)
    pd.testing.assert_frame_equal(actual, filtered_df)


# In this test case we are checking whether we have filtered developer's from CA region
def test_filter_dev_CA(filtered_df):
    actual = filter_dev_CA(filtered_df)

    dev_CA_df = {
        "jobTitleName": ['Developer', 'Developer'],
        "region": ['CA', 'CA'],
        "salary": ['20000', '30000']
    }

    expected = pd.DataFrame(dev_CA_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual, expected)


# In this test case we are checking whether we are calculating and printing the correct average salary of developer's from CA region
def test_avg_sal_CA():
    dev_CA_df = {
        "jobTitleName": ['Developer', 'Developer'],
        "region": ['CA', 'CA'],
        "salary": ['20000', '30000']
    }
    test_df = pd.DataFrame(dev_CA_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_dev_CA(test_df)

    expected = "In 'CA' region the average salary of a 'Developer' is 25000.0\n"

    assert actual == expected


# In this test case we are checking whether we have filtered developer's from FA region
def test_filter_dev_FA(filtered_df):
    actual = filter_dev_FA(filtered_df)

    dev_FA_df = {
        "jobTitleName": ['Developer'],
        "region": ['FA'],
        "salary": ['10000']
    }

    expected = pd.DataFrame(dev_FA_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))
    # print("----Actual----")
    # print(actual)
    # print("----Expected----")
    # print(expected)


# In this test case we are checking whether we are calculating and printing the correct average salary of developer's from FA region
def test_avg_sal_FA():
    dev_FA_df = {
        "jobTitleName": ['Developer'],
        "region": ['FA'],
        "salary": ['10000']
    }
    test_df = pd.DataFrame(dev_FA_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_dev_FA(test_df)

    expected = "In 'FA' region the average salary of a 'Developer' is 10000.0\n"

    assert actual == expected


# In this test case we are checking whether we have filtered developer's from YA region
def test_filter_dev_YA(filtered_df):
    actual = filter_dev_YA(filtered_df)

    dev_YA_df = {
        "jobTitleName": ['Developer'],
        "region": ['YA'],
        "salary": ['20000']
    }

    expected = pd.DataFrame(dev_YA_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))


# In this test case we are checking whether we are calculating and printing the correct average salary of developer's from YA region
def test_avg_sal_YA():
    dev_YA_df = {
        "jobTitleName": ['Developer'],
        "region": ['YA'],
        "salary": ['20000']
    }
    test_df = pd.DataFrame(dev_YA_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_dev_YA(test_df)

    expected = "In 'YA' region the average salary of a 'Developer' is 20000.0\n"

    assert actual == expected
