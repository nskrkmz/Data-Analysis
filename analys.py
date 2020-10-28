import pandas as pd
import numpy as np

sozluk = {'İsim':pd.Series(['Ada','Cem','Sibel','Ahmet','Mehmet','Ali','Veli',
          'Ayşe','Hüseyin','Necmi','Nalan','Namık']),
          'Meslek':pd.Series(['işçi','işçi','memur','serbest','serbest',None,None,
          'sigortacı','işsiz',None,None,'memur']),
          'Tarih':pd.Series(['11.11.2010','11.11.2010','11.11.2010','18.11.2011','18.11.2011',None,None,
          None,'11.11.2010',None,'18.11.2011','18.11.2011']),          
          'Yaş':pd.Series([21, 24, 25, 44, 31, 27, 35, 33, 42, 29, 41, 43]),
          'ÇocukSayısı':pd.Series([None, None, None, None, None, 1, 2, 0, None, None, None, None]),
          'Puan':pd.Series([89, 87, 77, 55, 70, 79, 73, 79, 54, 92, 61, 69])}

df = pd.DataFrame(sozluk)

# df.head() ilk 5 satırı görüntüler
# df.tail() son 5 satırı görüntüler
# df.sample() rastgele 5 satırı görüntüler
# df.shape() satır ve sutun sayısını görüntüler
# df.info() veri hakkında bilgi verir
# df['Yaş']  nitelik seçerek kayır gösterme
# df['Yaş','İsim'] [:5] nitelik seçerek ilk 5 kayıt
# df[['Yas','İsim']]  birden fazla nitelik seçme

# df[(df['Yas']>30) & (df['Puan']>50)]  koşullu nitelik isteme

#puery() fonksiyonu ile filtreleme
#df_filtered = df.query('Yaş>30 & Puan>50')

















