from argparse import ArgumentParser
from app import Camera

def main() -> None:
    parser = ArgumentParser()
    
    parser.add_argument(
        "--url",
        required=True,
    )
    args = parser.parse_args()

    cam = Camera(args.url)
    cam.read_stream()

if __name__ == "__main__":
    main()
