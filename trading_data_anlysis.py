# -*- coding: utf-8 -*-
"""Trading data anlysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eVy3L93zeMLsZbDbozwjpM7vzqTYjBXJ

#**TRADING DATA ANLYSIS**

**BATCH - 6**

**BATCH-MEMBERS :-**

* DUVVA SURESH CSINP318 **(T L)**

* RAMBA JAYA HARIKA CSINP327

* KADIYAM UMAMAHESWARI CSINP339

* DOREDLA SARANYA CSINP342

* POLISETTY AMALA MARY CSINP346

* PRAMODH MADICHARLA CSINP353

* SINDHU CHINTA CSINP360

# **IMPORTING LIBRARIES**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

"""## **RAW DATA**"""

date=['12-02-2022','12-02-2022','12-02-2022','14-02-2022','14-02-2022','14-02-2022','14-02-2022','15-02-2022','05-03-2022','05-03-2022',
      '06-03-2022','06-03-2022','07-03-2022','08-03-2022','08-03-2022','09-03-2022','10-03-2022','11-03-2022','12-03-2022','13-03-2022',
      '16-03-2022','17-03-2022','18-03-2022','18-03-2022','19-03-2022','20-03-2022','22-03-2022','23-03-2022','24-03-2022','25-03-2022',
      '26-03-2022','27-03-2022','05-04-2022','05-04-2022','06-04-2022','07-04-2022','08-04-2022','09-04-2022','11-04-2022','12-04-2022',
      '13-04-2022','14-04-2022','15-04-2022','17-04-2022','18-04-2022','18-04-2022','19-04-2022','20-04-2022','22-04-2022','22-04-2022']



script_Id=['INE5A0001','INE5A0002','INE5A0003','INE5A0004','INE5A0005','INE5A0006','INE5A0007','INE5A0008','INE5A0009','INE5A0010',
           'INE6B003','INE5BA01','INE5BA03','INE5VA008','INE5GA005','INEV5A006','INE5GB007','INE6YA008','INE5HA009','INE5DA010',
           'INE20RGA1','INE201H5A','INE4RA003','INETA56002','INE45G607','INE0HA006','INE0075A','INE5AHO1001','INETG5A008','INE5A0010',
           'INE5A001D','INE5D002E','INE5A003F','INE5A004G','INE56005H','INE5A006I','INE7G00J','INE0ER08K','INE0UA09L','INE06O10M',
           'INEYA001','INE5QOO2','INE5Q7600','INE5A00G6','INE6A007R','INE5AOO5D','INE5A009J','INERF00UH','INE9K005','INE6AKO10']



sector=['oil corporation','oil corporation','oil corporation','power grid corporation','metals','coco cola','coco cola','coco cola','power grid corporation','power grid corporation',
        'power grid corporation','electronics','electronics','electronics','electronics','electronics','electronics','electronics','electronics','electronics',
        'telecom','telecom','telecom','telecom','telecom','telecom','financial corporation','financial corporation','financial corporation','financial corporation',
        'financial corporation','financial corporation','financial corporation','financial corporation','financial corporation','financial corporation','financial corporation','financial corporation','power grid corporation','it sector',
        'vechile','ferrous','it sector','financial','financial','building material','medical','thermal','vechile','building material']



exchange=['NSE','NSE','BSE','NSE','NSE','NSE','NSE','NSE','NSE','BSE',
          'BSE','NSE','NSE','NSE','BSE','BSE','BSE','BSE','NSE','NSE',
          'BSE','BSE','BSE','BSE','NSE','NSE','NSE','NSE','NSE','NSE',
          'BSE','BSE','BSE','BSE','BSE','NSE','NSE','NSE','NSE','NSE',
          'NSE','NSE','NSE','NSE','NSE','BSE','BSE','NSE','BSE','NSE']



