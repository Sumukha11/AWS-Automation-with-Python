#Import Boto3
import boto3
import time

rds = boto3.client('rds', region_name='ap-south-1')

username='sumukha'
password='mypasswd'
db_subnet_group='vpc-subnet-group'
db_cluster_id='rds-sumukha-cluster'

#Create the DB cluster
try:
    response=rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
    print(f"The DB Cluster named '{db_cluster_id}' already exists")
except rds.exceptions.DBClusterNotFoundFault:
    print(f"DB Cluster {db_cluster_id} not found creating a new cluster...")
    
    response = rds.create_db_cluster(
        DatabaseName= 'auroraDB',
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.11.2',
        EngineMode='provisioned',
        DBClusterIdentifier=db_cluster_id,
        # EnableHttpEndpoint=True,
        MasterUsername=username,
        DBSubnetGroupName=db_subnet_group,
        MasterUserPassword=password,
    #     ScalingConfiguration={
    #         'MinCapacity':1, #Minimum ACU
    #         'MaxCapacity':8, #Max ACU
    #         'AutoPause': True,
    #         'SecondsUntilAutoPause':300, #Pause after 5 minutes of inactivity
    # }
)
    print(f"The DB cluster {db_cluster_id} has been created.")
    
    #wait for the DB cluster to be available
    while True:
        response = rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
        status=response['DBClusters'][0]['Status']
        print(f"The Status of the DB is {status}")
        if status == 'available':
            break
        
        print("waiting for the DB Cluster to become Available...")
        time.sleep(40)


#Deleting the DB Cluster
response = rds.delete_db_cluster(
    DBClusterIdentifier=db_cluster_id,
    SkipFinalSnapshot=True
)

print(f"DB Cluster '{db_cluster_id}' has been deleted")