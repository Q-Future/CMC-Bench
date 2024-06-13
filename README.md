<div align="center">
    
    
 <div>
  <a href="https://github.com/lcysyzxdxc/"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fvqassessment%2FCMC-Bench&count_bg=%23E97EBA&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visitors&edge_flat=false"/></a>
  <a href="https://github.com/Q-Future/CMC-Bench"><img src="https://img.shields.io/github/stars/lcysyzxdxc/CMC-Bench"/></a>
  <a href="https://arxiv.org/pdf/2400.00000"><img src="https://img.shields.io/badge/Arxiv-2406.03070-blue"/></a>
  <a href="https://huggingface.co/datasets/lcysyzxdxc/CMC-Bench"><img src="https://img.shields.io/badge/Data-Release-green"></a>
 </div>

 <div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="fig/teaser.png">
 </div>

 <h1>CMC-Bench: Towards a New Paradigm of Visual Signal Compression</h1>

 _Using large Multimodal Models for Cross Modality Compression_

 <div>
      <a href="https://github.com/lcysyzxdxc" target="_blank">Chunyi Li</a><sup>1</sup>,
      <a href="https://multimedia.sjtu.edu.cn/index.php?m=home&c=View&a=index&aid=141" target="_blank">Xiele Wu</a><sup>1</sup>,
      <a href="https://teowu.github.io/" target="_blank">Haoning Wu</a><sup>2</sup>,
      <a href="https://medialab.sjtu.edu.cn/author/donghui-feng/" target="_blank">Donghui </a><sup>1</sup>,
      <a href="https://zzc-1998.github.io/" target="_blank">Zicheng Zhang</a><sup>1</sup>,
 </div>

 <div>
      <a href="https://guolusjtu.github.io/guoluhomepage/" target="_blank">Guo Lu</a><sup>1</sup>,
      <a href="https://minxiongkuo.github.io/" target="_blank">Xiongkuo Min</a><sup>1</sup>,
      <a href="https://jhc.sjtu.edu.cn/~xiaohongliu/" target="_blank">Xiaohong Liu</a><sup>1</sup><sup>*</sup>,
      <a href="https://ee.sjtu.edu.cn/en/FacultyDetail.aspx?id=24&infoid=153&flag=153" target="_blank">Guangtao Zhai</a><sup>1</sup><sup>*</sup>,
      <a href="https://personal.ntu.edu.sg/wslin/Home.html" target="_blank">Weisi Lin</a><sup>2</sup>
 </div>
 <div>
  <sup>1</sup>Shanghai Jiaotong University,  <sup>2</sup>Nanyang Technological University
 </div> 
 <div>
  <sup>*</sup>Corresponding author. 
 </div>
 <a href="https://github.com/Q-Future/CMC-Bench/blob/main/CMC_Bench.pdf"><strong>Paper</strong></a> |
 <a href="https://github.com/Q-Future/CMC-Bench"><strong>Project Page</strong></a> |
 <a href="https://huggingface.co/datasets/lcysyzxdxc/CMC-Bench"><strong>Data</strong></a> 
 <div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:60%" src="fig/spotlight.png">
 </div>
</div>

<div align="left">

**Why use LMMs for compression?** Large Multimodal Models (LMMs) support the conversion between multiple modalities, where text consumes much less space than image modalities. By cascading Image-to-Text (I2T) and Text-to-Image (T2I) models, images can be compressed and reconstructed from semantic information. This Cross-Modality Compression (CMC) paradigm operates at the semantic level, which outperforms traditional codecs at the pixel level. It enables easy attainment of 1,000 times compression, and even 10,000 times in extreme cases.

However, at such low bitrates, CMC presents two significant issues that cannot be overlooked. CMC-Bench is designed to evaluate : **(1) Consistency** between the distorted and reference image, **(2) Pcrecption** quality of the distorted image only. Thus, CMC-Bench is designed to identify where LMMs can be further optimized toward the compression task, thereby promote the evolution of visual signal codec protocols.

## Release
- [2024/6/13] 🔥 [Github repo](https://github.com/Q-Future/CMC-Bench) for **CMC-Bench** is online. Follow the instruction to join the I2T or T2I model arena!!
- [2024/6/11] 🔥 We release the **CMC-Bench** data and meta information at [Huggingface](https://huggingface.co/datasets/lcysyzxdxc/CMC-Bench).
- [To Do] Update the subjective label for quality assessment task.
- [To Do] Update all interval image and text data for compression.

## CMC-Bench Construction
To provide a comprehensive and high-quality resource for various applications on the Internet, we carefully curated 1,000 images without compression distortion as the ground truth of CMC-Bench. Including 400 NSIs, 300 SCIs, and 300 AIGIs. The data selection and annoattion detail are attached in out paper.

We employ 6 I2T and 12 T2I models across four working modes. **(1) Text** mode with only T2I and I2T model; **(2) Pixel** mode with several pixels to guide T2I model; **(3) Image** mode with a compressed image as I2T guidance but without I2T model; **(4) Full** mode with all necessary information but most expenses. A I2T+T2I group will be evaluated in 4*2=8 dimensions.

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="fig/mode-all.png">
</div>

## Leaderboard of CMC-Bench
Radar maps are shown as a quick glance. Among I2Ts, GPT-4o shows the best perfoemance. Among T2Is, DiffBIR ranks best in terms of **Image** and **Full** but unsupportive at other two modes, while RealVis is the most full-edged model.
<div style="width: 100%; text-align: center; margin:auto;">
  <img style="width:50%" src="fig/radar-i2t.png"><img style="width:50%" src="fig/radar-t2i.png">
</div>
The detailed leaderboard is:

|Model	|	Full-FR	|	Full-NR	|	Pixel-FR	|	Pixel-NR	|	Text-FR	|	Text-NR	|	Image-FR	|	Image-NR	|
|Animate	|	2.2985	|	1.8469	|	1.8246	|	2.4324	|	1.6983	|	3.4979	|	2.2522	|	1.6148	|
|Dreamlike	|	2.5071	|	1.7892	|	1.9545	|	2.3038	|	1.709	|	3.1588	|	2.4226	|	1.5131	|
|PG20	|	2.3603	|	2.3695	|	1.8883	|	2.6875	|	1.718	|	3.7438	|	2.2476	|	2.2071	|
|PG25	|	2.0716	|	2.9194	|	1.7418	|	3.626	|	1.7382	|	3.7299	|	1.9612	|	2.9935	|
|RealVis	|	2.5646	|	2.0415	|	1.9878	|	2.7815	|	1.7805	|	3.4802	|	2.5033	|	1.8098	|
|SD15	|	2.4895	|	1.7733	|	1.9422	|	2.1444	|	1.6832	|	2.5318	|	2.4163	|	1.5574	|
|SDXL	|	2.4184	|	1.6837	|	1.9103	|	1.9724	|	1.7471	|	3.4225	|	2.3482	|	1.5586	|
|SSD-1B	|	2.4939	|	2.0803	|	1.9611	|	2.4828	|	1.7753	|	3.4796	|	2.4147	|	1.9308	|
|DiffBIR	|	2.9194	|	2.5803	|	-	|	-	|	-	|	-	|	2.863	|	1.7342	|
|InstructPix	|	2.1519	|	1.7191	|	-	|	-	|	-	|	-	|	2.3457	|	1.2219	|
|PASD	|	2.727	|	2.2256	|	-	|	-	|	-	|	-	|	2.6378	|	2.0101	|
|StableSR	|	2.6232	|	1.4368	|	-	|	-	|	-	|	-	|	2.6088	|	1.4293	|



</div>