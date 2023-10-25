import pulumi
import pulumi_aws as aws

class EC2VPCComponent(pulumi.ComponentResource):
    def __init__(self, name: str, args, opts=None):
        super().__init__("MyComponent", name, {}, opts)

        # Crie a VPC
        vpc = aws.ec2.Vpc(name, cidr_block=args['vpc_cidr_block'], opts=pulumi.ResourceOptions(parent=self))

        # Crie uma subnet privada
        subnet = aws.ec2.Subnet(name, vpc_id=vpc.id, cidr_block=args['subnet_cidr_block'], opts=pulumi.ResourceOptions(parent=self))

        # Crie uma instância EC2 na subnet privada
        instance = aws.ec2.Instance(name, 
            instance_type=args['instance_type'],
            ami=args['ami'],
            subnet_id=subnet.id,
            tags={'Name': 'MinhaInstancia'},
            opts=pulumi.ResourceOptions(parent=self))

        # Exporte as saídas
        self.vpc_id = vpc.id
        self.subnet_id = subnet.id
        self.instance_id = instance.id

# Use o componente em uma pilha
stack = pulumi.StackReference("Vborges/components/components")

#my_component = EC2VPCComponent("my-component", {
#    'vpc_cidr_block': '10.0.0.0/16',
#    'subnet_cidr_block': '10.0.0.0/24',
#    'instance_type': 't2.micro',
#    'ami': 'ami-0c55b159cbfafe1f0',  # Substitua pelo ID de uma AMI válida
#}, opts=pulumi.ResourceOptions(parent=stack))
#
## Exporte as saídas do componente
#pulumi.export("vpc_id", my_component.vpc_id)
#pulumi.export("subnet_id", my_component.subnet_id)
#pulumi.export("instance_id", my_component.instance_id)
