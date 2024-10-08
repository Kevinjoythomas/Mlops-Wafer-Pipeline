import os 
import argparse
import yaml
import logging

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="default")
    args.add_argument("--datasource",default=None)
    
    passed_args = args.parse_args()
    print(passed_args)