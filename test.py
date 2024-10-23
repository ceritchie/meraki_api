import meraki
API_KEY = "YOUR_MERAKI_API_KEY_HERE"
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizations()
print (response)

