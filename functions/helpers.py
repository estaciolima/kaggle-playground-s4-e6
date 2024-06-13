def convert_feature_types(df):
    df = df.astype('category')
    df = df.astype({'Previous qualification (grade)': 'float64',
            'Admission grade': 'float64',
            'Age at enrollment': 'int64',
            'Curricular units 1st sem (credited)': 'int64',
            'Curricular units 1st sem (enrolled)': 'int64',
            'Curricular units 1st sem (evaluations)': 'int64',
            'Curricular units 1st sem (approved)': 'int64',
            'Curricular units 1st sem (grade)': 'float64',
            'Curricular units 1st sem (without evaluations)': 'int64',
            'Curricular units 2nd sem (credited)': 'int64',
            'Curricular units 2nd sem (enrolled)': 'int64',
            'Curricular units 2nd sem (evaluations)': 'int64',
            'Curricular units 2nd sem (approved)': 'int64',
            'Curricular units 2nd sem (grade)': 'float64',
            'Curricular units 2nd sem (without evaluations)': 'int64',
            'Unemployment rate': 'float64',
            'Inflation rate': 'float64',
            'GDP': 'float64'
            })
    
    return df
        