Type=['buy','sell','buy','buy','buy','buy','buy,','buy','buy','sell',
      'sell','sell','sell','sell','buy','sell','buy','buy','buy','sell',
      'sell','sell','sell','sell','sell','buy','buy','sell','sell','sell',
      'buy','buy','buy','sell','sell','buy','buy','sell','buy','buy','sell',
      'buy','buy','buy','sell','sell','sell','sell','sell','buy']



Quantity=[20,np.nan,30,np.nan,30,200,40,36,67,80,
          100,56,90,np.nan,100,67,60,98,78,65,
          100,67,90,np.nan,87,90,200,87,np.nan,np.nan,
          200,125,175,20,np.nan,np.nan,56,89,76,76,
          50,76,90,80,100,30,np.nan,np.nan,np.nan,np.nan]



brokername=['(UPSTOX) RKSV SECURITIES INDIA PRIVATE LIMITED','(UPSTOX) RKSV SECURITIES INDIA PRIVATE LIMITED','(UPSTOX) RKSV SECURITIES INDIA PRIVATE LIMITED','(UPSTOX) RKSV SECURITIES INDIA PRIVATE LIMITED','(UPSTOX) RKSV SECURITIES INDIA PRIVATE LIMITED','ANGEL ONE LIMITED',
'ANGEL ONE LIMITED','ANGEL ONE LIMITED','ANGEL ONE LIMITED','ANGEL ONE LIMITED','ANGEL ONE LIMITED','ANGEL ONE LIMITED','ANGEL ONE LIMITED','ANGEL ONE LIMITED','ANGEL ONE LIMITED','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD',
'KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD','KOTAK SECURITIES LTD',
'5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','5PAISA CAPITAL LIMITED','PAYTM MONEY LTD','PAYTM MONEY LTD','PAYTM MONEY LTD',
'PAYTM MONEY LTD','PAYTM MONEY LTD','PAYTM MONEY LTD','PAYTM MONEY LTD','PAYTM MONEY LTD','PAYTM MONEY LTD','PAYTM MONEY LTD']




brokerage_fee=[0.45,np.nan,np.nan,np.nan,0.45,0.34,0.45,0.36,0.78,0.76,
               0.63,0.69,0.74,np.nan,0.23,0.45,0.56,1.03,0.67,0.45,
               0.56,1.34,1.03,np.nan,0.56,0.65,0.65,0.46,0.63,0.72,
               1.43,1.45,1.45,np.nan,0.56,np.nan,0.76,0.56,0.53,1.54,
               1.45,1.64,0.65,np.nan,0.42,0.43,np.nan,np.nan,np.nan,0.87]



gst=[0.23,3.45,2.34,np.nan,1.23,1.34,1.46,1.54,1.45,4.67,
     4.56,np.nan,4.67,5.78,np.nan,3.56,3.45,6.45,3.45,8.99,
     6.67,6.69,5.87,2.45,5.23,np.nan,7.67,8.56,np.nan,np.nan,
     7.46,np.nan,np.nan,np.nan,4.56,6.96,4.76,3.54,5.76,np.nan,
     6.76,9.76,4.65,8.87,6.87,np.nan,np.nan,np.nan,np.nan,5.47]



stt=[0.67,0.78,np.nan,np.nan,0.87,0.78,0.78,0.67,0.56,0.56,
     0.99,np.nan,np.nan,np.nan,0.68,0.65,0.67,0.56,0.76,0.75,
     np.nan,np.nan,np.nan,0.87,0.78,0.77,0.87,np.nan,np.nan,np.nan,
     np.nan,0.78,0.87,0.76,0.76,0.76,0.76,0.76,np.nan,np.nan,
     np.nan,0.78,0.78,0.58,0.78,0.76,0.87,0.89,0.88,np.nan]



sebi=[0.89,0.88,np.nan,np.nan,np.nan,np.nan,0.78,0.78,0.89,0.69,
      np.nan,np.nan,np.nan,np.nan,np.nan,0.87,0.87,0.87,0.76,0.56,
      np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.78,0.78,0.67,0.78,
      0.67,0.67,0.76,0.87,0.87,np.nan,np.nan,np.nan,np.nan,np.nan,
      0.89,0.67,0.67,np.nan,np.nan,0.78,0.78,0.66,np.nan,np.nan]



