import hashlib

def calculate_sha1(data_list):
    s2 = []
    #sha1_hash = hashlib.sha1()
    """for i in range(len(data_list)):"""
        

    for i in range(len(data_list)):
        if isinstance(data_list[i], str):
            d3 = data_list[i].encode('utf-8')

        # Create a new hash object for each iteration
        sha1_hash = hashlib.sha1()

        # Update the hash object with the input data
        sha1_hash.update(d3)

        # Get the hexadecimal representation of the hash
        s2.append(sha1_hash.hexdigest())

        """    for data in data_list:
        if isinstance(data, str):
            data = data.encode('utf-8')

        # Create a new hash object for each iteration
        sha1_hash = hashlib.sha1()

        # Update the hash object with the input data
        sha1_hash.update(data)

        # Get the hexadecimal representation of the hash
        s2.append(sha1_hash.hexdigest())
       """
    print(len(s2),"ithum")

    return s2

def words(a):
    with open(a, 'r', encoding='utf-8') as file:
        # Read the content of the file
        content = file.read()

    # Split the content into words
    words = content.split()
    words1=[]
    # Remove punctuation and convert to lowercase (optional)
    words = [word.lower() for word in words]

    
    # Get unique words using a set
    unique_words = list(set(words))

    # Print or use the unique words list as needed
    return unique_words

pwds= words('common.txt')
pwds1=['11111','1111111','11111','12345','54321','123456','654321','1234567','7654321','00000','000000','0000000','22222','222222','2222222']
pwds=pwds+pwds1
pwd2=[]
for k1 in pwds:
    if(len(k1)>=5 and len(k1)<=7):
        pwd2.append(k1)
#print(pwds)
salts = words ('salt.txt')
#print(salts)
salted=[]
salted1=[]
record2=[]
for i in range(len(pwd2)):
    for j in range(len(salts)):
        salted.append(pwd2[i]+salts[j])
        record2.append(pwd2[i]+salts[j]+" "+str(i)+","+str(j))
print("Length",len(record2))
record3=[]
for i in range(len(pwd2)):
    for j in range(len(salts)):
        salted.append(salts[j]+pwd2[i])
        record3.append(salts[j]+pwd2[i]+" "+str(j)+","+str(i))
print("Length2",len(record3))
"""

for i in pwd2:
    ii=0
    for j in salts:
        salted.append(i+j)
        record2.append(i+j+)
for i1 in pwd2:
    for j1 in salts:
        salted1.append(j1+i1)"""
#print(salted)       
s4=[]
hashes= calculate_sha1(salted)
print("hlooo",len(hashes))
hashes1=calculate_sha1(salted1)
#print(hashes)
#print(hashes.index('06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2'))
test=['fafa4483874ec051989d53e1e432ba3a6c6b9143','06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2','2834da08d58330d8dafbb2ac1c0f85f6b3b135ef',
'92e54f10103a3c511853c7098c04141f114719c1','437fbc6892b38db6ac5bdbe2eab3f7bc924527d9'
'f44f3b09df53c1c11273def13cacd8922a86d48c']
n=0
n1=0
for i in range(len(hashes)):
    for j in range(len((test))):
        if(hashes[i]==test[j]):
            print("The salt has been added before")
            print("Match")
            print("For hash 06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2")
            print("Salt used is www.exploringsecurity.com")
            print("Password is 54321")

            #print(hashes.index(h))
            #print(test.index(h1))
        else:
            n=n+1
record2[n].split()
record2[n][2].split(‘+’)
print(“For hash”,hashes[i])
print("Salt used is” record2[n][2][1])
print("Password used is” record2[n][2][0])

print (n)
for i in range(len(hashes1)):
    for j in range(len(test)):
        if(hashes1[i]==test[j]):
            print(hashes1[i])
            print(test[j])
            print("number2")
            print("Yes")
record3[n].split()
record3[n][2].split(‘+’)
print(“For hash”,hashes[i])
print("Salt used is” record3[n][2][1])
print("Password used is” record3[n][2][0])

print("Ithaan",n1)
print(record3[n1/2])