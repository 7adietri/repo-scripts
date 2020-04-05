# -*- coding: utf-8 -*-
from __future__ import absolute_import
from kodi_six import xbmc
from kodi_six import xbmcgui
from kodi_six import xbmcaddon


def main():
    if xbmc.getInfoLabel('Window(10000).Property(script.plex.service.started)'):
        # Prevent add-on updates from starting a new version of the addon
        return

    xbmcgui.Window(10000).setProperty('script.plex.service.started', '1')

    if xbmcaddon.Addon().getSetting('kiosk.mode') == 'true':
        xbmc.log('script.plex: Starting from service (Kiosk Mode)', xbmc.LOGNOTICE)
        xbmc.executebuiltin('RunScript(script.plex)')


if __name__ == '__main__':
    main()
