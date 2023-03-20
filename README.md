# AI SCRIPTS

AI Video & Image Scripts

## Documentation

- Video Image Extracter notebook on [Google colab](https://colab.research.google.com/github/ptran1203/pytorch-animeGAN/blob/master/notebooks/animeGAN.ipynb)


**Step 1.** Create anime images from the video

```bash
python3 video_to_images.py --video-path {path}/videos/simpsons1_S31E11.mp4\
                                --save-path {path}/dataset/simpsons\
                                --max-image 1800\
                                --image-size 256\
```

**Step 2.** Create edge-smooth version of dataset from **Step 1.**

```bash
python3 script/edge_smooth.py --dataset simpsons --image-size 256
```
