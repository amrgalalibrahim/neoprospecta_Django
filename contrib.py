from django.contrib.auth.models import User, Permission

def create_superuser(username, email, password):
    # Create user
    user = User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser {username} created successfully")

if __name__ == '__main__':
    # Run the function to create a superuser
    create_superuser('neoprospecta', 'neoprospecta@example.com', 'neopct1234')

