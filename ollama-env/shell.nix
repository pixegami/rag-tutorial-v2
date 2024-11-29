with import <nixpkgs> {};

pkgs.mkShell {
  name = "Ollama Server";

  nativeBuildInputs = with pkgs; [
    git        # For version control (if needed)
    ollama
    python311Full   
    python311Packages.boto3
    python311Packages.langchain
    python311Packages.langchain-community
    python311Packages.langchain-chroma
    python311Packages.pip
    python311Packages.pypdf
    python311Packages.pytest
    python311Packages.venvShellHook
    vim
    zellij
  ];

  LANGUAGE = "Ollama";
  VERSION  = "ollama --version";

  shellHook = ''
    # Optional: Set up a virtual environment when entering the shell
    echo "Welcome to $LANGUAGE Development Environment"
    $VERSION
    # zellij -l "direction: vertical parts: - direction: horizontal parts: - run: {cmd: echo "Load Model"} - run: {cmd: ollama serve}"
    # zellij run "ollama serve" --layout vertical --split-left --command "sleep 5; ollama run gemma2:2b"

    # zellij run --floating ollama serve
    zellij --layout layout.kdl
  '';
}
