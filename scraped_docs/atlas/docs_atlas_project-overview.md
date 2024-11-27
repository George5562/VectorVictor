# Manage the Project Landing Page - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization / Project Access Manage the Project Landing Page On this page Project Overview Content Required Access Enable the Project Overview Disable the Project Overview The project overview is a landing page for your Atlas project that
displays modules that contain common Atlas actions. The
overview makes it easy to find resources and manage your
clusters from the Atlas home page. To navigate to the project overview, click Overview in the
sidebar in Atlas . If Atlas doesn't display an Overview option, you must first enable the overview for your
project. If you disable the project overview, Atlas displays Clusters as the project landing page. Project Overview Content Some of the modules that the project overview displays include but are
not limited to: Application Development The application development module provides resources to connect to
your clusters with the official MongoDB libraries.
If you've already connected to an app with a driver, Atlas displays
recent connections in this module. Note If you don't see your app listed, set the appName in your connection string to match your cluster name
and connect to your deployment. It may take up to one hour after
connection for your app to show on the project overview. For example, if your cluster is named myCluster , you would add &appName=myCluster as
shown in the following connection string: mongodb+srv://<db_username>:<db_password>@myCluster.abc12.mongodb.net/?retryWrites=true&w=majority&appName=myCluster Required Access To enable or disable the project overview, you must have Project Owner or Organization Owner access to Atlas . Enable the Project Overview Atlas enables the overview by default. You can reenable the
overview if you previously disabled it. Follow these steps to enable the project overview.
After you enable the overview, the Overview option
displays in the sidebar for all users in the project. 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 Toggle Project Overview to ON . Disable the Project Overview Follow these steps to disable the project overview. After you disable
the overview, the following changes apply for all users in the project: The Overview option doesn't display in the
sidebar for this project. Clusters becomes the project landing page. 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 Toggle Project Overview to Off . Back Settings Next Invitations
