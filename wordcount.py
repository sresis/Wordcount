import sys
file = open(sys.argv[1])

# returns all words from file and gets rid of punctuation/capitals
def get_words(file):
	all_lines = []
	for line in file:
		line = line.rstrip()
		full_line = line.split(' ')
		for word in full_line:
			all_lines.append(word)

	return all_lines
# returns count of each word
def get_count(words):
	word_count = {}
	for item in words:
		item = item.rstrip('!@#$%^&*,.:?')
		item = item.lower()
		word_count[item] = word_count.get(item, 0) + 1
	return word_count

# returns sorted dictionary
def sort_dict(dictionary):
	sorted_dict = sorted((value, key) for (key, value) in dictionary.items())
	sorted_dict.reverse()
	new_list = {}
	for index, value in sorted_dict:
		new_list[value] = index
	return new_list

# main function. Prints word: word count for each word in the text
def main():
	words = get_words(file)
	word_count = get_count(words)
	final_list = sort_dict(word_count)
	for (key, value) in final_list.items():
		print(f'{key}: {value}')


main()