stampduty=[0.56,0.67,0.67,0.67,0.56,0.67,np.nan,np.nan,np.nan,np.nan,
           0.67,0.56,0.67,0.67,0.76,0.67,0.78,np.nan,np.nan,0.67,
           0.67,np.nan,np.nan,0.78,0.67,0.67,0.48,0.67,np.nan,np.nan,
           0.67,0.56,0.56,0.67,0.57,0.78,np.nan,np.nan,np.nan,0.78,
           0.56,0.56,np.nan,np.nan,np.nan,0.78,0.67,0.68,0.67,np.nan]
orderno=['100589001','011322675','000765442','0874544564','0774544224','0653434556','8389292292','883992922','882828282','085363721',
         '7478329292','383292221','6474839221','7456372004','73728292','2728229292','72828292','737388293','45644567','654457545',
         '45543755456','564456454','564544545','45456564564','573454747','74547543754','7647646454','732327327','372657826','34234623734',
         '345327437','32236243','347326732','2363262784','325322364','343243232','36547655','3534654767','353456547','43654765658',
         '534654767','433253464','454567568','44565457','6474324','46454747','465654727','564764742','265475727','645767858']
trade_name =['indian oil','hpcl','bharat petroleum','ntpc ','vadanta ltd','coco cola','thumbsup','limca','apedcl','ap janko',
              'ap transco','samsung','lenovo','vivo','redmi','iphone','oppo','realme','nokia','lava',
              'airtel','idea','bsnl','vodafone','tatadocomo','jio','sbi bank','hdfc bank','canara bank','icici bank',
              'corporation bank','union bank','andhra bank','indian bank','bank of borada',' axis bank','central bank','reserve bank','ntpc ltd','infosys ltd',
              'tata motors','tata steel ltd','wipro ltc','bajaj auto ltd','bajaj finance ltd','asian paints ltd',' apollo hospital ltd','coal india ltd','hero motors ltd','shree cement ltd']


buyprice=[290,450,560.76,460.78,901.90,np.nan,np.nan,np.nan,np.nan,567.90,
          506.90,np.nan,np.nan,705.09,504.76,np.nan,np.nan,np.nan,546.76,np.nan,
          np.nan,np.nan,689.09,np.nan,np.nan,np.nan,np.nan,785.67,456.87,674.67,
          np.nan,np.nan,567.67,789.79,906.78,np.nan,np.nan,np.nan,np.nan,np.nan,
          780.67,806.68,679.95,609.78,907.78,789.07,789.90,np.nan,865.90,678.89]


sellprice=[np.nan,np.nan,np.nan,907.89,679.90,856.78,np.nan,np.nan,789.90,785.78,
           675.78,654.76,786.68,875.67,876.89,np.nan,np.nan,np.nan,643.67,np.nan,
           np.nan,678.46,657.76,np.nan,np.nan,np.nan,764.68,895.57,np.nan,np.nan,
           765.76,675.57,765.67,657.57,np.nan,np.nan,np.nan,657.57,np.nan,674.76,
           np.nan,np.nan,769.68,654.76,675.90,768.78,np.nan,np.nan,890.67,np.nan]



dayhigh=[359.67,764.7,np.nan,np.nan,np.nan,734.67,673.56,764.67,785.67,786.67,
         np.nan,np.nan,np.nan,np.nan,657.57,567.67,675.57,678.78,675.56,678.67,
         np.nan,np.nan,567.57,679.68,675.67,np.nan,np.nan,np.nan,675.55,np.nan,
         675.56,456.87,675.56,576.68,567.45,345.56,np.nan,np.nan,np.nan,np.nan,
         890.67,576.67,678.67,789.67,np.nan,np.nan,np.nan,678.57,np.nan,np.nan]



