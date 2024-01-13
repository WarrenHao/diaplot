# 检查是否有python3.8环境，没有则创建

# 检查python3.8环境(conda)
if conda env list | grep -q "py38"; then
    echo "py38 exists"
else
    echo "py38 does not exist"
    conda create -n py38 python=3.8
fi

# 激活环境
conda activate py38

# 安装依赖
pip install -r requirements.txt

# 安装jupyterlab
conda install -c conda-forge jupyterlab

# 安装jupyterlab插件
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install @jupyterlab/toc
jupyter labextension install @jupyterlab/git
jupyter labextension install @jupyterlab/github
jupyter labextension install @jupyterlab/latex
jupyter labextension install @jupyterlab/geojson-extension


# 检查环境变量中是否存在node的环境，没有则添加
if echo $PATH | grep -q "node"; then
    echo "node exists"
else
    echo "node does not exist"
    # 从node官网安装node
    # https://nodejs.org/en/download/
    # 添加node环境变量
    export PATH=$PATH:/c/Program\ Files/nodejs
fi


# 检查本地是否有可用的latex环境
if echo $PATH | grep -q "texlive"; then
    echo "texlive exists"
else
    echo "texlive does not exist"
    # 从texlive官网下载texlive
    # https://www.tug.org/texlive/acquire-netinstall.html
    # 添加texlive环境变量
fi
