# AI SCRIPTS

AI Video & Image Scripts

## Documentation

- Video Image Extracter notebook on [Google colab](https://colab.research.google.com/drive/1h7W_rwBdg1f6re_8nvqlow6p72YLiea2?usp=sharing)


**Step 1.** Create anime images from the video

```bash
python3 video_to_images.py  --video-path {path}/videos/simpsons1_S31E11.mp4\
                            --save-path {path}/dataset/simpsons\
                            --frame_splitter 75\
                            --size (256,256)
```

frame_splitter default value is 100
size default value is (256,256)


**** Create edge-smooth version of dataset from **Step 1.**

```bash
python3 edge_smooth.py --dataset simpsons --image-size 256
```
