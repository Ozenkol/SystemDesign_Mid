import { ApolloServer } from "apollo-server"; 
import { driver as _driver, auth } from "neo4j-driver";
import { Neo4jGraphQL } from "@neo4j/graphql";
const driver = _driver( 
 "bolt://localhost:7687",
 auth.basic("neo4j", "neo4j")
);

const typeDefs = /* GraphQL */ `
type Business {
businessId: ID!
name: String!
city: String!
state: String!
address: String!
location: Point!
reviews: [Review!]! @relationship(type: "REVIEWS", direction: IN)
categories: [Category!]!
@relationship(type: "IN_CATEGORY", direction: OUT)
}
type User {
userID: ID!
name: String!
reviews: [Review!]! @relationship(type: "WROTE", direction: OUT)
}
type Review {
reviewId: ID!
stars: Float!
date: Date!
text: String
user: User! @relationship(type: "WROTE", direction: IN)
business: Business! @relationship(type: "REVIEWS", direction: OUT)
}
type Category {
name: String!
businesses: [Business!]!
@relationship(type: "IN_CATEGORY", direction: IN)
}
`;

const neoSchema = new Neo4jGraphQL({ typeDefs, driver });
neoSchema.getSchema().then((schema) => {
  const server = new ApolloServer({
      schema,
  });

  server.listen().then(({ url }) => {
      console.log(`🚀 Server ready at ${url}`);
  });
})