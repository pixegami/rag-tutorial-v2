with import <nixpkgs> {};

pkgs.mkShell {
  name = "python-study-group";

  nativeBuildInputs = with pkgs; [
    git        # For version control (if needed)
    python311Full   
    python311Packages.pip
    python311Packages.pypdf
    python311Packages.langchain
    python311Packages.pytest
    python311Packages.boto3
    python311Packages.chromadb  # unstable channel
    python311Packages.venvShellHook
    python311Packages.pipx
    poetry
    vim
  ];

  LANGUAGE = "Ollama RAG";
  VERSION  = "python --version";

  shellHook = ''
    # Optional: Set up a virtual environment when entering the shell
    python3 -m venv .venv
    source .venv/bin/activate
    echo "Welcome to $LANGUAGE Development Environment"
    $VERSION
  '';
}
