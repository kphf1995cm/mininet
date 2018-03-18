"""Fattree topology example



Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=fattree' from the command line.
"""

from mininet.topo import Topo

class FattreeTopo( Topo ):

    "Fattree topology example."

    #def __init__( self, *args, **params ):

    #	Topo(self,args,params)

    def build( self, podnum=2 ):
    	
    	self.podnum=podnum
     	self.coreSwitchNum=(podnum/2)*(podnum/2)
     	self.switchNum=5*self.coreSwitchNum
     	self.hostNum=self.coreSwitchNum*podnum

     	halfPodnum=podnum/2
     	aggrSwitchIndex=self.coreSwitchNum
     	edgeSwitchIndex=self.coreSwitchNum*3

     	curAggrSwitchIndex=0
     	curEdgeSwitchIndex=0

     	hosts=[]
     	switches=[]

     	# add host
     	for h in range(1,self.hostNum+1):
     		hosts.append(self.addHost('h%s' % h))

     	# add switch
     	for s in range(1,self.switchNum+1):
     		switches.append(self.addSwitch('s%s' % s))

     	# add aggr and edge switch bottom link
     	for i in range(self.podnum): # traverse every pod

     		for j in range(halfPodnum): # traverse every switch in pod i
     			
     			curAggrSwitchIndex=aggrSwitchIndex+i*halfPodnum+j
     			curEdgeSwitchIndex=edgeSwitchIndex+i*halfPodnum+j

     			for p in range(halfPodnum):

     				self.addLink(switches[curAggrSwitchIndex],switches[edgeSwitchIndex+i*halfPodnum+p])
     				self.addLink(switches[curEdgeSwitchIndex],hosts[i*self.coreSwitchNum+j*halfPodnum+p])

     	
     	# add core switch link

     	k_s=0
     	for i in range(self.coreSwitchNum): 

     		k=k_s
     		for j in range(self.podnum):

     			curAggrSwitchIndex=aggrSwitchIndex+j*halfPodnum+k
     			self.addLink(switches[i],switches[curAggrSwitchIndex])
     			
     			if k==halfPodnum-1:
     				k=0
     			else:
     				k=k+1

     		if k_s==halfPodnum-1:
     			k_s=0
     		else:
     			k_s=k_s+1


topos = { 'fattree': ( lambda: FattreeTopo() ) }
