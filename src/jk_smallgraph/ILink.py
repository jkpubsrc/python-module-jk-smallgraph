

import os
import typing


from .INode import INode






class ILink(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def linkID(self) -> int:
		raise NotImplementedError()
	#

	@property
	def fromNode(self) -> INode:
		raise NotImplementedError()
	#

	@property
	def toNode(self) -> INode:
		raise NotImplementedError()
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

#







