# GraphQL

#### Schema

base types like String, Int
customied types declared with `type` prefix

const Post = `
  type Post {
    id: Int!
    title: String
    content: String
    author: String
    comments: [Comment]
  }
`;

type with "!"  mandatory field
`[type]` an array with type elements

