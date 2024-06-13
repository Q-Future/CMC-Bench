
import inspect
from typing import List, Optional, Union
import argparse, os, sys, glob
import numpy as np
import torch
from PIL import Image
import pandas as pd
from diffusers import AutoPipelineForImage2Image
from diffusers import AutoPipelineForText2Image
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_name", type=str, default="real",help="Name of t2i model")
    parser.add_argument("--model_dir", type=str, default="SG161222/RealVisXL_V4.0",help="Path of t2i model")
    parser.add_argument("--mode",type=str,default="full",help="reference working mode")
    parser.add_argument("--ref_dir",type=str,default="./Ref/",help="Reference image")
    parser.add_argument("--strength",type=float,help="strength",default=0)
    parser.add_argument("--input_path",type=str,default="./Text/gpt4v.csv",help="Path of the input text")
    parser.add_argument("--output_path",type=str,default="./Result/",help="Path of the output image")

    opt = parser.parse_args()
    name=opt.model_name
    mode=opt.mode
    ref_dir=opt.ref_dir


    ind=pd.read_csv(opt.input_path)

 #   out_path='F:/chunyi/CMC-Bench/valid/I2T/'+opt.input+'-'+refimg+'/'
    out_path=opt.output_path+'/'+name+'/'+mode+'/'

    if mode=='full':
        folder = ref_dir+'image/'
        strength=0.5
        AutoPipeline=AutoPipelineForImage2Image
    elif mode=='pixel':
        folder = ref_dir+'pixel/'
        strength=0.8
        AutoPipeline=AutoPipelineForImage2Image
    elif mode=='image':
        folder = ref_dir+'image/'
        strength=0.5
        AutoPipeline=AutoPipelineForImage2Image
    elif mode=='text':
        strength=1.0
        AutoPipeline=AutoPipelineForText2Image

    
    if opt.strength>0:
        strength=opt.strength

    if not os.path.exists(out_path):#如果路径不存在
        os.makedirs(out_path)

    if name=='real':
        pipe = AutoPipeline.from_pretrained(
            "SG161222/RealVisXL_V4.0",
            torch_dtype=torch.float16,
            use_safetensors=True,
            add_watermarker=False,
            variant="fp16"
        )
        pipe.to(device)
    elif name=='sd15':
        pipe = AutoPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", 
            torch_dtype=torch.float16, 
            use_safetensors=True, 
            variant="fp16")
        pipe.to(device)
    else:
        pipe = AutoPipeline.from_pretrained(
            opt.model_dir, 
            torch_dtype=torch.float16, 
            use_safetensors=True, 
            variant="fp16")
        pipe.to(device)



    torch.manual_seed(42)
    
    files=os.listdir(folder)

    cnt=0
    for num in range(0,1000):
        file = ind['name'][num]
        path = folder + file
        init_image = Image.open(path).convert("RGB")
        w=int(np.round(init_image.size[0]/max(init_image.size)*1024))
        h=int(np.round(init_image.size[1]/max(init_image.size)*1024))
        
        if mode=='image':
            prompt='High quality, masterpiece, clean, high-resolution, 8k'
        else:
            prompt = ind['text'][num]
        image = pipe(prompt, image=init_image.resize((w,h)), num_inference_steps=40, strength=strength).images[0]
        image.resize(init_image.size).save(out_path+file)
        cnt=cnt+1
        if cnt%100==0:
            break        

if __name__ == "__main__":
	main()