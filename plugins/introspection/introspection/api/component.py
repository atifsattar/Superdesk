'''
Created on Mar 4, 2012

@package: introspection
@copyright: 2011 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Provides the components introspection.
'''

from . import modelAdmin
from ally.api.config import service, call, query
from ally.api.type import IterPart
from ally.api.criteria import AsLike, AsBoolean

# --------------------------------------------------------------------

@modelAdmin
class Component:
    '''
    Provides the component data.
    '''
    Id = str
    Name = str
    Group = str
    Version = str
    Locale = str
    Description = str
    Loaded = bool
    Path = str
    InEgg = bool

# --------------------------------------------------------------------

@query
class QComponent:
    '''
    Provides the component query.
    '''
    name = AsLike
    group = AsLike
    version = AsLike
    locale = AsLike
    loaded = AsBoolean
    path = AsLike
    inEgg = AsBoolean

# --------------------------------------------------------------------

@service
class IComponentService:
    '''
    Provides services for ally components.
    '''

    @call
    def getById(self, id:Component.Id) -> Component:
        '''
        Provides the component based on the provided id.
        '''

    @call
    def getComponents(self, offset:int=None, limit:int=None, q:QComponent=None) -> IterPart(Component):
        '''
        Provides all the components.
        '''
