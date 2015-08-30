#dependencies
import os
import mechanize

br = mechanize.Browser() #creates Mechanize browser object
directory = os.getcwd() #grabs current working directory

formName = "upload" #name of HTML form
mimeType = 'image/jpg' #MIME type of file to be uploaded
fileExtension = ".jpg" #extension of file to be uploaded
fileTotal = 0 # total files of fileExtension in directory
uploadedTotal = 0 #total files uploaded
errorTotal = 0 #total number of failed uploads

for filename in os.listdir(directory):

	if filename.endswith(fileExtension):
	
		#grab filename without extension
		fileWithoutExt = os.path.splitext(os.path.basename(filename))[0]
		#split name by spaces so that reports with several parts get uploaded correctly e.g. '20151503 part1' and '20151503 part2' to '20151503'
		file = fileWithoutExt.split(" ")[0]
		#get URL corresponding to file
		url = "http://example.com/view.php?view="+filename # URL
		fileTotal += 1
		
		try:
			br.open(url)
			br.select_form(name=formName)
			br.form.add_file(open(filename, 'rb'), mimeType, filename)
			br.submit()
			print filename+" uploaded to " +url
			uploadedTotal += 1
		#error handling
		except:
			pass
			errorTotal += 1
			print "Unexpected error occured when trying to upload "+filename+" to "+url

print "TOTAL "+fileExtension+" FILES IN DIRECTORY: "+str(fileTotal)			
print "TOTAL FILES UPLOADED: "+str(uploadedTotal)
print "ERRORS: "+str(errorTotal)
print "DONE. PRESS [ENTER] KEY TO EXIT"
raw_input()
