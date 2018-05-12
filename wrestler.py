### Program Name: Wrestler
### Filename: wrestler.py
### Author: Ryan Ellis
### Due Date: 5/13/18

# dependicies
import sys

# file handling

def file_pull(a_file_object):



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
					if(rival.bface_heel == None):
						if(wrest.bface_heel == 'heel'):
							rival.bface_heel = 'babyface'
						else:
							rival.bface_heel = 'heel'
					else:
						if rival.bface_heel == wrest.bface_heel:
							print 'Impossible'
							return 0
					print 'Yes, possible'

			if rivalry_flag == True:
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

	wrest = Wrest_Graph()

	wrest.add_wrest('Mill')

	wrest.add_wrest('BAX')

	wrest.add_wrest_edge('Mill', 'BAX')

	wrest.rivalry_search()

main()