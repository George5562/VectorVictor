# Data API and HTTPS Endpoints Deprecation - Atlas App Services


Docs Home / MongoDB Atlas / Atlas App Services / Data API [Deprecated] Data API and HTTPS Endpoints Deprecation On this page MongoDB Drivers and a Native Language Framework Node.js and Express Java and SpringBoot Python and FastAPI RESTHeart MongoDB Drivers and Cloud Native Functions AWS Lambda Azure Functions Google Cloud Run Functions Vercel, Node.js, and Express Partner Solutions Neurelo Hasura Snaplogic Considerations Get Help Atlas Device Sync, Atlas Edge Server, Data API, and HTTPS Endpoints are deprecated. Refer to the deprecation page for details . As of September 2024, Data API and HTTPS Endpoints are deprecated for Atlas App
Services. Data API and HTTPS Endpoints will reach end-of-life and be removed on September 30, 2025 . If you use Data API or HTTPS Endpoints, you should
migrate to alternative solution providers before the services are removed. The Data API and HTTPS Endpoints effectively enabled you to create a REST
interface to data in your Atlas clusters. Alternative solutions to consider: MongoDB Drivers and a Native Language Framework MongoDB Drivers and Cloud Native Functions Partner Solutions MongoDB Drivers and a Native Language Framework Leverage MongoDB Drivers with a native language framework of your choice to
create REST APIs in your self-managed app stack. Node.js and Express Express is a popular framework for building restful APIs, which can be leveraged
with the MongoDB native node driver to expose REST API endpoints for your
application. Getting Started with Express, Node, and MongoDB Express Documentation Java and SpringBoot Java Spring Boot is a framework that streamlines the creation of
production-ready Spring-based applications with minimal configuration. Getting Started with MongoDB and SpringBoot SpringBoot Documentation SpringBoot MongoDB Guide Python and FastAPI FastAPI is a modern, easy-to-learn, Python 3.6+ framework for building APIs
based on standard Python type hints. Getting Started With MongoDB and FastAPI FastAPI Documentation RESTHeart RESTHeart is an open source runtime that leverages MongoDB features via
REST, GraphQL, and WebSocket APIs to provide a persistent data API. RESTHeart
provides REST APIs for MongoDB features, built-in Authentication and Authorization,
and support for Java, Kotlin, JavaScript, and Typescript. RESTHeart documentation MongoDB Drivers and Cloud Native Functions Leverage MongoDB Drivers alongside serverless functions to perform CRUD
operations. AWS Lambda AWS Lambda is a compute service that runs your code in response to events and
automatically manages the compute resources, making it the fastest way to turn
an idea into a modern, production, serverless application. AWS Documentation Integrate MongoDB Atlas with AWS Lambda using the Node.js Driver Serverless Development with Lambda and the MDB Java Driver How to use PyMongo to Connect MongoDB Atlas with AWS Lambda Azure Functions Azure Functions is a serverless solution that allows you to write less code,
maintain less infrastructure, and save on costs. Instead of worrying about
deploying and maintaining servers, the cloud infrastructure provides all the
up-to-date resources needed to keep your applications running. Azure Documentation Integrate Atlas with Azure Functions Tutorial with the .Net Driver for CRUD Operations Getting Started with MongoDB Atlas and Azure Functions using .Net and C# Google Cloud Run Functions Cloud Run is a managed compute platform that enables you to run containers that
are invocable via requests or events. GCP documentation Vercel, Node.js, and Express Vercel is a cloud platform that helps developers build, scale, and secure web
applications. Getting Started with Express, Node, and MongoDB How to Deploy an Express.js Application to Vercel Express Documentation Partner Solutions Below are MongoDB partners that offer best-in-class solutions for exposing REST
APIs to MongoDB. Neurelo Neurelo is a platform for developers designed to simplify working with
databases. It provides a powerful database abstraction with an API-first
approach, instantly transforming databases into REST and GraphQL APIs. Neurelo
offers features such as building and managing schemas with Text-to-Schema
support, fully-documented REST and GraphQL APIs (with SDKs) generated from your
schema with an API  playground, custom API endpoints for complex queries with
Text-to-MQL support, multiple CI/CD environments, schema-aware mock data
generation, and more. This abstraction layer enables developers to program with databases through
APIs, simplifying communication between the application and the database and
making it easier and faster to integrate databases into their applications. Refer to Neurelo REST API MongoDB Atlas Migration Guide to learn more. Hasura Hasura empowers developers to rapidly build and deploy GraphQL and REST APIs on
MongoDB and many other data sources. By radically cutting down API development
times, Hasura enables rapid access to data for next-gen applications and
services, and enables enterprises to shorten time to market on data-powered
products and features. Refer to Hasura MongoDB GraphQL API Migration Guide to learn more. Snaplogic Snaplogic provides an integration platform for connecting cloud data sources. Refer to MongoDB Snap Pack documentation to learn more. Considerations Migrating to an alternative solution implies that you will no longer have access
to the auxiliary features provided by Atlas App Services. Depending on which of
these features you use, you'll need to implement the equivalent features on your
new solution. This process can vary in complexity based on how extensively you
rely on these features. When evaluating the alternative solutions, consider the
following: Atlas Functions Global Context would no longer be
available Global Modules would need to be re-mapped
to Node and BSON packages before use Neither Bearer or Credential Headers-based Authentication would be available Values and Secrets will no longer be available App Services Data Access Permissions will no longer be
available Get Help Please contact our support team through the MongoDB Support Portal or your Account Executive. Back Data API [Deprecated] Next Data API Endpoints [Deprecated]
