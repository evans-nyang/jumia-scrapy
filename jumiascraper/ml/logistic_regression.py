import os

import pandas as pd
from dotenv import load_dotenv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder
from sqlalchemy import create_engine

load_dotenv()

DB_URI = os.environ.get('DB_URI')

con = create_engine(DB_URI)

df = pd.read_sql_table('mobile_phones', con)

mobile_phones_df = df

# Fill missing numerical values with the mean
numerical_cols = ['price', 'old_price', 'discount', 'votes', 'stars']
mobile_phones_df[numerical_cols] = mobile_phones_df[numerical_cols].fillna(mobile_phones_df[numerical_cols].mean())

# Fill missing categorical values with the most frequent category
categorical_cols = ['brand', 'specs', 'image_url', 'official_store']
mobile_phones_df[categorical_cols] = mobile_phones_df[categorical_cols].apply(lambda x: x.fillna(x.value_counts().index[0]))


# Convert categorical variables into numerical representations
# One-hot encode 'brand'
onehot_encoder = OneHotEncoder(sparse=False, drop='first')
brand_encoded = onehot_encoder.fit_transform(mobile_phones_df[['brand']])
brand_df = pd.DataFrame(brand_encoded, columns=onehot_encoder.get_feature_names_out(['brand']))
mobile_phones_df = pd.concat([mobile_phones_df, brand_df], axis=1)

# Label encode 'official_store'
label_encoder = LabelEncoder()
mobile_phones_df['official_store_encoded'] = label_encoder.fit_transform(mobile_phones_df['official_store'])


# Scale numerical features to bring them to a similar range. Used min-max scaling to scale the features between 0 and 1
scaler = MinMaxScaler()
numerical_cols_to_scale = ['price', 'old_price', 'discount', 'votes', 'stars']
mobile_phones_df[numerical_cols_to_scale] = scaler.fit_transform(mobile_phones_df[numerical_cols_to_scale])


# Define the target variable
y = mobile_phones_df['official_store_encoded']

# Define the feature matrix
features = ['price', 'discount', 'votes', 'stars'] + list(brand_df.columns)
X = mobile_phones_df[features]

# Convert all column names of X to strings
X = X.rename(columns={col: str(col) for col in X.columns})


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)


# Make predictions on the test data
y_pred = model.predict(X_test)


# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Generate a classification report to get more detailed evaluation metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

# pd.set_option('display.max_columns', None)
# print(mobile_phones_df)
