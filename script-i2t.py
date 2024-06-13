
import argparse
from modelscope import (
    snapshot_download, AutoModelForCausalLM, AutoTokenizer, GenerationConfig
)
import torch
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

import pandas as pd

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground_truth", type=str, default='./GT/',help="Path to the folder of ground truth")
    parser.add_argument("--output_path", type=str, default="./Text/",help="Path to the output text")
    parser.add_argument("--model_name", type=str, default="Qwen",help="Name of i2t model")
    parser.add_argument("--model_dir", type=str, default="Qwen/Qwen-VL-Chat",help="Path of i2t model")
    parser.add_argument("--explen", type=int, default=10,help="Text length")

    opt = parser.parse_args()

    torch.manual_seed(42)

    tokenizer = AutoTokenizer.from_pretrained(opt.model_dir,trust_remote_code=True)
    if not hasattr(tokenizer, 'model_dir'):
        tokenizer.model_dir = opt.model_dir

    # use fp16
    model = AutoModelForCausalLM.from_pretrained(opt.model_dir, device_map="auto", trust_remote_code=True, fp16=True).eval()

    model.to(device)

    #Qwen
    explen=opt.explen

    adds=['Considering Light and Color', ', Clarity', ', Dense Caption', ', and Region Semantic']
    add=''.join(adds[0:int(explen/10)])
    import os
    folder=opt.ground_truth
    files=os.listdir(folder)
    lst=[]
    cnt=0
    for file in files:
        path = folder + file

        question = 'Generate an informative paragraph in '+str(explen)+' words based on the image.'+add

        response, history = model.chat(tokenizer, query=f'<img>{path}</img>'+question, history=None)

        text=response
        lst.append([file,text])
        cnt=cnt+1
        if cnt%100==0:
            print('------'+str(cnt)+' images are encoded------')

    column=['name','text'] #列表头名称
    test=pd.DataFrame(columns=column,data=lst)#将数据放进表格
    test.to_csv(opt.output_path+'/'+opt.model_name+'.csv', encoding='utf-8')#数据存入csv,存储位置及文件名称

if __name__ == "__main__":
    main()
    
