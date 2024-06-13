import pyiqa
import torch
import numpy as np
from PIL import Image
import cv2
import argparse, os, sys, glob

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def compute_folder(metric,out_folder,ref_folder=""):
    if metric.metric_name=='fid':
        score=metric(out_folder, dataset_name="FFHQ", dataset_res=1024, dataset_split="trainval70k")    
    elif metric.metric_mode=='FR':
        ref_list=os.listdir(ref_folder)
        out_list=os.listdir(out_folder)
        score=np.zeros(len(out_list))
        for num in range(len(score)):
            ref_name=ref_folder+ref_list[num]
            out_name=out_folder+out_list[num]
            score[num]=metric(ref_name,out_name)
    elif metric.metric_mode=='NR':
        out_list=os.listdir(out_folder)
        score=np.zeros(len(out_list))
        for num in range(len(score)):
            out_name=out_folder+out_list[num]
            score[num]=metric(out_name)
    return score    

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_weight", type=str, default="./Weight/",help="Weight of TOPIQ")
    parser.add_argument("--target", type=str, default="real",help="The model you want to evaluate")
    parser.add_argument("--target_path", type=str, default="",help="Self designed distorted path, remain empty")
    parser.add_argument("--gt_path", type=str, default="",help="Self designed groung truth path, remain empty")

    opt = parser.parse_args()
    print('------Evaluating '+opt.target+'------')

    fr_pref = pyiqa.create_metric('topiq_fr', device=device,pretrained_model_path=opt.model_weight+"topiq-fr.pth")
    nr_pref = pyiqa.create_metric('topiq_nr', device=device,pretrained_model_path=opt.model_weight+"topiq-nr.pth")

    modes=['full','image','pixel','text']
    
    frs=[]
    nrs=[]

    for mode in modes:
        out_folder='./Result/'+opt.target+'/'+mode+'/'
        if not os.path.exists(out_folder):
            print(mode+' does not exist. Jumped!')
            continue
        gt_folder='./GT/'
        print('-------------------'+mode+'-------------------')
        
        score=compute_folder(fr_pref,out_folder,gt_folder)
        frs.append(np.mean(score))
        print('FR: '+'{:.4f}'.format(np.mean(score)),end='\t')
        score=compute_folder(nr_pref,out_folder,gt_folder)
        nrs.append(np.mean(score))
        print('NR: '+'{:.4f}'.format(np.mean(score)))
    
    print('Overall: '+'{:.4f}'.format(np.mean(frs)*2/3+np.mean(nrs)/3))

if __name__ == "__main__":
	main()