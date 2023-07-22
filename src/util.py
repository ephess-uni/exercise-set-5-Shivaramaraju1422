from pathlib import Path


def get_repository_root() -> Path:
    """
    get_repository_root returns a pathlib.Path object that can be used to locate files
    relative to the repository root--regardless of the run environment.  As long as
    this module in importable, the repository root can be located.

    Example
    -------
    repo_root = get_repository_root()
    data_dir = repo_root / 'data'
    output_dir = repo_root / 'outputs'

   
    with open(output_dir / 'test_output.txt', 'w') as f:
        f.write('test success!')

   
    hello_out_file = os.path.join(get_repository_root(), 'hello.txt')
    """
    return Path(__file__).absolute().parent.parent
