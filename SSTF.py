# Kelompok :
# 1. Farrel Ardiyanto Saputro  / 71210702
# 2. Christophorus Adyatma WSN / 71210771
# 3. Nathanael Vito Kristianto / 71210681
# 4. Nicholas Marcell Kusumo / 71210680
# 5. Kezia Trifena Kurniani / 71210715
# 6. Melisa Wijaya / 71210714

# Program implementasi algoritma SSTF (Shortest Seek Time First)

# UNTUK CARA PENGGUNAAN PROGRAM INI, HANYA TINGGAL DI RUN


# Menghitung perbedaan masing-masing posisi kepala
def calculateDifference(queue, head, diff):
	for i in range(len(diff)):
		diff[i][0] = abs(queue[i] - head)
	
# temukan trek yang belum diakses pada jarak minimum dari kepala
def findMin(diff):
	index = -1
	minimum = 999999999
	for i in range(len(diff)):
		if (not diff[i][1] and
				minimum > diff[i][0]):
			minimum = diff[i][0]
			index = i
	return index
	
def shortestSeekTimeFirst(request, head):			
		if (len(request) == 0):
			return
		l = len(request)
		diff = [0] * l
		
		# menginisialisasi array
		for i in range(l):
			diff[i] = [0, 0]
		
		# hitung jumlah total operasi seek	
		seek_count = 0
		
		# menyimpan urutan dimana akses disk dilakukan
		seek_sequence = [0] * (l + 1)
		
		for i in range(l):
			seek_sequence[i] = head
			calculateDifference(request, head, diff)
			index = findMin(diff)
			diff[index][1] = True
			seek_count += diff[index][0]
			head = request[index]
	
		# untuk trek yang terakhir diakses
		seek_sequence[len(seek_sequence) - 1] = head
		print("Total head movement =", seek_count,"cylinders")	
		print("Head starts at", seek_sequence[0])
		
		# print urutannya
		print("Queue = ", end = " ")
		for i in range(l + 1):
			if i != 0:
				if i != len(seek_sequence)-1:
					print(seek_sequence[i], end =", ")
				else:
					print(seek_sequence[i], end =" ")
	

# Output
if __name__ =="__main__":
	proc = [176, 79, 34, 60, 92, 11, 41, 114]
	shortestSeekTimeFirst(proc, 50)

	# variabel proc adalah daftar sequence
	# parameter kedua pada fungsi shortestSeekTimeFirst adalah head start position
