

def recordUri():
	return "record/"+getValue("record_ID")

def recordIdentifierUri():
	return recordUri()+"/identifier"

def titleUri():
	return recordUri()+"/title"

def languageUri():
	if getValue("values"):
  		return "thesauri/language/"+getValue("values").lower().replace(' ','')

def objectTypeUri():
	return "thesauri/objecttype/"+getValue("values").lower().replace(' ','')
