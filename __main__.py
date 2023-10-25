import pulumi
from components.ec2vpc import EC2VPCComponent

## Crie uma pilha
#stack = pulumi.StackReference("estudo")

# Use o componente
meu_componente = EC2VPCComponent("meu-componente", {
    'vpc_cidr_block': '10.0.0.0/16',
    'subnet_cidr_block': '10.0.0.0/24',
    'instance_type': 't2.micro',
    'ami': 'ami-0c55b159cbfafe1f0',  # Substitua pelo ID de uma AMI válida
})#, opts=pulumi.ResourceOptions(parent=EC2VPCComponent))


# Exporte as saídas
pulumi.export("vpc_id", meu_componente.vpc_id)
pulumi.export("subnet_id", meu_componente.subnet_id)
pulumi.export("instance_id", meu_componente.instance_id)
