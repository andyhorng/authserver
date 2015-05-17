
import socket

domains = [
    "www.facebook.com",
    "m.facebook.com",
    "connect.facebook.net",
    "business.facebook.com",
    "api.facebook.com",
    "api-read.facebook.com",
    "graph.facebook.com",
    "static.ak.fbcdn.net",
    "fbstatic-a.akamaihd.net",
    "static.ak.facebook.com",
    "s-static.ak.facebook.com",
    "facebook.com",

    "fbstatic-a.akamaihd.net",
    "fbcdn-profile-a.akamaihd.net",
    "fbcdn-sphotos-a-a.akamaihd.net",
    "fbcdn-creative-a.akamaihd.net",
    "fbexternal-a.akamaihd.net",

    "fbcdn-sphotos-b-a.akamaihd.net",
    "fbcdn-sphotos-c-a.akamaihd.net",
    "fbcdn-sphotos-d-a.akamaihd.net",
    "fbcdn-sphotos-e-a.akamaihd.net",
    "fbcdn-sphotos-f-a.akamaihd.net",
    "fbcdn-sphotos-g-a.akamaihd.net",
    "fbcdn-sphotos-h-a.akamaihd.net",

    "ngrok.io",
    "www.dailycred.com",
]

print "FirewallRuleSet global {"
print """
    # facebook ip range
    FirewallRule allow to 204.15.20.0/22
    FirewallRule allow to 69.63.176.0/20
    FirewallRule allow to 66.220.144.0/20
    FirewallRule allow to 66.220.144.0/21
    FirewallRule allow to 69.63.184.0/21
    FirewallRule allow to 69.63.176.0/21
    FirewallRule allow to 74.119.76.0/22
    FirewallRule allow to 69.171.255.0/24
    FirewallRule allow to 173.252.64.0/18
    FirewallRule allow to 69.171.224.0/19
    FirewallRule allow to 69.171.224.0/20
    FirewallRule allow to 103.4.96.0/22
    FirewallRule allow to 69.63.176.0/24
    FirewallRule allow to 173.252.64.0/19
    FirewallRule allow to 173.252.70.0/24
    FirewallRule allow to 31.13.64.0/18
    FirewallRule allow to 31.13.24.0/21
    FirewallRule allow to 66.220.152.0/21
    FirewallRule allow to 66.220.159.0/24
    FirewallRule allow to 69.171.239.0/24
    FirewallRule allow to 69.171.240.0/20
    FirewallRule allow to 31.13.64.0/19
    FirewallRule allow to 31.13.64.0/24
    FirewallRule allow to 31.13.65.0/24
    FirewallRule allow to 31.13.67.0/24
    FirewallRule allow to 31.13.68.0/24
    FirewallRule allow to 31.13.69.0/24
    FirewallRule allow to 31.13.70.0/24
    FirewallRule allow to 31.13.71.0/24
    FirewallRule allow to 31.13.72.0/24
    FirewallRule allow to 31.13.73.0/24
    FirewallRule allow to 31.13.74.0/24
    FirewallRule allow to 31.13.75.0/24
    FirewallRule allow to 31.13.76.0/24
    FirewallRule allow to 31.13.77.0/24
    FirewallRule allow to 31.13.96.0/19
    FirewallRule allow to 31.13.66.0/24
    FirewallRule allow to 173.252.96.0/19
    FirewallRule allow to 69.63.178.0/24
    FirewallRule allow to 31.13.78.0/24
    FirewallRule allow to 31.13.79.0/24
    FirewallRule allow to 31.13.80.0/24
    FirewallRule allow to 31.13.82.0/24
    FirewallRule allow to 31.13.83.0/24
    FirewallRule allow to 31.13.84.0/24
    FirewallRule allow to 31.13.85.0/24
    FirewallRule allow to 31.13.86.0/24
    FirewallRule allow to 31.13.87.0/24
    FirewallRule allow to 31.13.88.0/24
    FirewallRule allow to 31.13.89.0/24
    FirewallRule allow to 31.13.90.0/24
    FirewallRule allow to 31.13.91.0/24
    FirewallRule allow to 31.13.92.0/24
    FirewallRule allow to 31.13.93.0/24
    FirewallRule allow to 31.13.94.0/24
    FirewallRule allow to 31.13.95.0/24
    FirewallRule allow to 69.171.253.0/24
    FirewallRule allow to 69.63.186.0/24
    FirewallRule allow to 31.13.81.0/24
    FirewallRule allow to 179.60.192.0/22
    FirewallRule allow to 179.60.192.0/24
    FirewallRule allow to 179.60.193.0/24
    FirewallRule allow to 179.60.194.0/24
    FirewallRule allow to 179.60.195.0/24
    FirewallRule allow to 185.60.216.0/22
    FirewallRule allow to 45.64.40.0/22
    FirewallRule allow to 185.60.216.0/24
    FirewallRule allow to 185.60.217.0/24
    FirewallRule allow to 185.60.218.0/24
    FirewallRule allow to 185.60.219.0/24
    FirewallRule allow to 129.134.0.0/16
    FirewallRule allow to 157.240.0.0/16
    FirewallRule allow to 204.15.20.0/22
    FirewallRule allow to 69.63.176.0/20
    FirewallRule allow to 69.63.176.0/21
    FirewallRule allow to 69.63.184.0/21
    FirewallRule allow to 66.220.144.0/20
    FirewallRule allow to 69.63.176.0/20
    FirewallRule allow to 139.175.236.0/24
"""

for domain in domains:
    print "    # " + domain
    dedupe = []
    for info in socket.getaddrinfo(domain, 80):
        if len(info[4]) == 2:
            if info[4][0] not in dedupe:
                dedupe.append(info[4][0])

    for ip in dedupe:
        print "    FirewallRule allow to {}/32".format(ip)

print "}"
