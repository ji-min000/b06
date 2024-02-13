import pandas as pd

#데이터 불러오기 
df = pd.read_csv('C:/Users/user/Downloads/프로젝트 데이터_ RAW파일(날짜수정).csv' , index_col=0 , encoding_errors='ignore')

#환불건만 빼낸 데이터 프레임 
minus = df['Profit'] < 0
df_refund = df[minus]

#서브카테고리 기준 전체 수량 
sc_total= df.groupby(['Sub-Category']).agg({'Quantity' : 'sum'})

#서브카테고리 기준 환불 수량 
sc_minus = df_refund.groupby(['Sub-Category']).agg({'Quantity' : 'sum'})

#서브카테고리 기준 전체수량 대비 환불수량 비율 
sc_per_refund = round((sc_minus/sc_total)*100,1)

# 인텍스 정리 (서브카테고리 인덱스를 컬럼으로 넣고 기본 인텍스 추가) 
sc_per_refund_reset = sc_per_refund.reset_index() 

# NaN 값 (환불이 없는값) 0으로 변경 
sc_reset = sc_per_refund_reset.fillna(0)

# 환불비율이 적은 순으로 정렬 
sc_reset = sc_reset.sort_values(by="Quantity", ascending=True).head(20)

# 환불비율 점수화 
sc_reset['refund_score'] = round(sc_reset['Quantity']/68*10, 1)
