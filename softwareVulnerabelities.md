# 4. Insecure Direct Object Reference

A direct object reference occurs when a developer exposes a reference to an internal implementation object, such as a file, directory, or a database key. Without an access control check or other protection, attackers can manipulate these references to acceess unauthorized data

http://example.com/projects/123

if after the url, can I see the other peoples project?

http://example.com/projects/124

# 5. Security Misconfiguration

Misconfigured web servers provide hackers with opportunities to abuse websites. Good security requires having a secure configuration defined and deployed for the application, frameworks, application server, web server, database server, and platform. Secure settings should be defined, implemented and maintained as defaults are often insecure. Additionally, software should be kept up to date.

Most web applications depend on some kind of a framework, such as Weblogic, Spring, ADF, Ruby on Rails, Open Source Libraries, JARs and JARs and JARs of fun..

# 6. Sensitive Data Exposure

Many web applications do not properly protect sensitive data, such as credit cards, tax IDs and authentication credentials. Attackers may steal or modify such weakly protected data to conduct credit card fraud, identity theft, or other crimes. Sensitive data deserves extra protection such as encrytion at rest or in transit, as well as special precautions when exchanged with the browser.

# 7. Missing Function Level Access Control

Most web applicaiton verify function level access rights before making that functionalty visible in the UI. However, applications need to perform the same access control checks on the server when each function is accessed. If requests are not verified, attackers will be able to forge requests in order to access functionality without proper authorization.

http://example.com/projects/123
http://example.com/user/getProjects

attacker can try

http://example.com/admin/getProjects
http://example.com/manager/getProjects

# 8. Cross-Site Request Forgery (CSRF)

A CSRF attack forces a logged-on victim's browser to send a forged HTTP request, including the victim's session cookie and any other automatically included authentication information, to a vulnerable web application. This allows the attacker to force the victom's browser to generate requests the vulnerable application thinks are legitimate requests from the victim.

http://example.com/myApp

than

<img src="http://example.com/myApp/deleteEverything"></img>

with JavaScript and XSS, evil sites can completely take over your browser, can browse around your intranet, log into bank accounts. Anything you are currently logged into.

# 9. Using Components with known vulnerabilities

Components, such as libraries, frameworks, and other software modules, almost always run with full priviledges. If a vulnerable component is exploited, such an attach can facilitate serious data loss or server takeover. Applications using components with known vulnerabilities may undermine application defenses and enable a range of possible attacks and impacts

# 10. Unvalidated Redirects and Forwards

Web applications frequently redirect and forward users to other pages and websits, and use untrusted data to determine the destination pages. Without proper validation, atteckers can redirect victims to phishing or malware sites, or use forward to access unauthorized pages.
