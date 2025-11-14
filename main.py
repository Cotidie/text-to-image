#!/usr/bin/env python3

from backend import Config, ImageGenerationServer


def main() -> None:
    try:
        config = Config()
        server = ImageGenerationServer(config)
        port = 5000

        print(f"Starting Text-to-Image Generation Server on port {port}...")
        print(f"Model: {config.model}")
        
        server.run(host="0.0.0.0", port=port)
        
    except Exception as e:
        print(f"Failed to start server: {e}")
        raise


if __name__ == "__main__":
    main()