daylow=[345.56,564.46,654.67,657.57,675.57,654.67,345.56,np.nan,np.nan,np.nan,
        234.45,456.56,564.67,np.nan,np.nan,np.nan,np.nan,345.56,345.78,342.45,
        np.nan,np.nan,345.56,456.48,342.77,345.67,675.56,463.56,564.44,345.67,
        np.nan,np.nan,np.nan,np.nan,345.67,234.45,345.67,np.nan,564.56,np.nan,
        np.nan,np.nan,np.nan,345.67,453.56,235.56,456.67,234.89,np.nan,np.nan]



openprice=[230,240,np.nan,253.66,np.nan,140.66,np.nan,145.69,146.69,150.64,
           234.78,243.69,244.96,np.nan,343.63,np.nan,345.67,567.89,345.64,340.75,
           np.nan,235.77,238.99,255.67,np.nan,258.96,234.56,np.nan,534.78,345.89,
           np.nan,np.nan,456.67,345.78,np.nan,568.95,348.69,678.76,258.86,289.80,
           350.67,450.69,567.78,np.nan,678.78,654.66,549.78,674.66,675.87,540.80]



personname=['chandra','suresh','sirisha','harika','saranya','promodh','mary','amala','sindu','ramba',
            'jaya','urvasi','sunny','samantha','samatha','durga','prasad','ramana','rupa','bhavani',
            'vishwa','satya','nandini','ram','nithin','charan','rajnikanth','tarak','kalyan','pawan',
            'praveen','uma','maheswari','mahesh','eswari','siva','sekhar','naga devi','prasad','janani',
            'blake blossam','cherry','jhonny sins','mia malkova','mia khalifa','tony','shanker','gowtham','bala krishna','gopi']



panno=['APO5EE9078','APO5O6GGG5A','APO5OOH6345','APO590OO7T8','APO5UY67001','APO5LO9087','APO590O007','APO590887','APO58900E4','APO59IK887',
       'APO5RA005','APO57A003','AP05TA22005','APO5GR55A9','APO5900Y6','APO5ERFG3','APO59IKK8','APO5UA550','APO5RA223','APO567RRA2',
       'APORGH5A009','PB065A007','KAO6HA007','KO98KA7001','KOT68JA1','HAO90078','AO06HH62','ASO7BN009','HN560089','JK007OOK8',
       'AP0B6HH5AG9','GU6JNNA90','TY6678005','RAOO67H56','GH6706GU1','RT67008GA01','HJ7AFG678','HU89700GA1','HU7T5601','KO87OOUT1',
       'TYOP9065','HJ6755FA','HJUU76FA5','HJY667GA','GH658JK1','HJU67A20','OG80OOP001','UJ7765RA1','KOTOO086','GH6Y0067']



uccno=['2000155674','2345518900','0999670054','676466894','6756545501','870014567','566780743','7863780045','870018956','780853434',
       '67007000012','0977667001','67557600123','6743500123','5637720','78690489','097878001','674562980','09887813001','870889010',
       '67587098801','78600457643','5670056A001','653400123','6755300234','765300125','67553008234','8766OO2001','89776001001','08601123090',
       '78600675','8755462201','675530017','2000155674','6788456','9077564','764400352','897723456','907754267','9077536',
       '67554830','65448342','786645201','897754230','67553001','670045632','7855462001','89005631','78994561','78996531']

"""## **data framing**"""

data={'DATE':date,
    'SCRIPT_ID':script_Id,
    'SECTOR':sector,
    'EXCHANGE':exchange,
    'QUANTITY':Quantity,
    'TYPE':Type,
    'BROKER_NAME':brokername,
    'ORDERNO':orderno,
    'TRADE_NAME':trade_name,
    'PERSON_NAME':personname,
    'PAN_NO':panno,
    'UCC_NO':uccno}

dataset=pd.DataFrame(data,columns=['DATE','SCRIPT_ID','SECTOR','EXCHANGE','QUANTITY','TYPE','BROKER_NAME','ORDERNO','TRADE_NAME','PERSON_NAME','PAN_NO','UCC_NO'])
dataset.head()#5

