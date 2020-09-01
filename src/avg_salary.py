import json
from pandas.io.json import json_normalize


def read_json():
    with open("../resources/sample_data.json") as sample_data:
        data = json.load(sample_data)
        employees = data['Employees']
        df = json_normalize(employees)
        return df


# Here we are filtering only the necessary columns needed for the average salary calculation in each region
# Also we are removing ',' to make the salary column as integer type
def filter_necessary_cols(df):
    df_filtered_cols = df[['jobTitleName', 'region', 'salary']]
    df_filtered_cols['salary'] = df_filtered_cols['salary'].replace(',', '', regex=True)
    df_filtered_cols['salary'] = df_filtered_cols['salary'].astype('int')
    return df_filtered_cols


# In this method we are filtering developer's in CA region
def filter_dev_ca(df_filtered_cols):
    ca_dev = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Developer') & (df_filtered_cols['region'] == 'CA')]
    return ca_dev


# In this method we are calculating the average salary of a developer in CA region by taking a mean of the salary column
def avg_sal_dev_ca(ca_dev):
    mean_salary = ca_dev['salary'].mean()
    return "In 'CA' region the average salary of a 'Developer' is " + str(mean_salary) + "\n"


# In this method we are filtering developer's in FA region
def filter_dev_fa(df_filtered_cols):
    fa_dev = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Developer') & (df_filtered_cols['region'] == 'FA')]
    return fa_dev


# In this method we are calculating the average salary of a developer in FA region by taking a mean of the salary column
def avg_sal_dev_fa(fa_dev):
    mean_salary = fa_dev['salary'].mean()
    return "In 'FA' region the average salary of a 'Developer' is " + str(mean_salary) + "\n"


# In this method we are filtering developer's in YA region
def filter_dev_ya(df_filtered_cols):
    ya_dev = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Developer') & (df_filtered_cols['region'] == 'YA')]
    return ya_dev


# In this method we are calculating the average salary of a developer in YA region by taking a mean of the salary column
def avg_sal_dev_ya(ya_dev):
    mean_salary = ya_dev['salary'].mean()
    return "In 'YA' region the average salary of a 'Developer' is " + str(mean_salary) + "\n"


# Program directory is only in CA region
# In this method we are filtering Program Directory in CA region
def filter_prog_dir_ca(df_filtered_cols):
    ca_prog_dir = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'Program Directory') & (df_filtered_cols['region'] == 'CA')]
    return ca_prog_dir


# In this method we are calculating the average salary of a Program Directory in CA region by taking a mean of the salary column
def avg_sal_prog_dir_ca(ca_prog_dir):
    mean_salary = ca_prog_dir['salary'].mean()
    return "In 'CA' region the average salary of a 'Program Directory' is " + str(mean_salary) + "\n"


# Product owner CA
# In this method we are filtering Product owner in CA region
def filter_prod_own_ca(df_filtered_cols):
    ca_prod_own = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'ProductOwner') & (df_filtered_cols['region'] == 'CA')]
    return ca_prod_own


# In this method we are calculating the average salary of a Product owner in CA region by taking a mean of the salary column
def avg_sal_prod_own_ca(ca_prod_own):
    mean_salary = ca_prod_own['salary'].mean()
    return "In 'CA' region the average salary of a 'ProductOwner' is " + str(mean_salary) + "\n"


# product owner SA
# In this method we are filtering Product owner in SA region
def filter_prod_own_sa(df_filtered_cols):
    sa_prod_own = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'ProductOwner') & (df_filtered_cols['region'] == 'SA')]
    return sa_prod_own


# In this method we are calculating the average salary of a Product owner in SA region by taking a mean of the salary column
def avg_sal_prod_own_sa(sa_prod_own):
    mean_salary = sa_prod_own['salary'].mean()
    return "In 'SA' region the average salary of a 'ProductOwner' is " + str(mean_salary) + "\n"


# product owner YA
# In this method we are filtering Product owner in YA region
def filter_prod_own_ya(df_filtered_cols):
    ya_prod_own = df_filtered_cols[
        (df_filtered_cols['jobTitleName'] == 'ProductOwner') & (df_filtered_cols['region'] == 'YA')]
    return ya_prod_own


# In this method we are calculating the average salary of a Product owner in YA region by taking a mean of the salary column
def avg_sal_prod_own_ya(ya_prod_own):
    mean_salary = ya_prod_own['salary'].mean()
    return "In 'YA' region the average salary of a 'ProductOwner' is " + str(mean_salary) + "\n"


# Here we are printing all the data to a output file (average salary of Developer, Program Directory and Product Owner in particular region)
def write_to_out():
    outfile = open('../outputs//output.txt', 'w')
    outfile.write(avg_sal_dev_ca(filter_dev_ca(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_dev_fa(filter_dev_fa(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_dev_ya(filter_dev_ya(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prog_dir_ca(filter_prog_dir_ca(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prod_own_ca(filter_prod_own_ca(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prod_own_sa(filter_prod_own_sa(filter_necessary_cols(read_json()))))
    outfile.write(avg_sal_prod_own_ya(filter_prod_own_ya(filter_necessary_cols(read_json()))))


if __name__ == "__main__":
    write_to_out()
