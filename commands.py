import twilio.twiml
from api import searchForRestroom


commands = {}

def reply(response):
    resp = twilio.twiml.Response()
    resp.message(response)
    return str(resp)

def handleUnknown(message):
    """UNKNOWN - failsafe"""
    return reply("Sorry didn't get that. Text HELP for commands")

def handleNoneFound(message):
    """no restrooms were found"""
    return reply("Sorry, there were no restrooms found. Make sure the address was entered correctly.")

def restroom(restroom):
    """pretty prints a restrooms info"""
    bath_str = "Closest Restroom: %s, %s, %s, %s" % (restroom['name'],
                                                     restroom['street'],
                                                     restroom['city'],
                                                     restroom['state'])
    return reply(bath_str)

def handleSearch(message):
    """Enter a human readable address to get the nearest restroom"""
    query = message.body
    if len(query) > 0 and query.split()[0].lower() == "search":
        query = query[1:]
    restrooms = searchForRestroom(query)

    if len(restrooms) < 1:
        return handleNoneFound()

    restroom = restrooms[0]
    return restroom(restroom)

def handleHelp(message, commandList):
    """HELP - list of commands"""
    listOfCommands = ", ".join(commandList)
    return reply("Text an address to this number in order to find the nearest access to a safe restrooom")


commands = {
    'unknown': handleUnknown,
    'help': handleHelp,
    'search': handleSearch
}


if __name__ == "__main__":
    restrooms = searchForRestroom("Portland, Oregon")
    restroom = restrooms[0]
    bath_str = "Closest Restroom: %s, %s, %s, %s" % (restroom['name'],
                                                     restroom['street'],
                                                     restroom['city'],
                                                     restroom['state'])
    print bath_str
