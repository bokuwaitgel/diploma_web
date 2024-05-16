import pandas as pd

sas_pre = "https://erstoracc1.dfs.core.windows.net/erblockstorage/gold/Sales_ml/Sales_WeeklyCoalPrice_HCC/"
sas_token="sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-08-14T15:15:40Z&st=2024-02-02T07:15:40Z&spr=https&sig=qqqKyJOeYz2SxE7R4KfiaFaH1ohIRaTgnLblwTW3zVU%3D"
sas_pre_pred = "https://erstoracc1.dfs.core.windows.net/erblockstorage/pred/sales/"
# sas_token="?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-08-14T15:15:40Z&st=2024-02-02T07:15:40Z&spr=https&sig=qqqKyJOeYz2SxE7R4KfiaFaH1ohIRaTgnLblwTW3zVU%3D"


def get_main():
    df_main = pd.read_csv(sas_pre + "Sales_WeeklyCoalPrice_HCC.csv?" + sas_token)
    return df_main

def get_pred(order, value):
    df_pred_exm = pd.read_csv(sas_pre_pred + "exm_"+order+".csv?" + sas_token)
    df_pred_lstm = pd.read_csv(sas_pre_pred + "lstm_"+order+".csv?" + sas_token)
    df_pred_sarima = pd.read_csv(sas_pre_pred + "sarima_"+order+".csv?" + sas_token)
    
    #let calculate the average of the three models
    df_pred = (df_pred_exm[value] + df_pred_lstm[value] + df_pred_sarima[value]) / 3
    
    df_pred = pd.DataFrame(df_pred)
    # #add the date column
    
    df_pred['Date'] = df_pred_exm['Date']
    return df_pred


def get_data(order, value):
    df_main = get_main()
    df_pred = get_pred(order, value)
    data = df_main, df_pred
    return data

