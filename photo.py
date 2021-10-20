#coding=utf-8

'''
1-將圖片轉化為陣列並存為二進位制檔案
2-從二進位制檔案中讀取數並重新恢復為圖片
'''

from __future__ import print_function
import numpy
import PIL.Image 
import pickle
import matplotlib.pyplot
import glob
import os

class Operation(object):
	image_base_path = "C:/temp/basket/images/"
	data_base_path = "C:/temp/basket/data/"

	def image_to_array(self,filenames):
		size = []
		n = filenames.__len__()#獲取圖片個數
		print("開始將圖片轉化為陣列")
		for i in range(n):
			result = numpy.array([]) #建立一個空的一維陣列
			image = PIL.Image.open(self.image_base_path+filenames[i])
			r,g,b = image.split() # rgb通道分離
			size.append(r.size)
			allsize = r.size[0]*r.size[1]
			print(i,r.size,allsize)
			# 注意：下面一定要reshpae(1024)使其變為一維陣列，否則拼接的資料會出現錯誤，導致無法恢復圖片
			r_arr = numpy.array(r).reshape(allsize)
			g_arr = numpy.array(g).reshape(allsize)
			b_arr = numpy.array(b).reshape(allsize)
			# 行拼接，類似於接火車；最終結果：共n行，一行3072列，為一張圖片的rgb值
			image_arr = numpy.concatenate((r_arr,g_arr,b_arr))
			result = numpy.concatenate((result,image_arr))

			result = result.reshape(1,allsize*3) # 將一維陣列轉化為n行3072列的二維陣列
			print("轉化陣列over，開始儲存為檔案")
			name = str(filenames[i]).replace('.jpg', '').replace('.png', '')
			file_path = self.data_base_path + f'{name}.bin'
			print(result)
			with open(file_path,mode='wb') as f:
				pickle.dump(result,f)
			size_path = self.data_base_path + f'{name}.txt'
			with open(size_path,mode='w',encoding='utf-8') as f:
				f.write(str(size[i]))
			print("儲存成功")
			print()

	def array_to_image(self,filename,size):
		with open(self.data_base_path + filename,mode='rb') as f:
			arr = pickle.load(f) #載入並反序列化資料
		rows = arr.shape[0] #rows=5
		#pdb.set_trace()
		#print("rows:",rows)
		arr = arr.reshape(rows,3,size[1],size[0])
		for index in range(rows):
			a = arr[index]
			#得到RGB通道
			r = PIL.Image.fromarray(a[0]).convert('L')
			g = PIL.Image.fromarray(a[1]).convert('L')
			b = PIL.Image.fromarray(a[2]).convert('L')
			image = PIL.Image.merge("RGB",(r,g,b))
			#顯示圖片
			matplotlib.pyplot.imshow(image)
			matplotlib.pyplot.show()
			#image.save(self.image_base_path + "result" + str(index) + ".png",'png')

if __name__ == "__main__":
	my_operator = Operation()
	images = []
	for file in glob.glob(my_operator.image_base_path+"*.jpg"):
		file = file.replace('C:/temp/basket/images\\','')
		images.append(file)

	my_operator.image_to_array(images)
	for file in glob.glob(my_operator.image_base_path+"*.jpg"):
		name = file.replace('C:/temp/basket/images\\','').replace('.jpg', '').replace('.png', '')
		with open(my_operator.data_base_path+name+'.txt',mode='r') as f:
			size = f.read()
			size = tuple(map(int, size.replace('(','').replace(')','').split(', ')))
			my_operator.array_to_image(f'{name}.bin', size)
