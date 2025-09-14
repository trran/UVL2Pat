import pathlib, json
from jinja2 import Environment, FileSystemLoader
import random
import pattern_generator
from flamapy.metamodels.fm_metamodel.transformations import UVLReader
#from flamapy.metamodels.pysat_metamodel.transformations import FmToPysat
#from flamapy.metamodels.bdd_metamodel.transformations import FmToBDD
#from flamapy.metamodels.pysat_metamodel.operations import PySATProducts
#from flamapy.metamodels.bdd_metamodel.operations import BDDProducts
#from flamapy.metamodels.fm_metamodel.operations import FMEstimatedProductsNumber

base_dir = pathlib.Path(__file__).parent
#Available categories:
# behavioral: strategy, observer.
# creational: factory_method, singleton.
# structural: adapter,  bridge, decorator.

#Change these variables to generate different patterns:
general_group = "creational"
pattern = "singleton"

config_name = "{}.json".format(pattern)
template_name = "{}.swift.j2".format(pattern)

configuration_path = "configurations"
template_path = "templates"

template_dir = base_dir / "patterns" / general_group / pattern / template_path
json_configuration_dir =  base_dir / "patterns" / general_group / pattern / configuration_path

configuration = json_configuration_dir / config_name

#fm = load_feature_model("singleton_pattern.uvl")
#config = get_random_configuration(fm)
#features_dict = configuration_to_dict(config, fm)

json_config = json.loads(configuration.read_text(encoding="utf-8"))

context = {
"features": json_config
}

pattern_generator.generate(context,template_name,template_dir,"")


def load_feature_model(uvl_file_path):
    fm = UVLReader(uvl_file_path).transform()
    return fm