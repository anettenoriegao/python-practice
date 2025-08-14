# 1. Split the values into individual values
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)

# 2. Split the lyrics by line using split()
lyrics = """ 
Katie Casey was baseball mad, 
Had the fever and had it bad. 
Just to root for the home town crew, 
Ev'ry sou 
Katie blew. 
On a Saturday her young beau 
Called to see if she'd like to go 
To see a show, but Miss Kate said "No, 
I'll tell you what you can do:" 
""" 
lyrics_split = lyrics.split("\n")
print(lyrics_split)

# 3. Split the lyrics by line using something other than split()
changed_values = lyrics.splitlines()
print(changed_values)

