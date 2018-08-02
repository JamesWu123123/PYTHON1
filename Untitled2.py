
# coding: utf-8

# In[8]:



import numpy as np
import pandas as pd
from datetime import datetime
data=[]
data=pd.read_excel('sz50.xlsx',sheetname=None, index_col='datetime')


# In[3]:


print(data.keys())


# In[4]:


import numpy as np
import pandas as pd
import talib as ta
import matplotlib.pyplot as plt
from datetime import datetime
stock1=pd.read_excel('sz50.xlsx',sheetname='600036.XSHG', index_col='datetime')
#print(stock1)
array =np.array(stock1['close'].values)
#print(array)
ma10=ta.SMA(array,timeperiod=10)
print(type(ma10))
print(ma10[-5:])


# In[ ]:


import numpy as np
import pandas as pd
import talib as ta
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
sma=pd.Series(ma10)
plt.figure(figsize=(15, 7))
sma.index=stock1.close.index
plt.plot(sma,c='orange')
plt.plot(stock1.close,c='b')
plt.show()


# In[ ]:


2018GDP predict


# In[ ]:


import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot


# In[ ]:


import warnings
warnings.filterwarnings('ignore')
index=['国内生产总值(亿元)','国内生产总值增长率(%)','人均国内生产总值(元/人)','人均国内生产总值增长率(%)','居民消费水平(亿元)','投资(亿元)']
name=['2017年','2016年','2015年','2014年','2013年','2012年','2011年']
op1=[827122.00,11.23,0,0,0,0]
op2=[743585.00,6.70,53935.00,6.10,297990,445595.00]
op3=[689052.10,6.90,50251.00,6.40,271306,417746.10]
op4=[643974.00,7.30,47203.00,6.80,248892,395082.00]
op5=[595244.40,7.80,43852.00,7.20,226660,368584.40]
op6=[540367.40,7.90,40007.00,7.30,205786,334581.40]
op7=[489300.60,9.50,36403.00,9.00,183876,305424.60]
df2 = pd.DataFrame([op1,op2,op3,op4,op5,op6,op7])
df2=df2.T
df2.index=index
df2.columns=name
df2


# In[ ]:


gdp = df2.loc[['国内生产总值(亿元)']]


# In[ ]:


df2.loc[['国内生产总值(亿元)']]


# In[ ]:


print(gdp.values)


# In[ ]:


l=gdp.values.reshape(7,)
l2=[]
for each in l[::-1]:
    l2.append(each)
gdp_dta=pd.Series(l2)


# In[ ]:


gdp_dta.plot(figsize=(12,8))


# In[ ]:


gdp_dta


# In[ ]:


#gdp_dta= gdp_dta.diff(1)[1:]
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(gdp_dta,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(gdp_dta,ax=ax2)


# In[ ]:


gdp_dta


# In[ ]:


#touzi=kxiaofei
#k=touzi/xiaofei
#beta=op2[-1]/op2[-2]
#β=投资/消费今年-消费去年
beta=op2[-1]/(op2[-2]-op3[-2])
alpha=(op2[-2]/op3[-2])-1
beta


# In[ ]:


op1.insert(5,int(xiaofei2017))


# In[5]:


touzi2017=op1[0]-op1[4]


# In[ ]:


op1.insert(6,touzi2017)


# In[ ]:


op2=[743585.00,6.70,53935.00,6.10,297990,445595.00]
op3=[689052.10,6.90,50251.00,6.40,271306,417746.10]
op4=[643974.00,7.30,47203.00,6.80,248892,395082.00]
op5=[595244.40,7.80,43852.00,7.20,226660,368584.40]
op6=[540367.40,7.90,40007.00,7.30,205786,334581.40]
op7=[489300.60,9.50,36403.00,9.00,183876,305424.60]
df2 = pd.DataFrame([op1,op2,op3,op4,op5,op6,op7])
df2=df2.T
df2.index=index
df2.columns=name
df2


# In[ ]:


xiaofei2018=op1[-2]*(1+alpha)
xiaofei2018


# In[ ]:


xiaofei2018=op1[-2]*(1+alpha)
xiaofei2018


# In[ ]:


touzi2018
gdp2018=touzi2018+xiaofei2018
op0=[int(gdp2018),round(((gdp2018/op1[0]-1)*100),2),0,0,int(xiaofei2018),int(touzi2018)]
op2=[743585.00,6.70,53935.00,6.10,297990,445595.00]
op3=[689052.10,6.90,50251.00,6.40,271306,417746.10]
op4=[643974.00,7.30,47203.00,6.80,248892,395082.00]
op5=[595244.40,7.80,43852.00,7.20,226660,368584.40]
op6=[540367.40,7.90,40007.00,7.30,205786,334581.40]
op7=[489300.60,9.50,36403.00,9.00,183876,305424.60]
name=['2018年','2017年','2016年','2015年','2014年','2013年','2012年','2011年']
df2 = pd.DataFrame([op0,op1,op2,op3,op4,op5,op6,op7])
df2=df2.T
df2.index=index
df2.columns=name
df2


# In[6]:


gdp = df2.loc[['国内生产总值(亿元)']]
l=gdp.values.reshape(8,)
l2=[]
for each in l[::-1]:
    l2.append(each)
gdp_dta=pd.Series(l2)
gdp_dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2011','2018'))
gdp_dta.plot(figsize=(12,8))
gdp_dta

