import yaml as pyYaml
import operatorcourier.identify as identify

class BuildCmd():
    name = 'build'
    
    def __init__(self):
        pass

    def _get_empty_bundle(self):
        operatorArtifactsTemplate = dict(
            data = dict(
                customResourceDefinitions = [],
                clusterServiceVersions = [],
                packages = [],
            )
        )
        return operatorArtifactsTemplate
    
    def _get_field_entry(self, yamlContent):
        yaml_type = identify.get_operator_artifact_type(yamlContent)
        if yaml_type == "ClusterServiceVersion" or yaml_type == "CustomResourceDefinition" or yaml_type == "Package":
            return yaml_type[0:1].lower() + yaml_type[1:] + 's'

    def _updateArtifact(self, operatorArtifact, yamlContent):
        operatorArtifact["data"][self._get_field_entry(yamlContent)].append(pyYaml.load(yamlContent))
        return operatorArtifact

    def build_bundle(self, strings):
        bundle =  self._get_empty_bundle()
        for item in strings:
            bundle = self._updateArtifact(bundle, item)

        return bundle
