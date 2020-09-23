def find_genre(triller,comedy,movie):
	for i in thriller:
		if i.upper() == movie.upper():
			print("It is a thriller")
			return
	for i in comedy:
		if i.upper() == movie.upper():
			print("It is a comedy")
			return 
	print("It's neither comedy nor thriller")

thriller=["Dark","Midhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]
print("Enter the name of the movie:")
find_genre(thriller,comedy,movie)