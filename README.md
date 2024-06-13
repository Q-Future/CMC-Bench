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

 <h1>CMC-Bench: A New Paradigm of Visual Signal Compression</h1>
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
      <img style="width:100%" src="fig/spotlight.png">
 </div>
</div>

<div align="left">

**Why use LMMs for compression?** Large Multimodal Models (LMMs) support the conversion between multiple modalities, where text consumes much less space than image modalities. By cascading Image-to-Text (I2T) and Text-to-Image (T2I) models, images can be compressed and reconstructed from semantic information. This Cross-Modality Compression (CMC) paradigm operates at the semantic level, which outperforms traditional codecs at the pixel level. It enables easy attainment of 1,000 times compression, and even 10,000 times in extreme cases.

However, at such low bitrates, CMC presents two significant issues that cannot be overlooked. CMC-Bench is designed to evaluate : **(1) Consistency** between the distorted and reference image, **(2) Pcrecption** quality of the distorted image only.

## Release
- [2024/6/13] 🔥 [Github repo](https://github.com/Q-Future/CMC-Bench) for **CMC-Bench** is online. Follow the instruction to join the I2T or T2I model arena!!
- [2024/6/11] 🔥 We release the **CMC-Bench** data and meta information at [Huggingface](https://huggingface.co/datasets/lcysyzxdxc/CMC-Bench).
- [] Update the subjective label for quality assessment task.
- [] Update all interval image and text data for compression.

## CMC-Bench Construction
To provide a comprehensive and high-quality resource for various applications on the Internet, we carefully curated 1,000 images without compression distortion as the ground truth of CMC-Bench. Including 400 NSIs, 300 SCIs, and 300 AIGIs.

We employ 6 I2T and 12 T2I models across four compression modes. Namely **Text** mode with only T2I and I2T, **Pixel** mode with several pixels to guide T2I model, **Image** mode with a compressed image as I2t guidance but without I2T model, **Full** mode with all necessary information but most expenses. Thus a I2T+T2I group will be evaluated in 4*2=8 dimensions.

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="fig/mode-all.png">
</div>

## Glance at A-Bench Performance

For I2T models, GPT-4o shows the best perfoemance. For T2I models, DiffBIR ranks best in terms of **Image** and **Full** but unsupportive at other two modes, while RealVis is the most full-edged model for all modes.
<div style="width: 100%; text-align: center; margin:auto;">
  <img style="width:50%" src="fig/radar-i2t.png"><img style="width:50%" src="fig/radar-t2i.png">
</div>

</div>