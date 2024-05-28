from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__) 
CORS(app)  # Enable CORS for all routess

@app.route('/api/data', methods=['GET'])
def get_data():
    # Read and process the CSV filee
    df = pd.read_csv('cheat_sheet.csv')
    df_sorted = df.sort_values(by=['ETR Rank'])
    df_final = df_sorted[['Team', 'Name', 'Position', 'ETR Rank', 'ADP', 'ADP Differential', 'Week_17', 'Week_16', 'Week_15', 'Division']]
    
    # Convert the DataFrame to a list of dictionaries
    data = df_final.to_dict(orient='records')
    
    # Return the data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
