import soundfile
data, samplerate = soundfile.read('out.wav')
soundfile.write('new.wav', data, samplerate, subtype='PCM_16')
print("done...")