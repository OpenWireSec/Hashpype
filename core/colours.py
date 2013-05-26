# This file is part of the HashPype Suite.
#
#    HashPype is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    HashPype is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with HashPype.  If not, see <http://www.gnu.org/licenses/>.
#
# Completer handles the auto-completion features for HashPype

class colours:
	
	def __init__(self):
				
		# Set up shell colours
		self.foreground_colours = { 'black' : '0;30',
								 'dark_gray' : '1;30',
								 'blue' : '0;34',
								 'light_blue' : '1;34',
								 'green' : '0;32',
								 'light_green' : '1;32',
								 'cyan' : '0;36',
								 'light_cyan' : '1;36',
								 'red' : '0;31',
								 'light_red' : '1;31',
								 'purple' : '0;35',
								 'light_purple' : '1;35',
								 'brown' : '0;33',
								 'yellow' : '1;33',
								 'light_gray' : '0;37',
								 'white' : '1;37' }
 			
		self.background_colours = { 'black' : '40',
								 'red' : '41',
								 'green' : '42',
								 'yellow' : '43',
								 'blue' : '44',
								 'magenta' : '45',
								 'cyan' : '46',
								 'light_gray' : '47' }
 
	# Returns coloured string
	def cstring(self, string, foreground_colour = None, background_colour = None):
		coloured_string = "";

		# Check if given foreground colour found
		if foreground_colour in self.foreground_colours.keys():
			coloured_string += '\033[' + self.foreground_colours[foreground_colour] + 'm'
			
		# Check if given background colour found
		if background_colour in self.background_colours.keys():
			coloured_string += '\033[' + self.background_colours[background_colour] + 'm'
			
 
		# Add string and end colouring
		coloured_string +=  string + '\033[0m'
 
		return coloured_string
		
 
	# Returns all foreground colour names
	def getfgcolours(self):
		return self.foreground_colours.keys()
	
 
	# Returns all background colour names
	def getbgcolours(self):
		return self.background_colours.keys()
	