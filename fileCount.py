# -*- coding: utf-8 -*-

'''
    Author : Choi Hey Min   
    
    하위 폴더 파일수 count 해서 excel 각 PREDICT의 ['path', 'count'] 저장
    
    최종 수정일 : 2021.03.08

'''

import os
import pandas as pd


def get_files(path):
    
    columns = ['path', 'count']
    df_data = pd.DataFrame(columns=columns)
    
    for currentdir, dirs, files in os.walk(path):
        # print(currentdir)
        fileCnt = (len(files)-1)/3
        # print('count:{}' .format(fileCnt))
        
        data = [currentdir, fileCnt]
        
        df_data = df_data.append(pd.Series(data, index=df_data.columns), ignore_index=True)
    
    return df_data


if __name__ == '__main__':
    
    path_list = ['PREDICT2', 'PREDICT5']

    df_cnt = pd.DataFrame()
    
    for path in path_list:
        
        df_new_data = get_files(path)
        
        df_cnt = pd.concat((df_cnt, df_new_data), axis=1)
    
    excel_file = 'model_cnt.xlsx'
    df_cnt.to_excel(excel_file, index=False)
    print('create {}' .format(excel_file))
    