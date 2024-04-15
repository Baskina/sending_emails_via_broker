from mongoengine import connect

client = connect(
    db='contacts',
    username='baskinadevelopment',
    password='5fQLW8GKlk87ARN6',
    host='mongodb+srv://baskinadevelopment:5fQLW8GKlk87ARN6@cluster0.upbkmny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
    alias='default'
)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)