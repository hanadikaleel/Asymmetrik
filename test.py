import OCR


ex1 = "ASYMMETRIK LTD \nMike Smith \nSenior Software Engineer \n(410)555-1234 \nmsmith@asymmetrik.com"
ex2 = "Foobar Technologies \nAnalytic Developer \nLisa Haung \n1234 Sentry Road \nColumbia, MD 12345 \nPhone: 410-555-1234 \nFax: 410-555-4321 \nlisa.haung@foobartech.com"
ex3 = "Arthur Wilson \nSoftware Engineer \nDecision & Security Technologies \nABC Technologies \n123 North 11th Street \nSuite 229 \nArlington, VA 22209 \nTel: +1 (703) 555-1259 \nFax: +1 (703) 555-1200 \nawilson@abctech.com"
ex4 = "Hanadi Kaleel \nJunior Software Engineer \nASYMMETRIK LTD  \nhanadikaleel@gmail.com \n860-796-4965"
ex5 = "Mark Johnson \nJohnson & Johnson \nMjohnson@harvard.edu\n2407964965"
ex6 = "Jane Smith-Jones \nInstagram \ninfo@instagram.com\n(301)796-4965"

print("Example 1: \n\n" + ex1)
print("\n==>\n")
print(OCR.BusinessCardParser.getContactInfo(ex1))

print("\n\nExample 2: \n\n" + ex2)
print("\n==>\n")
print(OCR.BusinessCardParser.getContactInfo(ex2))

print("\n\nExample 3: \n\n" + ex3)
print("\n==>\n")
print(OCR.BusinessCardParser.getContactInfo(ex3))

print("\n\nExample 4: \n\n" + ex4)
print("\n==>\n")
print(OCR.BusinessCardParser.getContactInfo(ex4))

print("\n\nExample 5: \n\n" + ex5)
print("\n==>\n")
print(OCR.BusinessCardParser.getContactInfo(ex5))

print("\n\nExample 6: \n\n" + ex6)
print("\n==>\n")
print(OCR.BusinessCardParser.getContactInfo(ex6))