dataset.tail()#5

dataset.dtypes

empty=[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
       np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
       np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
       np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
       np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]

Data={
    'OPENPRICE':openprice,
    'DAYHIGH':dayhigh,
    'DAYLOW':daylow,
    'BUYPRICE':buyprice,
    'SELLPRICE':sellprice,
    'GOVERNAMENT_SERVICE_TAX(GST)':gst,
    'SECURITIES_TRANSCATION_TAX(STT)':stt,
    'SECURITIES_AND_EXCHANGE_BOARD_OF_INDIA(SEBI)':sebi,
    'STAMPDUTY':stampduty,
    'BROKERAGE_FEE':brokerage_fee,
    'empty':empty
}

dataset1=pd.DataFrame(Data,columns=['OPENPRICE','DAYHIGH','DAYLOW','BUYPRICE','SELLPRICE','GOVERNAMENT_SERVICE_TAX(GST)','SECURITIES_TRANSCATION_TAX(STT)','SECURITIES_AND_EXCHANGE_BOARD_OF_INDIA(SEBI)','STAMPDUTY','BROKERAGE_FEE','empty'])
dataset1.head()

dataset1.tail()

dataset.columns

dataset1.columns

dataset.shape

dataset1.shape

"""-------------**find the null values**-----------"""

dataset.isna().head()

dataset.isna().tail()

dataset.notnull().head()

dataset.notnull().tail()

dataset1.isna().head()

dataset1.isna().tail()

dataset1.notnull().head()

dataset1.notnull().tail()

dataset.isna().sum(),dataset.isna().sum().sum()#12

dataset.notnull().sum()

dataset1.isna().sum()#.sum()#234

dataset1.notnull().sum()

"""-------**remove the empty null column**------------"""

dataset1=dataset1.drop('empty',axis=1)# Delete the empty column form 'df1' data set.
dataset1.columns

"""-------------**fill the null values**--------------"""

dataset['QUANTITY'].fillna(dataset['QUANTITY'].max(),inplace=True)
dataset.head()

dataset.isna().sum()

dataset1['OPENPRICE'].fillna(dataset1['OPENPRICE'].min(),inplace=True)
dataset1['DAYHIGH'].fillna(dataset1['DAYHIGH'].max(),inplace=True)
dataset1['DAYLOW'].fillna(dataset1['DAYLOW'].min(),inplace=True)
dataset1['BUYPRICE'].fillna(dataset1['BUYPRICE'].max(),inplace=True)
dataset1['SELLPRICE'].fillna(dataset1['SELLPRICE'].max(),inplace=True)
dataset1['GOVERNAMENT_SERVICE_TAX(GST)'].fillna(dataset1['GOVERNAMENT_SERVICE_TAX(GST)'].max(),inplace=True)
dataset1['SECURITIES_TRANSCATION_TAX(STT)'].fillna(dataset1['SECURITIES_TRANSCATION_TAX(STT)'].min(),inplace=True)
dataset1['SECURITIES_AND_EXCHANGE_BOARD_OF_INDIA(SEBI)'].fillna(dataset1['SECURITIES_AND_EXCHANGE_BOARD_OF_INDIA(SEBI)'].mean(),inplace=True)
dataset1['STAMPDUTY'].fillna(dataset1['STAMPDUTY'].min(),inplace=True)
dataset1['BROKERAGE_FEE'].fillna(dataset1['BROKERAGE_FEE'].mean(),inplace=True)
dataset1.head()

dataset1.isna().sum()

