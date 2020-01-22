from graphqlclient import GraphQLClient

def main():

    graphql_url = "http://127.0.0.1:5000/graphql"

    client = GraphQLClient(graphql_url)
    
    for i in range(100):

        sentence = """mutation addCloudProvider {{ 
            addCloudProvider (uid:\"CP-{}\", name:\"Cloud Provider {}\", abbreviation:\"CP-{}\") {{ 
                cloudProvider {{ 
                    uid 
                    name 
                    abbreviation 
                }} 
            }}
        }}""".format(str(i+1),str(i+1),str(i+1))

        result = client.execute(sentence)
    
    print("Done!")

if __name__ == "__main__":
    main()