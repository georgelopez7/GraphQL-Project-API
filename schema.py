from graphene import ObjectType, String, Schema, List, Int
from pymongo import MongoClient

client = MongoClient("<mongo-client>")
db = client["projects"]
collection = db["project-names"]

class Project(ObjectType):
    pro_id = Int()
    name = String()
    description = String()
    language = String()
    GithubLink = String()
    WebsiteLink = String()

class Query(ObjectType):
    projects = List(Project)
    projects_by_language = List(Project, language=String())

    def resolve_projects(self, info):
        results = collection.find()
        return [Project(pro_id=r['ProjectID'],name=r['ProjectName'], description=r['ProjectDescription'], language=r['ProgrammingLanguage'], GithubLink=r['ProjectLink'], WebsiteLink=r['WebsiteLink']) for r in results]
    
    def resolve_projects_by_language(self, info, language):
        results = collection.find({"ProgrammingLanguageLower": {"$regex": language.lower()}})
        return [
            Project(
                pro_id=r['ProjectID'],
                name=r["ProjectName"],
                description=r["ProjectDescription"],
                language=r["ProgrammingLanguage"],
                GithubLink=r['ProjectLink'], 
                WebsiteLink=r['WebsiteLink']
            )
            for r in results
        ]

schema = Schema(query=Query)
