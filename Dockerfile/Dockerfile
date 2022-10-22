FROM python:3.6-stretch

MAINTAINER Shashank Bhat "ssbhat98@gmail.com"

ENV TEMP_MRCNN_DIR /tmp/mrcnn

RUN apt-get update && apt-get install -y \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install tensorflow==1.8.0 && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py==2.8.0 scikit-image && \
    pip3 install keras==2.2.0 && \
    pip3 install imutils

RUN git clone https://github.com/matterport/Mask_RCNN.git $TEMP_MRCNN_DIR
RUN cd $TEMP_MRCNN_DIR && \
 python3 setup.py install


# Copy all the files from the project’s root to the working directory
COPY . /app

# Running Python Application
CMD ["python3", "/app/object_detect.py"]
