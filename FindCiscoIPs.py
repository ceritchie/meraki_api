
# Import "meraki" to allow Meraki function calls
import meraki
API_KEY = "YOUR_MERAKI_API_KEY_HERE"

# Import "datetime" to get current date and time
import datetime

#Dashboard Information
dashboard = meraki.DashboardAPI(API_KEY)

# ///////// Start Definition of Script Constants ////////////////
# api_key = Unique API key generated on a per Meraki User basis
# org_id = Unique organization ID of organization you want to query

API_KEY = "YOUR_MERAKI_API_KEY_HERE"
ORG_ID = "3506-6257"



# Get the current list of networks from your Organization
current_networks = meraki.getnetworklist(API_KEY,ORG_ID)


# Establish when "now" is, used to create the file name for output
now = datetime.datetime.now()

# Create/Name the output file with year, month, day and hour minutes
filename = now.strftime("%Y-%m-%d %H.%M") + ".txt"

# Open the file for output
f = open(filename,"w+")

# "i" will be used to increment through each "network" in the Organization
i = 0

for i in range(len(current_networks)):

    # Output to console the Name and ID of the current network
    print("Network Name:" + current_networks[i]['name'])
    print("Network ID:" + current_networks[i]['id'])

    curr_net_id = current_networks[i]['id']
    curr_net_devices = meraki.getnetworkdevices(api_key,curr_net_id)

    # Write to the output file the 'name' of the network and add a comma
    f.write(current_networks[i]['name'])
    f.write(",")

    # Checks for Meraki devices on this network, if there are no devices output to file "No Devices Present"
    if len(curr_net_devices) == 0:
        f.write("No devices Present")
        f.write("\n")

    # "j" will be used to increment through each "device" on this network
    j = 0

    for j in range(len(curr_net_devices)):
        # Output to console the serial number of the device
        print ("Device Serial:" +curr_net_devices[j]['serial'])
        curr_clients = meraki.getclients(api_key,curr_net_devices[j]['serial'])


        # Checks for clients attached to this device, if no clients present output the name, model and serial of the
        # device as well as the message "No Clients". Also catch the error that comes up in case this is a device for
        # which clients are not relevant, e.g. MV camera's.
        if len(curr_clients) == 0 or curr_clients[0] == "Invalid device type":
            # Output to console "No Clients" message
            print ("No clients")

            # Output to file "name", "model", "serial" of the device as well as "No Clients" message
            f.write(current_networks[i]['name'])
            f.write(',')
            f.write(curr_net_devices[j]['model'])
            f.write(',')
            f.write(curr_net_devices[j]['serial'])
            f.write(",")
            f.write("No Clients")
            f.write("\n")

        # Only list the clients if there are any.
        else:
            # "k" will be used to increment the number of clients on each device
            k = 0

            for k in range(len(curr_clients)):
                # Output to console "description" and "mac" of the client
                print (curr_clients[k]['description'],',',curr_clients[k]['mac'])

                # Output to file "name", "model", "serial" of the device as well as the "description" and "mac"
                # of the client
                f.write(current_networks[i]['name'])
                f.write(',')
                f.write(curr_net_devices[j]['model'])
                f.write(',')
                f.write(str(curr_net_devices[j]['name']))
                f.write(',')
                f.write(curr_net_devices[j]['serial'])
                f.write(',')
                f.write(str(curr_clients[k]['description']))
                f.write(",")
                f.write(curr_clients[k]['ip'])
                f.write("\n")

                # Increment "k" to move onto next client on current device
                k = k + 1

        # Increment "j" to move onto next device on current Network
        j = j + 1
    # Increment "i" to move onto next network in Organization
    i = i + 1

# Close the output file
f.close()
