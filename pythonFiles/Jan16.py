import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import glob
import csv
import Image
import random
barcodes = ['012546673624', '012546600262', '012546074247', '012546617536', '012546074407', '012546613682', '012546670050', '012546074834', '012546673099', '012546610476', '012546673716', '012546675758', '012546670449', '012546673730', '012546074339', '012546074025', '012546673020', '012546671217', '012546616744', '012546674379', '012546670326', '012546619592', '012546675871', '012546074902', '012546672559', '012546616447', '057700218051', '012546600200', '028029729405', '012546671224', '012546671347', '012546612197', '012546672016', '012546075190', '012546675451', '012546074742', '012546074919', '012546672504', '012546612692', '012546670036', '012546671576', '012546675369', '012546612296', '012546612050', '012546673754', '012546075589', '012546673518', '012546671231', '012546616492', '012546673044', '012546670388', '012546671538', '012546074049', '012546670302', '012546672412', '012546075374', '012546675857', '012546612678', '012546600040', '012546614689', '012546074759', '012546615563', '057700218174', '012546617642', '057700218204', '012546670258', '012546617604', '012546600347', '012546074254', '012546675642', '012546672597', '057700619179', '012546074766', '012546075473', '012546615488', '057700618967', '012546674751', '012546614658', '012546074896', '012546671316', '012546673778', '012546612685', '057700618493', '012546672801', '012546600101', '012546600026', '012546672511', '057700212424', '012546672078', '012546675666', '057700619155', '012546612319', '012546074018', '012546619615', '012546676045', '012546617680', '012546075091', '012546074704', '012546615952', '012546676199', '012546610599', '012546610452', '012546075336', '012546617529', '012546670463', '012546616119', '012546676281', '012546613477', '012546074391', '012546074551', '012546672849', '012546673082', '012546672573', '012546075381']
barcodes = barcodes[:20]
newBarcodes = []
for barcode in barcodes:
	newBarcodes.append(str(random.randint(1,9)) + barcode[1:])

barcodes = newBarcodes

objects = tuple(' ' * len(barcodes))
y_pos = np.arange(len(objects))
performance = barcodes
 
plt.bar(y_pos, performance, align='center')
plt.xticks(y_pos, objects)
plt.ylabel('Barcodes * 10^-12')
plt.title('Barcodes on my Walmart Receipt')
 
plt.savefig('testplot.png')