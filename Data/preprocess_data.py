import pandas
import numpy as np
import akshare
import argparse



"""
akshare stock api

stock_sse_summary: 
    shanghai exchange, stock data
stock_szse_summary: 
    shenzhen stock exchange
stock_szse_area_summary: 
    shenzhen stock exchange area
stock_szse_sector_summary: 
    shenzhen stock exchange sector
stock_sse_deal_daily: 
    shanghai deal daily
stock_individual_info_em: 
    individual stock, east money 
stock_bid_ask_em: 
stock_zh_a_spot_em: 
    shenzhen and shanghai  astock spot east money
stock_sh_a_spot_em:
stock_sz_a_spot_em:
stock_bj_a_spot_em:
stock_new_a_spot_em:
stock_cy_a_spot_em:
    cy chuangye 
stock_kc_a_spot_em:
    kc ke chuang
stock_zh_a_spot:
    different from east money
stock_zh_a_hist: 
    history data **RECOMMANDED**
stock_zh_a_daily:
    history data from xinlang, 


"""

def get_parser():
    parser = argparse.ArgumentParser(description="preprocess parser")
    parser.add_argument('--start_date', default="", type=str)
    parser.add_argument('--end_date', default="", type=str)
    parser.add_argument('--data_frequency', default="daily")
    parser.add_argument('--data_save_path', default="/home/zzz/StockDaily")
    args = parser.parse_args()
    return args

# Get stock symbol and get daily data
def get_daily_data(
    args: argparse.ArgumentParser = None,
):
    stock_zh_a_spot_em = akshare.stock_zh_a_spot_em()
    all_symbol_list = stock_zh_a_spot_em["代码"]
    for symbol in all_symbol_list:
        print(symbol)
        data = akshare.stock_zh_a_hist(
            symbol=symbol,
            period=args.data_frequency,
            start_date=args.start_date,
            end_date=args.end_date,
            adjust="",
        )
        

if __name__ == "__main__":
    args = get_parser()
    get_daily_data(args=args)

