from email.policy import default
from pprint import pprint
import sys
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.AppsV1Api()

def get_resources_dep(deploy_name: str=None):
    deployments_name = v1.list_deployment_for_all_namespaces()
    # dep_metadata_name = deployments_name.metadata.name
    for dep in deployments_name.items:
        d_contaier = dep.spec.template.spec.containers
        for res in d_contaier:
            res_lim = res.resources.limits
            res_req = res.resources.requests
            if deploy_name is not None:
                if deploy_name == dep.metadata.name:
                    print("DEPLOYMENT_NAME:",deploy_name)
                    print("RESOURCE_limits:", res_lim)
                    print("RESOURCE_requests:", res_req)
                    return
                continue
            print("DEPLOYMENT_NAME:",dep.metadata.name)
            print("RESOURCE_limits:", res_lim)
            print("RESOURCE_requests:", res_req)


if __name__ == "__main__":
    deploy_name = None
    if len(sys.argv) > 1:
        deploy_name = sys.argv[1]
    print(f"List resources of deployment {deploy_name}")
    get_resources_dep(deploy_name)