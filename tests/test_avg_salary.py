from src.avg_salary import *
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
def test_filter_dev_ca(filtered_df):
    actual = filter_dev_ca(filtered_df)

    dev_ca_df = {
        "jobTitleName": ['Developer', 'Developer'],
        "region": ['CA', 'CA'],
        "salary": ['20000', '30000']
    }

    expected = pd.DataFrame(dev_ca_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual, expected)


# In this test case we are checking whether we are calculating and printing the correct average salary of developer's from CA region
def test_dev_avg_sal_ca():
    dev_ca_df = {
        "jobTitleName": ['Developer', 'Developer'],
        "region": ['CA', 'CA'],
        "salary": ['20000', '30000']
    }
    test_df = pd.DataFrame(dev_ca_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_dev_ca(test_df)

    expected = "In 'CA' region the average salary of a 'Developer' is 25000.0\n"

    assert actual == expected


# In this test case we are checking whether we have filtered developer's from FA region
def test_filter_dev_fa(filtered_df):
    actual = filter_dev_fa(filtered_df)

    dev_fa_df = {
        "jobTitleName": ['Developer'],
        "region": ['FA'],
        "salary": ['10000']
    }

    expected = pd.DataFrame(dev_fa_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))


# In this test case we are checking whether we are calculating and printing the correct average salary of developer's from FA region
def test_dev_avg_sal_fa():
    dev_fa_df = {
        "jobTitleName": ['Developer'],
        "region": ['FA'],
        "salary": ['10000']
    }
    test_df = pd.DataFrame(dev_fa_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_dev_fa(test_df)

    expected = "In 'FA' region the average salary of a 'Developer' is 10000.0\n"

    assert actual == expected


# In this test case we are checking whether we have filtered developer's from YA region
def test_filter_dev_ya(filtered_df):
    actual = filter_dev_ya(filtered_df)

    dev_ya_df = {
        "jobTitleName": ['Developer'],
        "region": ['YA'],
        "salary": ['20000']
    }

    expected = pd.DataFrame(dev_ya_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))


# In this test case we are checking whether we are calculating and printing the correct average salary of developer's from YA region
def test_dev_avg_sal_ya():
    dev_ya_df = {
        "jobTitleName": ['Developer'],
        "region": ['YA'],
        "salary": ['20000']
    }
    test_df = pd.DataFrame(dev_ya_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_dev_ya(test_df)

    expected = "In 'YA' region the average salary of a 'Developer' is 20000.0\n"

    assert actual == expected


# In this test case we are checking whether we have filtered program directory from CA region, also program directory is only in CA region
def test_filter_prog_dir_ca(filtered_df):
    actual = filter_prog_dir_ca(filtered_df)

    prog_dir_ca_df = {
        "jobTitleName": ['Program Directory'],
        "region": ['CA'],
        "salary": ['15000']
    }

    expected = pd.DataFrame(prog_dir_ca_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))


# In this test case we are checking whether we are calculating and printing the correct average salary of program directory from CA region
def test_prog_dir_avg_sal_ca():
    prog_dir_ca_df = {
        "jobTitleName": ['Program Directory'],
        "region": ['CA'],
        "salary": ['15000']
    }
    test_df = pd.DataFrame(prog_dir_ca_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_prog_dir_ca(test_df)

    expected = "In 'CA' region the average salary of a 'Program Directory' is 15000.0\n"

    assert actual == expected


# In this test case we are checking whether we have filtered productOwner's from CA region
def test_filter_prod_own_ca(filtered_df):
    actual = filter_prod_own_ca(filtered_df)

    prod_own_ca_df = {
        "jobTitleName": ['ProductOwner'],
        "region": ['CA'],
        "salary": ['2000']
    }

    expected = pd.DataFrame(prod_own_ca_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))


# In this test case we are checking whether we are calculating and printing the correct average salary of program directory from CA region
def test_prod_own_avg_sal_ca():
    prod_own_ca_df = {
        "jobTitleName": ['ProductOwner'],
        "region": ['CA'],
        "salary": ['2000']
    }
    test_df = pd.DataFrame(prod_own_ca_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_prod_own_ca(test_df)

    expected = "In 'CA' region the average salary of a 'ProductOwner' is 2000.0\n"

    assert actual == expected


# In this test case we are checking whether we have filtered productOwner's from SA region
def test_filter_prod_own_sa(filtered_df):
    actual = filter_prod_own_sa(filtered_df)

    prod_own_sa_df = {
        "jobTitleName": ['ProductOwner', 'ProductOwner', 'ProductOwner'],
        "region": ['SA', 'SA', 'SA'],
        "salary": ['45000', '25000', '25000']
    }

    expected = pd.DataFrame(prod_own_sa_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))


# In this test case we are checking whether we are calculating and printing the correct average salary of program directory from SA region
def test_prod_own_avg_sal_sa():
    prod_own_sa_df = {
        "jobTitleName": ['ProductOwner', 'ProductOwner', 'ProductOwner'],
        "region": ['SA', 'SA', 'SA'],
        "salary": ['45000', '25000', '25000']
    }
    test_df = pd.DataFrame(prod_own_sa_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_prod_own_sa(test_df)

    expected = "In 'SA' region the average salary of a 'ProductOwner' is 31666.666666666668\n"

    assert actual == expected


# In this test case we are checking whether we have filtered productOwner's from SA region
def test_filter_prod_own_ya(filtered_df):
    actual = filter_prod_own_ya(filtered_df)

    prod_own_ya_df = {
        "jobTitleName": ['ProductOwner'],
        "region": ['YA'],
        "salary": ['17000']
    }

    expected = pd.DataFrame(prod_own_ya_df, columns=['jobTitleName', 'region', 'salary'])
    expected['salary'] = expected['salary'].astype('int')
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected.reset_index(drop=True))


# In this test case we are checking whether we are calculating and printing the correct average salary of program directory from YA region
def test_prod_own_avg_sal_ya():
    prod_own_ya_df = {
        "jobTitleName": ['ProductOwner'],
        "region": ['YA'],
        "salary": ['17000']
    }
    test_df = pd.DataFrame(prod_own_ya_df, columns=['jobTitleName', 'region', 'salary'])
    test_df['salary'] = test_df['salary'].astype('int')

    actual = avg_sal_prod_own_ya(test_df)

    expected = "In 'YA' region the average salary of a 'ProductOwner' is 17000.0\n"

    assert actual == expected


# def test_writetofile(tmpdir):
#     file = tmpdir.join('../outputs//output.txt')
#     write_to_out()
#     assert file.read() == "In 'CA' region the average salary of a 'Developer' is 25000.0"
