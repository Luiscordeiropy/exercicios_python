n = float(input('digite uma distãncia em metros:'))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('{}Km \n {}Hm \n {}Dam \n {:.0f}Dm \n {:.0f}Cm \n {:.0f}mm'.format(km, hm, dam, dm, cm, mm))
