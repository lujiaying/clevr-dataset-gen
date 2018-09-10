#!/bin/bash

alias blender='/media/drive/Jiaying/blender-2.79b-linux-glibc219-x86_64/blender'
blender --background --python render_images.py -- --num_images 1000 --use_gpu 1 --start_idx 526
blender --background --python render_images.py -- --num_images 1000 --use_gpu 1 --start_idx 1526
blender --background --python render_images.py -- --num_images 1000 --use_gpu 1 --start_idx 2526
blender --background --python render_images.py -- --num_images 1000 --use_gpu 1 --start_idx 3526
blender --background --python render_images.py -- --num_images 1000 --use_gpu 1 --start_idx 4526
blender --background --python render_images.py -- --num_images 1000 --use_gpu 1 --start_idx 5526
