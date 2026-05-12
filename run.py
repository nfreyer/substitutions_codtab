#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:32:57 2018

@author: ernestmordret
"""
import argparse
import logging

# from params import *
from substitutions.detect import main as detect_main
import os


def parse_params(param_file):
    """Parse params file into dict.

    Args:
        param_file (str): Path to param file

    Returns:
        dict: Dict mapping param name to value
    """
    params = {}
    with open(param_file) as fin:
        for line in fin:
            if line.strip().startswith("#"):
                continue
            key, val = line.strip().split("=")
            key, val = key.strip(), val.strip()
            params[key] = val
            # if key == "excluded_samples":
            #     params[key] = params[key].split(",")
            #     params["excluded_samples"].remove("")
    return params


def create_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    return logger

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="Path to config file")
    parser.add_argument(
        "-d", "--detect", action="store_true", help="run the detect script without unimod filter and with a codon table."
    )
    
    args = parser.parse_args()
    param_dict = parse_params(args.config)
    return args, param_dict

def main():
    args, param_dict = parse_args()
    logger = create_logger()
    if os.path.isdir(param_dict["output_dir"]):
        pass
    else:
        logger.info("creating output directory")
        os.mkdir(param_dict["output_dir"])
    
    if args.detect:
        if os.path.isfile(os.path.join(param_dict["output_dir"], "subs")):
            overwrite = input("output directory already exists. Press y to overwrite: ")
            if overwrite.lower() == "y":
                logger.warning("overwriting subs")
                os.remove(os.path.join(param_dict["output_dir"], "subs"))
                os.remove(os.path.join(param_dict["output_dir"], "subs.csv"))
            else:
                logger.info("exit")
                exit()
    
        logger.info("detecting substitutions. That step might take some time...")
        detect_main(param_dict)    

if __name__ == '__main__':
    main()
