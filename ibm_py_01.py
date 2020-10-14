A=(0,1,2,3)
B=list(A)
B[0]="A"
print(B)

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")
print(genres_tuple.index("disco"))
C_tuple=(-5, 1, -3)
sort_C_tuple = sorted(C_tuple)
print(sort_C_tuple)

A={1,2,3,4,5}
B={1,3,9, 12}

S={'A','B','C'}
U={'A','Z','C'}

print(U.union(S))

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
A = set(A)
print(A)
print(sum(A))
print(sum(B))

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)