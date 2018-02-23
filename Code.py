class Transportation(object):
   def __init__( self, start, end, distance ):
      if self.__class__ == Transportation:
         raise NotImplementedError
      self.start = start
      self.end = end
      self.distance = distance

   def find_cost( self ):
      raise NotImplementedError


class Walk( Transportation ):
   def __init__( self, start, end, distance ):
      Transportation.__init__( self, start, end, distance)
   def find_cost( self ):
      return 0

class Taxi( Transportation ):
   def __init__(self,start,end,distance):
      Transportation.__init__(self,start,end,distance)
   def find_cost(self):
      return 40*self.distance
      
class Train( Transportation ):
   def __init__(self,start,end,distance,station):
      Transportation.__init__(self,start,end,distance)
      self.station = station
   def find_cost(self):
      return 5*self.station
      
