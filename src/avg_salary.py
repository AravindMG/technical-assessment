import json
from pandas.io.json import json_normalize


def read_json():
    with open("/Users/aravind/Documents/technical-assessment/resources/sample_data.json") as sample_data:
        data = json.load(sample_data)
        employees = data['Employees']
        df = json_normalize(employees)
        print(df.head(3))
        return df


def filter_necessary_cols(df):
    df_filtered_cols = df[['jobTitleName', 'region', 'salary']]
    df_filtered_cols['salary'] = df_filtered_cols['salary'].replace(',', '', regex=True)
    df_filtered_cols['salary'] = df_filtered_cols['salary'].astype('int')
    # print(df_filtered_cols)
    return df_filtered_cols


# In SA region there are no devs
def filter_dev_CA(df_filtered_cols):
    CA_dev = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Developer') & (df_filtered_cols['region'] == 'CA')]
    # print(CA_dev)
    return CA_dev


def avg_sal_dev_CA(CA_dev):
    mean_salary = CA_dev['salary'].mean()
    print(mean_salary)
    return "In 'CA' region the average salary of a 'Developer' is " + str(mean_salary) + "\n"


def filter_dev_FA(df_filtered_cols):
    FA_dev = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Developer') & (df_filtered_cols['region'] == 'FA')]
    print(FA_dev)
    return FA_dev


def avg_sal_dev_FA(FA_dev):
    mean_salary = FA_dev['salary'].mean()
    return "In 'FA' region the average salary of a 'Developer' is " + str(mean_salary) + "\n"


def filter_dev_YA(df_filtered_cols):
    YA_dev = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Developer') & (df_filtered_cols['region'] == 'YA')]
    print(YA_dev)
    return YA_dev


def avg_sal_dev_YA(YA_dev):
    mean_salary = YA_dev['salary'].mean()
    return "In 'YA' region the average salary of a 'Developer' is " + str(mean_salary) + "\n"


# Program directory is only in CA region
def filter_prog_dir_CA(df_filtered_cols):
    CA_prog_dir = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Program Directory') & (df_filtered_cols['region'] == 'CA')]
    return CA_prog_dir


def avg_sal_prog_dir_CA(CA_prog_dir):
    mean_salary = CA_prog_dir['salary'].mean()
    return "In 'CA' region the average salary of a 'Program Directory' is " + str(mean_salary) + "\n"


# Product owner CA
def filter_prod_own_CA(df_filtered_cols):
    CA_prod_own = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'ProductOwner') & (df_filtered_cols['region'] == 'CA')]
    return CA_prod_own


def avg_sal_prod_own_CA(CA_prod_own):
    mean_salary = CA_prod_own['salary'].mean()
    return "In 'CA' region the average salary of a 'ProductOwner' is " + str(mean_salary) + "\n"


# product owner SA
def filter_prod_own_SA(df_filtered_cols):
    SA_prod_own = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'ProductOwner') & (df_filtered_cols['region'] == 'SA')]
    return SA_prod_own


def avg_sal_prod_own_SA(SA_prod_own):
    mean_salary = SA_prod_own['salary'].mean()
    return "In 'SA' region the average salary of a 'ProductOwner' is " + str(mean_salary) + "\n"


# product owner YA
def filter_prod_own_YA(df_filtered_cols):
    YA_prod_own = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'ProductOwner') & (df_filtered_cols['region'] == 'YA')]
    return YA_prod_own


def avg_sal_prod_own_YA(YA_prod_own):
    mean_salary = YA_prod_own['salary'].mean()
    return "In 'YA' region the average salary of a 'ProductOwner' is " + str(mean_salary) + "\n"


def write_to_out():
    outfile = open('/Users/aravind/Documents/technical-assessment/resources/output.txt', 'w')
    outfile.write(avg_sal_dev_CA(filter_dev_CA(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_dev_FA(filter_dev_FA(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_dev_YA(filter_dev_YA(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prog_dir_CA(filter_prog_dir_CA(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prod_own_CA(filter_prod_own_CA(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prod_own_SA(filter_prod_own_SA(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prod_own_YA(filter_prod_own_YA(filter_necessary_cols(read_json()))))


if __name__ == "__main__":
    # write_to_out()
    filter_dev_YA(filter_necessary_cols(read_json()))