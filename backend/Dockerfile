FROM python:3.12.0-bullseye

ENV APPDIRPATH /app
WORKDIR ${APPDIRPATH}

RUN apt update &&\
    rm -rf ~/.cache &&\
    apt clean all

# pipxのインストール
RUN python -m pip install --upgrade pip &&\
    python -m pip install --user pipx &&\
    python -m pipx ensurepath &&\
    python -m pipx completions &&\
    echo "eval \"$(register-python-argcomplete pipx)\"" >> ~/.bashrc

ENV PATH "/root/.local/bin:${PATH}"

# poetryのインストール
RUN touch ~/.bash_completion &&\
    pipx install poetry &&\
    pipx upgrade poetry &&\
    poetry completions bash >> ~/.bash_completion

