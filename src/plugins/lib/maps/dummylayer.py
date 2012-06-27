# -*- python -*-
# -*- coding: utf-8 -*-
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2011-2012       Serge Noiraud
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id$

#-------------------------------------------------------------------------
#
# Python modules
#
#-------------------------------------------------------------------------
import os
import gobject

#------------------------------------------------------------------------
#
# Set up logging
#
#------------------------------------------------------------------------
import logging
_LOG = logging.getLogger("maps.dummylayer")

#-------------------------------------------------------------------------
#
# Gramps Modules
#
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#
# osmGpsMap
#
#-------------------------------------------------------------------------

try:
    import osmgpsmap
except:
    raise

class DummyLayer(gobject.GObject, osmgpsmap.GpsMapLayer):
    def __init__(self):
        """
        Initialize the dummy layer
        """
        gobject.GObject.__init__(self)

    def do_draw(self, gpsmap, gdkdrawable):
        """
        Draw the layer
        """
        pass

    def do_render(self, gpsmap):
        """
        Render the layer
        """
        pass

    def do_busy(self):
        """
        The layer is busy
        """
        return False

    def do_button_press(self, gpsmap, gdkeventbutton):
        """
        Someone press a button
        """
        return False

gobject.type_register(DummyLayer)

