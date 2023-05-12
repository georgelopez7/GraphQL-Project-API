# Projects API (GraphQL)
![Group 4](https://github.com/georgelopez7/GraphQL-Project-API/assets/71076769/0d15f00e-40e0-4e0c-baa9-8f9691d0ea45)

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Technologies](#technologies)
- [Flask Infrastructure](#flask-infrastructure)
- [GraphQL Schema](#graphql-schema)
- [Mongo Database Schema](#mongo-database-schema)
- [Author Info](#author-info)

---

## Description

This project is a Flask API that provides access to my portfolio of projects stored in a MongoDB database. The API uses GraphQL to retrieve and query data based on specific programming languages.

Designed to be used in conjunction with my portfolio website, the API enables visitors to view my projects and filter them based on programming languages. This helps visitors get a better understanding of my skills and expertise in different technologies.

In addition, the API also includes an endpoint that is used in conjunction with a contact form on my portfolio website. This enables visitors to get in touch with me and provides a simple and effective way for me to manage communications with potential clients or collaborators.

For example:

A user can type *python* and all projects that involve Python will be retrieved.

[Back To The Top](#projects-api-grapghql)

--- 

## Technologies

- Python

    - **Flask** package

        Used to build the infrastructure of the API

- GraphQL

    Used to handle querying 

- MongoDB

    Used to store all the project data


[Back To The Top](#projects-api-grapghql)

---

## Flask Infrastructure

This Flask API serves two main purposes. Firstly, it provides a GraphQL endpoint that enables developers to retrieve project data from a MongoDB database. This endpoint is easy to use and can help developers quickly access and analyze the relevant project data.

Secondly, the API also includes an endpoint that is used in conjunction with a contact form on my portfolio website. This endpoint enables me to receive emails from people who visit my website and want to get in touch with me.

[Back To The Top](#projects-api-grapghql)

---

## GraphQL Schema


This GraphQL API has two main queries in the **schema.py** file. The first query retrieves all projects, while the second query collects projects based on a user-inputted language. Both queries are simple to use and can help developers efficiently retrieve project data from a MongoDB database based on their requirements.

[Back To The Top](#projects-api-grapghql)

---

## Mongo Database Schema


All projects are stored in a Mongo database, and the database schema can be seen in the diagram below:

![Blank diagram - Page 1](https://github.com/georgelopez7/GraphQL-Project-API/assets/71076769/5519f0a7-86df-4c5a-8eb4-9eea6e5893d8)

[Back To The Top](#projects-api-grapghql)

---


## Author Info

LinkedIn - [George Lopez](https://www.linkedin.com/in/george-benjamin-lopez/)

[Back To The Top](#projects-api-grapghql)
