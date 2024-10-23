import meraki
# ///////// Start Definition of Script Constants ////////////////
# api_key = Unique API key generated on a per Meraki User basis
# org_id = Unique organization ID of organization you want to query
#
#api_key = 'YOUR_PERSONAL_API_KEY_IN_MERAKI'
#org_id = 'YOUR_ORG_ID'

dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizations(net_id)
