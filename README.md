# Tarassov-Nikita-HW1


Preparation:

    Register a GitHub account
    Fill link to the account in Google Doc. Join itmo-wad GitHub organization
    Create your GitHub profile (if you have nothing against it)

Frontend: create a static profile page about yourself (HTML + CSS)

    Profile page should have: heading, text, image, etc.
    You can choose any design of profile page that you like

Backend: using Python Flask to serve the frontend (profile page)


Basic part:

    Serve static profile page at default route ('/') (using any method you want)
    Serve images, CSS files as static resources

Advanced part:

    Serve profile page using render_template (might be with parameters on your choice)
    Serve profile page at '/profile' and redirect default route to it

README file:

    Short description about what have been done

Make Github page for your frontend part (with your own repository, not in itmo-wad organization)


After your account added to itmo-wad organization, create a new repository and upload your home to that repository.
Provide the link to that repository as submission for this assignment.


I used an html table to create profile page with some css styles for this table, in flask import render_template to render page and redirect to redirect from "/" default route to new "/profile" route