dataset1['total_buy_price']=dataset1.BUYPRICE*dataset.QUANTITY
dataset1['total_sell_price']=dataset1.SELLPRICE*dataset.QUANTITY
dataset1['sum_of_transation_taxes/quantity']=dataset1['GOVERNAMENT_SERVICE_TAX(GST)']+dataset1['SECURITIES_TRANSCATION_TAX(STT)']+dataset1['SECURITIES_AND_EXCHANGE_BOARD_OF_INDIA(SEBI)']+dataset1['STAMPDUTY']+dataset1['BROKERAGE_FEE']
dataset1['total_transcation_taxes']=dataset['QUANTITY']*dataset1['sum_of_transation_taxes/quantity']
dataset1.head()

dataset1['net']=dataset1['total_sell_price']-dataset1['total_buy_price']-dataset1['total_transcation_taxes']
dataset1.head()

def gain(value):
  if value < 0:
    return 'loss'
  if value > 0:
    return 'profit'
dataset1['gain']=dataset1['net'].map(gain)

dataset1.shape

"""## **FINALLY OBTAINED DATAFRAME**"""

finaldataset=pd.concat([dataset,dataset1],axis=1)
pd.set_option('display.max_columns',None)
finaldataset.head()

finaldataset.columns

finaldataset.shape

finaldataset.info()

finaldataset.ndim #dimension of finaldataset

finaldataset.describe()

Df3=finaldataset.filter(['QUANTITY','OPENPRICE','DAYHIGH','DAYLOW	BUYPRICE','SELLPRICE','GOVERNAMENT_SERVICE_TAX(GST)','SECURITIES_TRANSCATION_TAX(STT)','SECURITIES_AND_EXCHANGE_BOARD_OF_INDIA(SEBI)','	STAMPDUTY','BROKERAGE_FEE','total_buy_price','total_sell_price','sum_of_transation_taxes/quantity','total_transcation_taxes','net'])
Df3.corr()#corelation

Df3.cov()#covariation

"""# **data visualization**

### **Line graph**
"""

df5=finaldataset['OPENPRICE'].iloc[20:31]
df6=finaldataset['DAYHIGH'].iloc[20:31]
df7=finaldataset['DAYLOW'].iloc[20:31]
DF1=finaldataset['DATE'].iloc[20:31]

"""line graph values"""

pd.concat([DF1,df5,df6,df7],axis=1)

plt.plot(DF1,df5,marker='d',color='red',label='OPENPRICE')
plt.plot(DF1,df6,marker='+',color='green',label='DAYHIGH')
plt.plot(DF1,df7,marker='*',color='blue',label='DAYLOW')
plt.xticks(color='slateblue')
plt.tick_params(axis='x',labelrotation=90)
plt.xlabel('trade days',fontsize=20,labelpad=20)
plt.ylabel('price',fontsize=20,labelpad=20)
plt.title('stock predicted',pad=20)
plt.grid(alpha=0.5)
plt.legend(frameon=True,framealpha=0.8,edgecolor='aqua',ncol=1,fontsize='small',labelspacing=1)
plt.show()

"""### **bar graph**"""

dfx=finaldataset['total_buy_price'].iloc[0:10]
dfy=finaldataset['PERSON_NAME'].iloc[0:10]
df3=finaldataset['total_sell_price'].iloc[0:10]
df4=finaldataset['net'].iloc[0:10]
df8=finaldataset['gain'].iloc[0:10]

"""bar graph values"""

pd.concat([dfy,dfx,df3,df4,df8],axis=1)

w=0.1985
x=dfy
bar1=np.arange(len(dfy))
bar2=[i+w for i in bar1]
bar3=[i+w for i in bar2]
plt.bar(bar1,dfx,width=w,label='total_buy_price')
plt.bar(bar2,df3,width=w,label='total_sell_price')
plt.bar(bar3,df4,width=w,label='net')
plt.xticks(bar1+w,x,size=10,rotation=90)
plt.xlabel('traders',fontsize=20,color='red',alpha=0.6)
plt.ylabel('stocks predicted',fontsize=20,color='red',alpha=0.6)
plt.title('traders net worth',pad=10)
plt.legend(edgecolor='black')
plt.show()

"""### **Heat map for corelation**"""

sns.heatmap(Df3.corr())
plt.plot()