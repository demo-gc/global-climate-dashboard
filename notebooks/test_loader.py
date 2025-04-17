import sys
# filepath = r'C:\Users\user\PycharmProjects\PublicProjects\data\raw\ global_temp_anomalies.csv'
sys.path.append('../src')  # So you can import from src/


from data_loader import load_global_temperature_data

df = load_global_temperature_data()
df.head()
