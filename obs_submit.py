#!/usr/bin/env python3
#
# Copyright (C) 2022
#	Written by Nasrun (Nas) Hayeeyama
#

VERSIONNUMBER = 'v1.0'
PROGRAM_DESCRIPTION = "For submit to obs"

########################################################
#
#	STANDARD IMPORTS
#

import sys
import os

import argparse
import logging

import asyncio

import pprint

import simpleobsws

########################################################
#
#	LOCAL IMPORTS
#

########################################################
#
#	Standard globals
#

########################################################
#
#	Program specific globals
#

MaximumNumCharacter = len( 'xxxxxxxxxxxxxxxxxxxxxxxxxx' )

########################################################
#
#	Helper functions
#

########################################################
#
#	Class definitions
#

########################################################
#
#	Function bodies
#

async def ping( ws ):
    '''
    '''

    await ws.connect() # Make the connection to OBS-Websocket
    result = await ws.call('GetVersion') # We get the current OBS version. More request data is not required
    pprint.pprint(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(1)
    await ws.disconnect()

async def request( ws, text ):
    ''''''

    await ws.connect() # Make the connection to OBS-Websocket

    

    data = {"sourceName": "text", "sourceSettings": {"text": text}}
    result = await ws.call('SetSourceSettings', data) # Make a request with the given data    
    pprint.pprint(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(1)
    await ws.disconnect()

async def request_position( ws ):
    ''''''

    await ws.connect() # Make the connection to OBS-Websocket

    

    data = { "scene-name" : "Scene", "item": "text" }
    result = await ws.call('GetSceneItemProperties', data) # Make a request with the given data    
    pprint.pprint(result) # Print the raw json output of the GetVersion request
    await asyncio.sleep(1)
    await ws.disconnect()

########################################################
#
#	main
#	
def main():
    
    #	initial parser instance
    parser = argparse.ArgumentParser( description=PROGRAM_DESCRIPTION )
    parser.add_argument( 'text', type=str,
                            help="text to submit, less than or equal 26 characters" )


    #########################################################
    #
    #		set python logger
    #

    logger = logging.getLogger( parser.prog )
    logger.setLevel( logging.INFO )
    
    formatter = logging.Formatter( '[%(levelname)s] : %(message)s' )
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel( logging.INFO )
    consoleHandler.setFormatter( formatter )

    logger.addHandler( consoleHandler )

    #########################################################
    #
    #		get option and argument
    #

    args = parser.parse_args()

    textSubmit = args.text
    
    # if( len( textSubmit ) > MaximumNumCharacter ):
    #     logger.error( "Your submit is more than maximum characters ({})".format( MaximumNumCharacter ) )
    #     sys.exit(-1)

    #   Normalize text
    # remainNumChar = MaximumNumCharacter - len( textSubmit )
    # if remainNumChar >= 1:
    #     blockStr = ' ' * MaximumNumCharacter
    #     x = ( remainNumChar // 2 )
    #     startIdx = x 
    #     endIdx = MaximumNumCharacter - x
    #     print( remainNumChar )
    #     print(startIdx)
    #     print(endIdx)
    #     textSubmit = blockStr[:startIdx] + textSubmit + blockStr[endIdx:]


    loop = asyncio.get_event_loop()
    ws = simpleobsws.obsws( host='127.0.0.1', 
                            port=4444, 
                            password='test', 
                            loop=loop) # Every possible argument has been passed, but none are required. See lib code for defaults.

    loop.run_until_complete( request( ws, textSubmit ) )


########################################################
#
#	call main
#

if __name__=='__main__':
    main()

