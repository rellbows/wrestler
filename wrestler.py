### Program Name: Wrestler
### Filename: wrestler.py
### Author: Ryan Ellis
### Due Date: 5/13/18

# dependicies
import sys

# file handling/data loading

def data_load(file_object, a_graph_object):

	# get wrestlers and rivalries from object. strip out the 'solutions'
	# bits at the end of the file

	file_data = []

	for line in file_object:
		if line == '\r\n':
			break
		else:
			file_data.append(line.strip())

	# load the data from the file into the graph object

	num_wrests = int(file_data[0])
	num_rivalries = int(file_data[num_wrests + 1])

	for wrest in file_data[1:(num_wrests + 1)]:
		a_graph_object.add_wrest(wrest)

	for rivalry in file_data[(num_wrests + 2):]:
		parent_child = rivalry.split(' ')
		a_graph_object.add_wrest_edge(parent_child[0], parent_child[1])

# the meat and potatoes

class Wrest_Graph:

	def __init__(self):
		self.wrest_graph = []

	def add_wrest(self, a_wrest_name):
		new_wrest = Wrest_Vert(a_wrest_name)
		self.wrest_graph.append(new_wrest)

	def get_wrest_index(self, a_wrest_name):
		for i, wrest in enumerate(self.wrest_graph):
			if(a_wrest_name == wrest.name):
				return i
		return -1

	def get_wrest_name(self, a_wrest_index):
		return self.wrest_graph[a_wrest_index].name

	def add_wrest_edge(self, parent_wrest, child_wrest):
		parent_index = self.get_wrest_index(parent_wrest)
		child_index = self.get_wrest_index(child_wrest)
		if(parent_index == -1 or child_index == -1):
			print "Invalid name(s)."
		else:
 			self.wrest_graph[parent_index].add_wrest_edge(child_index)

	def rivalry_search(self):
		if(len(self.wrest_graph) > 1):

			# flag used to ensure there is at least 1 rivalry
			rivalry_flag = False

			self.wrest_graph[0].bface_heel = 'babyface'

			for wrest in self.wrest_graph:
				for rival_index in wrest.wrest_edges:

					# proves there is at least 1 rivalry
					rivalry_flag = True

					rival = self.wrest_graph[rival_index]

					# wrestler and/or rival don't have type specified
					if(wrest.bface_heel == None and rival.bface_heel == None):
						wrest.bface_heel = 'babyface'
						rival.bface_heel = 'heel'
					elif(wrest.bface_heel == None and rival.bface_heel != None):
						if(rival.bface_heel == 'babyface'):
							wrest.bface_heel = 'heel'
						else:
							wrest.bface_heel = 'babyface'
					elif(wrest.bface_heel != None and rival.bface_heel == None):
						if(wrest.bface_heel == 'heel'):
							rival.bface_heel = 'babyface'
						if(wrest.bface_heel == 'babyface'):
							rival.bface_heel = 'heel'
					elif rival.bface_heel == wrest.bface_heel:
						print 'Impossible'
						return 0

			if rivalry_flag == True:
				print 'Yes, possible'
				babyfaces = [x.name for x in self.wrest_graph if x.bface_heel == 'babyface']
				print 'Babyfaces:'
				print babyfaces
				heels = [y.name for y in self.wrest_graph if y.bface_heel == 'heel']
				print 'Heels:'
				print heels
				return 1
			else:
				print 'Opps! There are no rivalries listed.'
				return 0
		else:
			print 'Opps! You must have at least 2 wrestlers to find rivalries.'
			return 0

class Wrest_Vert:

	def __init__(self, a_wrest_name):
		self.name = a_wrest_name
		self.bface_heel = None
		self.wrest_edges = []

	def add_wrest_edge(self, a_wrest_index):
		self.wrest_edges.append(a_wrest_index)

def main():
	''''driver code'''

	# file handling

	file_name = sys.argv[1]

	file_object = open(file_name)

	# create graph and load with data

	wrest = Wrest_Graph()

	data_load(file_object, wrest)

	file_object.close()

	# run search

	wrest.rivalry_search()

main()