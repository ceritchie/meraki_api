MERAKI_DASHBOARD_API_KEY = "YOUR_MERAKI_API_KEY_HERE"
import meraki
dashboard = meraki.DashboardAPI("YOUR_MERAKI_API_KEY_HERE")
my_orgs=dashboard.organizations.getOrganizations()


