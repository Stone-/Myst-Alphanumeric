# xDniConversions.py #

'''
Create a new KI /command that takes a descimal integer. Then displays the OTStandard spelling as a status message.

questions:
    #: Should this display the text "D'ni OTS = " or just display the spelled number?  I dont know how to do the localization stuff.
    
    #: Would def DecimalToOts be in its own file xDniConversions.py?  or just included at the bottom of xKIChat.CommandsProcessor?
'''


#################################################
# xKIConstants.py

## Constants for KI Chat commands.
class kCommands:
    EasterEggs = {"/look" : "LookAround",
                  "/get feather" : "GetFeather",
                  "/look in pocket" : "LookForFeathers"}
    DniConversions = {"/decimal" : "DecimalToOts"}


#################################################
# xKIChat.py

## Processes KI Chat commands.
class CommandsProcessor:

    ## Link the processor with the chat manager.
    def __init__(self, chatMgr):

        self.chatMgr = chatMgr

    ## Called when the processor needs to process a message.
    # Returns the appropriate message and performs all the necessary operations
    # to apply the command.
    def __call__(self, message):

        msg = message.lower()

        # Load all available commands.
        commands = dict()
#        commands.update(kCommands.Localized)
#        if PtGetAgeName() == "Jalak":
#            commands.update(kCommands.Jalak)
#        if PtIsInternalRelease():
#            commands.update(kCommands.Internal)
#        commands.update(kCommands.EasterEggs)
        commands.update(kCommands.DniConversions)

        # Does the message contain a standard command?
        for command, function in commands.items():
            if msg.startswith(command):
                theMessage = message.split(" ", 1)
                if len(theMessage) > 1 and theMessage[1]:
                    params = theMessage[1]
                else:
                    params = None
                getattr(self, function)(params)
                return None

    ''' ... '''

    #~~~~~~~~~~~~~~~~~#
    # Dni Conversions #
    #~~~~~~~~~~~~~~~~~#

    ## Display the OTS spelling of a decimal integer in chat.
    def DecimalToOts(self, decimal):
        "decimal: str -> None"
        
        zero = 'roon'
        stems = ('', 'fah', 'bree', 'sehn', 'tor',
                 'vaht', 'vahgahfah', 'vahgahbree', 'vahgahsen', 'vahgahtor',
                 'nayvoo', 'naygahfah', 'naygahbree', 'naygahsen', 'naygahtor',
                 'heebor', 'heegahfah', 'heegahbree', 'heegahsen', 'heegahtor',
                 'rish', 'rigahfah', 'rigahbree', 'rigahsen', 'rigahtor')
        suffixes = ('', 'see', 'rah', 'lahn', 'mel', 'blo')

        message = "D'ni OTS: {}"

        result = []
        if decimal.isdigit():
            decimal = int(decimal)
        else:
            self.chatMgr.DisplayStatusMessage('Sorry: Must be a positive integer.')
            return
        if decimal > 244140624:
            self.chatMgr.DisplayStatusMessage(("Sorry: 244,140,624 is the largest"
                " decimal that can be represented alphabeticly in D'ni."))
            return

        if decimal == 0:
            self.chatMgr.DisplayStatusMessage(message.format(zero))
            return
        i = 0
        while decimal > 0:
            index = decimal % 25
            if index:
                result.insert(0, stems[index] + suffixes[i])
            decimal = decimal // 25
            i += 1
        self.chatMgr.DisplayStatusMessage(message.format(','.join(result)))


#################################################
#  fake chatMgr so this will run

class chatMgr:
    def DisplayStatusMessage(x):
        print(x)

CommandsProcessor(chatMgr)('/decimal 233')

