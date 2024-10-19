import pandas as pd

#----------Leer el raw data------------
#data CDC
datasets = {
    "boys": {
        "age_weight": pd.read_csv("data/CDC/0-2/b_age_weight.csv"),
        "age_length": pd.read_csv("data/CDC/0-2/b_age_length.csv"),
        "age_head": pd.read_csv("data/CDC/0-2/b_age_headc.csv"),
        "length_weight": pd.read_csv("data/CDC/0-2/b_length_weight.csv"),
        "BMI_for_age_2_20": pd.read_csv("data/CDC/2-20/BMI-for-age_b.csv"),
        "Weight_for_age_2_20": pd.read_csv("data/CDC/2-20/Weight-for-age_b.csv"),
        "Stature_for_age_2_20": pd.read_csv("data/CDC/2-20/Stature-for-age_b.csv")
    },
    "girls": {
        "age_weight": pd.read_csv("data/CDC/0-2/g_age_weight.csv"),
        "age_length": pd.read_csv("data/CDC/0-2/g_age_length.csv"),
        "age_head": pd.read_csv("data/CDC/0-2/g_age_headc.csv"),
        "length_weight": pd.read_csv("data/CDC/0-2/g_length_weight.csv"),
        "BMI_for_age_2_20": pd.read_csv("data/CDC/2-20/BMI-for-age_W.csv"),
        "Weight_for_age_2_20": pd.read_csv("data/CDC/2-20/Weight-for-age_W.csv"),
        "Stature_for_age_2_20": pd.read_csv("data/CDC/2-20/Stature-for-age_W.csv")
    }
}

#data OMS

datasets_oms = {
    'boys':{
        'age_weight':pd.read_csv('data/OMS/0-5/b_weight_age_oms_0-3.csv'),
        'age_head_0-3':pd.read_csv('data/OMS/0-5/b_hc_oms_0-3.csv'),
        'age_head_3-5':pd.read_csv('data/OMS/0-5/b_hc_oms_3-5.csv'),
        "age_length_0-3": pd.read_csv("data/OMS/0-5/b_length_age_oms_0-3.csv"),
        "length_weight_0-2": pd.read_csv("data/OMS/0-5/b_weight_height_oms_0-2.csv"),
        "length_weight_2-5": pd.read_csv("data/OMS/0-5/b_weight_height_oms_2-5.csv"),
        "BMI_for_age_5_19": pd.read_csv("data/OMS/5-19/b_bmi_oms.csv"),
        "Weight_for_age_3_10": pd.read_csv("data/OMS/5-19/b_weight_a_oms_3-10.csv"),
        "Stature_for_age_3_19": pd.read_csv("data/OMS/5-19/b_height_oms_3-19.csv")
    },
    'girls':{
        'age_weight':pd.read_csv('data/OMS/0-5/g_weight_age_oms_0-3.csv'),
        'age_head_0-3':pd.read_csv('data/OMS/0-5/g_hc_oms_0-3.csv'),
        'age_head_3-5':pd.read_csv('data/OMS/0-5/g_hc_oms_3-5.csv'),
        "age_length_0-3": pd.read_csv("data/OMS/0-5/g_length_age_oms_0-3.csv"),
        "length_weight_0-2": pd.read_csv("data/OMS/0-5/g_weight_height_oms_0-2.csv"),
        "length_weight_2-5": pd.read_csv("data/OMS/0-5/g_weight_height_oms_2-5.csv"),
        'BMI_for_age_5_19': pd.read_csv("data/OMS/5-19/g_bmi_oms.csv"),
        "Weight_for_age_3_10": pd.read_csv("data/OMS/5-19/g_weight_a_oms_3-10.csv"),
        "Stature_for_age_3_19": pd.read_csv("data/OMS/5-19/g_height_oms_3-19.csv")
    }
}