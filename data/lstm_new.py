import pandas as pd

sas_pre = "https://erstoracc1.dfs.core.windows.net/erblockstorage/gold/Sales_ml/new/"
sas_token="sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-08-14T15:15:40Z&st=2024-02-02T07:15:40Z&spr=https&sig=qqqKyJOeYz2SxE7R4KfiaFaH1ohIRaTgnLblwTW3zVU%3D"
sas_pre_pred = "https://erstoracc1.dfs.core.windows.net/erblockstorage/pred/sales_v2/"
# sas_token="?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-08-14T15:15:40Z&st=2024-02-02T07:15:40Z&spr=https&sig=qqqKyJOeYz2SxE7R4KfiaFaH1ohIRaTgnLblwTW3zVU%3D"


def get_main():
    df_main = pd.read_csv(sas_pre + "data.csv?" + sas_token)
    return df_main


def get_data(order):
    df_main = get_main()
    data = df_main
    return data