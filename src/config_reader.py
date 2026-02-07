import yaml
import os

with open('config.yaml', 'r') as f:
    config=yaml.safe_load(f)

resume_path= config['paths']['resume_path']
jd_path= config['paths']['jd_path']
output_path= config['paths']['output_path']

project_name= config['project']['project_name']
run_id= config['project']['run_id']
samples=config['project']['samples']

model= config['llm']['model']
temperature= config['llm']['temperature']

system_prompt=config['prompts']['system_prompt']