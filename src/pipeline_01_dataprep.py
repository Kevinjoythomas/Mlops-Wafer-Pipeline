import os 
import argparse
import yaml
import logging

def read_params(config_path):
    with open(config_path) as yaml_file:
        config =  yaml.safe_load(yaml_file)  
    return config
def main(config_path,datasource):
    config = read_params(config_path)
    print(config)
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default = os.path.join("config","params.yaml")
    if not os.path.exists(default):
        print(f"Config file not found: {default}")
    args.add_argument("--config",default=default)
    args.add_argument("--datasource",default=None)
    
    passed_args = args.parse_args()
    main(config_path = passed_args.config ,datasource = passed_args.datasource)