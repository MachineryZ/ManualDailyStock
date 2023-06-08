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

# Get stock symbol and get daily data
stock_zh_a_spot_em = akshare.stock_zh_a_spot_em()
all_symbol_list = stock_zh_a_spot_em["代码"]
for symbol in all_symbol_list:
    print(symbol)
    data = akshare.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        start_date="20150101",
        end_date="20210907",
        adjust="",
    )
    print(data.shape)
