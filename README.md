# ShipsEar-An-Unofficial-Train-Test-Split
An unofficial train-test split for ShipsEar: An underwater vessel noise database

### Background
The ShipsEar dataset (https://doi.org/10.1016/j.apacoust.2016.06.008) is one of the most commonly used underwater noise databases and is widely used in the field of underwater acoustics.    
However, the official train-test split is not available, which prevents fair comparisons for many works.  
This repo is intended to provide an unofficial training-test split for works seeking fair comparisons and credible benchmarks.  

### Train-Test Split for 12 classes

|Category|Training set| Test set|
| ---- | ---- | ---- |
|Dredger|Dredger_80__04_10_12_adricristuy.wav <br> Dredger_94__A__Draga_2.wav <br> Dredger_96__A__Draga_4.wav | Dredger_93__A__Draga_1.wav <br> Dredger_95__A__Draga_3.wav|
|Fishboat|Fishboat_73__23_07_13_H3_pesqMariCarmen.wav <br> Fishboat_74__23_07_13_H3_pesqSaladinoPrimero.wav <br> Fishboat_76__23_07_13_H3_pesquero2.wav|Fishboat_75__23_07_13_H3_pesquero1.wav|
|Motorboat|Motorboat_27__19_07_13_Lancha2.wav <br> Motorboat_33__19_07_13_lanchaDuda_Sale.wav <br> Motorboat_39__19_07_13_lanchaMotora_Entra.wav <br> Motorboat_45__19_07_13_yate_Sale.wav <br> Motorboat_50__23_07_13_H3_lancha1.wav <br> Motorboat_52__23_07_13_H3_lancha3_interf.wav <br> Motorboat_70__23_07_13_H2_yatePeq.wav <br> Motorboat_72__23_07_13_H3_lancha2.wav <br> Motorboat_77__23_07_13_H3_Planeadora.wav <br> Motorboat_79__23_07_13_H3_zodiac.wav|Motorboat_21__18_07_13_lanchaMotora.wav <br> Motorboat_26__19_07_13_Lancha.wav <br> Motorboat_51__23_07_13_H3_lancha2_interf.wav|
|Musselboat|Musselboat_47__23_07_13_H2_bateero2.wav <br> Musselboat_48__23_07_13_H3_bateero3_interf.wav <br> Musselboat_49__23_07_13_H1_bateero4.wav|Musselboat_46__23_07_13_H3_bateero1.wav <br> Musselboat_66__23_07_13_H3_Pesquerito2_Velero.wav|
