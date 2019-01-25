import yaml

def get_operator_artifact_type(operatorArtifactString):
    operatorArtifact = yaml.load(operatorArtifactString)
    if isinstance(operatorArtifact, dict):
        if "packageName" in operatorArtifact:
            return "Package"
        elif "kind" in operatorArtifact:
            if operatorArtifact["kind"] == "ClusterServiceVersion" or operatorArtifact["kind"] == "CustomResourceDefinition":
                return operatorArtifact["kind"]
    raise ValueError('Courier requires valid CSV, CRD, and Package files')
