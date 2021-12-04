#Variables categoricas con NA
#CATEGORICAL_VARS_WITH_NA_FREQUENT = ['Cabin', 'Embarked','SibSp', 'Parch']

#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Age']


#Varibles para transformación logaritmia
NUMERICALS_LOG_VARS = ['Fare']

#Variables para hacer mapeo categorico por codificación ordinal
SEX_VARS = ['Sex']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['Cabin', 'Embarked','SibSp', 'Parch', 'Pclass']

#Mapeos de variables categoricas
SEX_MAPPINGS = {'male':1, 'female':0}

#Variables seleccionadas según análisis de Lasso
FEATURES = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']