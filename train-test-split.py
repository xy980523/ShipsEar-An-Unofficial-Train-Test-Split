import os
import shutil
import torchaudio

def class9_split(wavs):
    train_files, test_files = [], []
    for wav in wavs:
        # E.G., Tugboat_15__10_07_13_radaUno_Pasa.wav
        if wav.split('.')[-1] != 'wav':
            continue

        if int(wav.split('_')[1]) in [80,93,94,96,73,74,76,21,26,33,39,45,51,52,70,77,79,46,47,49,66,81,82,84,85,86,88,89,90,91,16,22,23,25,69,6,7,8,10,11,12,14,17,32,34,36,38,40,41,43,53,54,59,60,61,63,64,67,18,19,58,37,56,68]:
            train_files.append(wav)

        elif int(wav.split('_')[1]) in [95,75,27,50,72,48,83,87,92,24,71,9,13,35,42,55,62,65,20,78,57]:
            test_files.append(wav)
        else:
            print(wav,' is excluded!')

    return train_files, test_files

def class12_split(wavs):
    train_files, test_files = [], []
    for wav in wavs:
        # E.G., Tugboat_15__10_07_13_radaUno_Pasa.wav
        if wav.split('.')[-1] != 'wav':
            continue

        if int(wav.split('_')[1]) in [80,94,96,73,74,76,27,33,39,45,50,52,70,72,77,79,47,48,49,82,83,84,86,87,89,90,91,92,16,23,25,69,71,6,8,9,10,11,12,13,17,32,34,36,38,41,42,53,55,59,60,62,63,64,65,67,29,18,19,58,37,57,68,15]:
            train_files.append(wav)

        elif int(wav.split('_')[1]) in [93,95,75,21,26,51,46,66,81,85,88,22,24,7,14,35,40,43,54,61,30,20,78,56,31]:
            test_files.append(wav)
        else:
            print(wav,' is excluded!')
        
    return train_files, test_files


if __name__ == '__main__':
    wavs_path = '/user/shipsear_path/'
    wavs = os.listdir(wavs_path)

    ###################### 9-class train-test-split ######################
    train9_files, test9_files = class9_split(wavs)
    out9_path = '/user/shipsear_with_split-9class/'
    if not os.path.exists(out9_path):
        os.makedirs(os.path.join(out9_path,'train'))
        os.makedirs(os.path.join(out9_path,'test'))

    for x in train9_files:
        shutil.copy(os.path.join(wavs_path,x), os.path.join(out9_path,'train',x))
    for x in test9_files:
        shutil.copy(os.path.join(wavs_path,x), os.path.join(out9_path,'test',x))

    ###################### 12-class train-test-split ######################
    train12_files, test12_files = class12_split(wavs)
    out12_path = '/user/shipsear_with_split-12class/'
    if not os.path.exists(out12_path):
        os.makedirs(os.path.join(out12_path,'train'))
        os.makedirs(os.path.join(out12_path,'test'))

    for x in train12_files:
        shutil.copy(os.path.join(wavs_path,x), os.path.join(out12_path,'train',x))
    for x in test12_files:
        shutil.copy(os.path.join(wavs_path,x), os.path.join(out12_path,'test',x))

    # Cut clips for Trawler_28
    name = 'Trawler_28__19_07_13_NuevoRiaAldan.wav'
    waveform, sample_rate = torchaudio.load(os.path.join(wavs_path,name))
    duration = waveform.size(1) / sample_rate
    start_time = 125

    part1 = waveform[:, 15*sample_rate:start_time * sample_rate]
    part2 = waveform[:, start_time * sample_rate:]

    # Save as WAV file
    torchaudio.save(os.path.join(out12_path,'train',name.replace('.wav','_train.wav')), part1, sample_rate, bits_per_sample=16)
    torchaudio.save(os.path.join(out12_path,'test',name.replace('.wav','_test.wav')), part2, sample_rate, bits_per_sample=16)
