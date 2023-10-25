import docker


def list_images():
    client = docker.from_env()
    cont = client.containers.get('e65c677b434a4e549f94f6bac11b2567864dbfa53c7d3fadf1f7ca301b97e5a4')
    Statu = cont.attrs['State']['Status']
    # print(cont.attrs['State']['Status'])
    if Statu == 'running':
        print('si')



if __name__ == "__main__":
    list_images()
