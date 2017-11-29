formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one","two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right",
"But it didn't sing.", #double quote used because of the use of single quote in text
"So I said goodnight."
)