# ShipsEar-An-Unofficial-Train-Test-Split
An unofficial train-test split for ShipsEar: An underwater vessel noise database

## Background
**The ShipsEar dataset** (https://doi.org/10.1016/j.apacoust.2016.06.008) is one of the most commonly used underwater noise databases and is widely used in the field of underwater acoustics.    
However, the official train-test split is not available, which prevents fair comparisons for many works.  
This repo is intended to provide an unofficial **training-test split** for works seeking **fair comparisons and credible benchmarks**.  


## Train-Test Split
This repo releases two train-test-split for the following tasks:
1. 9-class recognition for ``Dredger, Fishboat, Motorboat, Musselboat, Naturalambientnoise, Oceanliner, Passengers, RORO, Sailboat''. The remaining three categories (Pilotship, Trawler, Tugboat) are not adopted due to the few number of recordings.   
2. 12-class recognition for ``Dredger, Fishboat, Motorboat, Musselboat, Naturalambientnoise, Oceanliner, Passengers, Pilotship, RORO, Sailboat, Trawler, Tugboat''

To prevent the model from overfitting to specific test data, we give different train-test-splits for 9-class and 12-class recognition. If the model can achieve promising performance in both 9-class and 12-class recognition, this can prove its generalization ability.
12-class recognition is more difficult because it tests the model’s few-shot learning capabilities. 9-class recognition is relatively simpler since the amount of data in each class is relatively sufficient.  
You can pick the appropriate task (or both) based on your approach and apply the corresponding train-test-split.

## Existing work using this Train-Test Split

## Train-Test Split for 9 classes
|Category|Training set| Test set|
| ---- | ---- | ---- |
|Dredger|Dredger_80__04_10_12_adricristuy.wav <br> Dredger_93__A__Draga_1.wav <br> Dredger_94__A__Draga_2.wav <br> Dredger_96__A__Draga_4.wav |Dredger_95__A__Draga_3.wav|
|Fishboat|Fishboat_73__23_07_13_H3_pesqMariCarmen.wav <br> Fishboat_74__23_07_13_H3_pesqSaladinoPrimero.wav <br> Fishboat_76__23_07_13_H3_pesquero2.wav|Fishboat_75__23_07_13_H3_pesquero1.wav|
|Motorboat|Motorboat_21__18_07_13_lanchaMotora.wav <br> Motorboat_26__19_07_13_Lancha.wav <br> Motorboat_33__19_07_13_lanchaDuda_Sale.wav <br> Motorboat_39__19_07_13_lanchaMotora_Entra.wav <br> Motorboat_45__19_07_13_yate_Sale.wav <br> Motorboat_51__23_07_13_H3_lancha2_interf.wav <br> Motorboat_52__23_07_13_H3_lancha3_interf.wav <br> Motorboat_70__23_07_13_H2_yatePeq.wav <br> Motorboat_77__23_07_13_H3_Planeadora.wav <br> Motorboat_79__23_07_13_H3_zodiac.wav|Motorboat_27__19_07_13_Lancha2.wav <br> Motorboat_50__23_07_13_H3_lancha1.wav <br> Motorboat_72__23_07_13_H3_lancha2.wav|
|Musselboat|Musselboat_46__23_07_13_H3_bateero1.wav <br> Musselboat_47__23_07_13_H2_bateero2.wav <br> Musselboat_49__23_07_13_H1_bateero4.wav <br> Musselboat_66__23_07_13_H3_Pesquerito2_Velero.wav|Musselboat_48__23_07_13_H3_bateero3_interf.wav|
|Naturalambientnoise|Naturalambientnoise_81__25_09_13_H3_corriente.wav <br> Naturalambientnoise_82__27_09_13_H3_lluvia.wav <br> Naturalambientnoise_84__27_09_13_H3_viento.wav <br> Naturalambientnoise_85__E__1L.wav <br> Naturalambientnoise_86__E__2M.wav <br> Naturalambientnoise_88__E__4L.wav <br> Naturalambientnoise_90__E__6H.wav <br> Naturalambientnoise_91__E__7H_N.wav|Naturalambientnoise_83__27_09_13_H3_oleaje.wav <br> Naturalambientnoise_87__E__3H.wav <br> Naturalambientnoise_92__E__8H_N.wav|
|Oceanliner|Oceanliner_16__10_07_13_mscOpera_InicioSalida.wav <br> Oceanliner_22__19_07_13_adventure_maniobra.wav <br> Oceanliner_23__19_07_13_adventure_parado.wav <br> Oceanliner_25__19_07_13_adventureOfTheSea_llegando.wav <br> Oceanliner_69__23_07_13_H2_costaVoyager.wav|Oceanliner_24__19_07_13_adventureFrenando_duda.wav <br> Oceanliner_71__23_07_13_H3_Discovery_UK_DUDA.wav|
|Passengers|Passengers_6__10_07_13_marDeCangas_Entra.wav <br> Passengers_7__10_07_13_marDeCangas_Espera.wav <br> Passengers_8__10_07_13_marDeOnza_Entra.wav <br> Passengers_10__10_07_13_marDeOnza_Sale.wav <br> Passengers_11__10_07_13_minhoUno_Entra.wav <br> Passengers_12__10_07_13_minhoUno_Sale.wav <br> Passengers_14__10_07_13_piraCies_Espera.wav <br> Passengers_17__10_07_13_visionSub_Entra.wav <br> Passengers_32__19_07_13_Arroios_llega.wav <br> Passengers_34__19_07_13_MarDeOnza_Llega.wav <br> Passengers_36__19_07_13_MinoUno_Sale.wav <br> Passengers_38__19_07_13_Arroios_Sale_2entran.wav <br> Passengers_40__19_07_13_MarDeCangas_Llega_Interf.wav <br> Passengers_41__19_07_13_MinoUno_Entra.wav <br> Passengers_43__19_07_13_PirataDeCies_Llega_Interf.wav <br> Passengers_54__23_07_13_H3_PirataSalvora_SALE1.wav <br> Passengers_59__23_07_13_H2_MarDeMouro.wav <br> Passengers_60__23_07_13_H3_MarDeCangas_LLEGA.wav <br> Passengers_61__23_07_13_H3_MarDeCangas_SALE-2.wav <br> Passengers_63__23_07_13_H3_MarDeOnza_LLEGA.wav <br> Passengers_64__23_07_13_H3_MarDeOnza_SALE.wav <br> Passengers_67__23_07_13_H3_PirataCiesSale.wav|Passengers_9__10_07_13_marDeOnza_Espera.wav <br> Passengers_13__10_07_13_piraCies_Entra.wav <br> Passengers_35__19_07_13_MarDeOnza_sale.wav <br> Passengers_42__19_07_13_PirataCies_Sale.wav <br> Passengers_55__23_07_13_H3_PirataSalvora_SALE2.wav <br> Passengers_62__23_07_13_H3_MarDeCangas_SALE.wav <br> Passengers_65__23_07_13_H3_MinhoUno_LLEGA.wav|
|RORO|RORO_18__18_07_13_AutoPrideEntra.wav <br> RORO_19__18_07_13_AutoprideMarchaAtras.wav <br> RORO_58__23_07_13_H2_EimskipReefer_Pesquerito1.wav|RORO_20__18_07_13_AutopridePrepManiobra.wav <br> RORO_78__23_07_13_H3_vikingChance.wav|
|Sailboat|Sailboat_37__19_07_13_Velero_Sale.wav <br> Sailboat_56__23_07_13_H3_velero1.wav <br> Sailboat_68__23_07_13_H3_veleroMarisol.wav|Sailboat_57__23_07_13_H3_velero2.wav|




## Train-Test Split for 12 classes

|Category|Training set| Test set|
| ---- | ---- | ---- |
|Dredger|Dredger_80__04_10_12_adricristuy.wav <br> Dredger_94__A__Draga_2.wav <br> Dredger_96__A__Draga_4.wav | Dredger_93__A__Draga_1.wav <br> Dredger_95__A__Draga_3.wav|
|Fishboat|Fishboat_73__23_07_13_H3_pesqMariCarmen.wav <br> Fishboat_74__23_07_13_H3_pesqSaladinoPrimero.wav <br> Fishboat_76__23_07_13_H3_pesquero2.wav|Fishboat_75__23_07_13_H3_pesquero1.wav|
|Motorboat|Motorboat_27__19_07_13_Lancha2.wav <br> Motorboat_33__19_07_13_lanchaDuda_Sale.wav <br> Motorboat_39__19_07_13_lanchaMotora_Entra.wav <br> Motorboat_45__19_07_13_yate_Sale.wav <br> Motorboat_50__23_07_13_H3_lancha1.wav <br> Motorboat_52__23_07_13_H3_lancha3_interf.wav <br> Motorboat_70__23_07_13_H2_yatePeq.wav <br> Motorboat_72__23_07_13_H3_lancha2.wav <br> Motorboat_77__23_07_13_H3_Planeadora.wav <br> Motorboat_79__23_07_13_H3_zodiac.wav|Motorboat_21__18_07_13_lanchaMotora.wav <br> Motorboat_26__19_07_13_Lancha.wav <br> Motorboat_51__23_07_13_H3_lancha2_interf.wav|
|Musselboat|Musselboat_47__23_07_13_H2_bateero2.wav <br> Musselboat_48__23_07_13_H3_bateero3_interf.wav <br> Musselboat_49__23_07_13_H1_bateero4.wav|Musselboat_46__23_07_13_H3_bateero1.wav <br> Musselboat_66__23_07_13_H3_Pesquerito2_Velero.wav|
|Naturalambientnoise| Naturalambientnoise_82__27_09_13_H3_lluvia.wav <br> Naturalambientnoise_83__27_09_13_H3_oleaje.wav <br> Naturalambientnoise_84__27_09_13_H3_viento.wav <br> Naturalambientnoise_86__E__2M.wav <br> Naturalambientnoise_87__E__3H.wav <br> Naturalambientnoise_89__E__5M.wav <br> Naturalambientnoise_90__E__6H.wav <br> Naturalambientnoise_91__E__7H_N.wav <br> Naturalambientnoise_92__E__8H_N.wav |Naturalambientnoise_81__25_09_13_H3_corriente.wav <br> Naturalambientnoise_85__E__1L.wav <br> Naturalambientnoise_88__E__4L.wav|
|Oceanliner|Oceanliner_16__10_07_13_mscOpera_InicioSalida.wav <br> Oceanliner_23__19_07_13_adventure_parado.wav <br> Oceanliner_25__19_07_13_adventureOfTheSea_llegando.wav <br> Oceanliner_69__23_07_13_H2_costaVoyager.wav <br> Oceanliner_71__23_07_13_H3_Discovery_UK_DUDA.wav |Oceanliner_22__19_07_13_adventure_maniobra.wav <br> Oceanliner_24__19_07_13_adventureFrenando_duda.wav |
|Passengers| Passengers_6__10_07_13_marDeCangas_Entra.wav <br> Passengers_8__10_07_13_marDeOnza_Entra.wav <br> Passengers_9__10_07_13_marDeOnza_Espera.wav <br> Passengers_10__10_07_13_marDeOnza_Sale.wav <br> Passengers_11__10_07_13_minhoUno_Entra.wav <br> Passengers_12__10_07_13_minhoUno_Sale.wav <br> Passengers_13__10_07_13_piraCies_Entra.wav <br> Passengers_17__10_07_13_visionSub_Entra.wav <br> Passengers_32__19_07_13_Arroios_llega.wav <br> Passengers_34__19_07_13_MarDeOnza_Llega.wav <br> Passengers_36__19_07_13_MinoUno_Sale.wav <br> Passengers_38__19_07_13_Arroios_Sale_2entran.wav <br> Passengers_41__19_07_13_MinoUno_Entra.wav <br> Passengers_42__19_07_13_PirataCies_Sale.wav <br> Passengers_53__23_07_13_H3_PirataSalvora_Llega1.wav <br> Passengers_55__23_07_13_H3_PirataSalvora_SALE2.wav <br> Passengers_59__23_07_13_H2_MarDeMouro.wav <br> Passengers_60__23_07_13_H3_MarDeCangas_LLEGA.wav <br> Passengers_62__23_07_13_H3_MarDeCangas_SALE.wav <br> Passengers_63__23_07_13_H3_MarDeOnza_LLEGA.wav <br> Passengers_64__23_07_13_H3_MarDeOnza_SALE.wav <br> Passengers_65__23_07_13_H3_MinhoUno_LLEGA.wav <br> Passengers_67__23_07_13_H3_PirataCiesSale.wav|Passengers_7__10_07_13_marDeCangas_Espera.wav <br> Passengers_14__10_07_13_piraCies_Espera.wav <br> Passengers_35__19_07_13_MarDeOnza_sale.wav <br> Passengers_40__19_07_13_MarDeCangas_Llega_Interf.wav <br> Passengers_43__19_07_13_PirataDeCies_Llega_Interf.wav <br> Passengers_54__23_07_13_H3_PirataSalvora_SALE1.wav <br> Passengers_61__23_07_13_H3_MarDeCangas_SALE-2.wav|
|Pilotship| Pilotship_29__19_07_13_practico.wav |Pilotship_30__19_07_13_practico2.wav|
|RORO|RORO_18__18_07_13_AutoPrideEntra.wav <br> RORO_19__18_07_13_AutoprideMarchaAtras.wav <br> RORO_58__23_07_13_H2_EimskipReefer_Pesquerito1.wav |RORO_20__18_07_13_AutopridePrepManiobra.wav <br> RORO_78__23_07_13_H3_vikingChance.wav|
|Sailboat|Sailboat_37__19_07_13_Velero_Sale.wav <br> Sailboat_57__23_07_13_H3_velero2.wav <br> Sailboat_68__23_07_13_H3_veleroMarisol.wav |Sailboat_56__23_07_13_H3_velero1.wav|
|Trawler|Trawler_28__19_07_13_NuevoRiaAldan.wav [15-125 second] |Trawler_28__19_07_13_NuevoRiaAldan.wav [125-163 second]|
|Tugboat|Tugboat_15__10_07_13_radaUno_Pasa.wav|Tugboat_31__19_07_13_RemolcadorArrancaPara.wav|

It is worth mentioning that the ``Trawler'' category has only one recording, so when dividing the training and test sets, this recording is divided into two non-overlapping segments, which can be downloaded at:  
https://github.com/xy980523/ShipsEar-An-Unofficial-Train-Test-Split/releases/download/main/Trawler_28__19_07_13_NuevoRiaAldan_train.wav  
https://github.com/xy980523/ShipsEar-An-Unofficial-Train-Test-Split/releases/download/main/Trawler_28__19_07_13_NuevoRiaAldan_test.wav
