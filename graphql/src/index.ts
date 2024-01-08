import { ApolloServer, gql } from 'apollo-server';


const run = () => {
  const typeDefs = gql`
    type Query {
      hello: String
    }
  `

  const resolvers = {
    Query: {
      hello: (): string => 'hello world'
    },
  };

  const server = new ApolloServer({ typeDefs, resolvers });

  server.listen().then(({ url }) => {
    console.log(`🚀 Server ready at ${url}`);
  });
};

// run();

// playground

const url: string = "https://google.com";
fetch(url)
  .then((res) => console.log(res))
  .catch((err) => console.error(err));

