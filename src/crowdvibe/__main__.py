"""Main app initialisation and entry-point"""

import uvicorn


def main() -> None:
    """Main entry-point method."""
    config = uvicorn.Config(
        "crowdvibe.app:create_app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info",
        factory=True,
    )
    server = uvicorn.Server(config)
    server.run()

    """uvicorn.run(
            "crowdvibe.app:get_application",
            host="0.0.0.0",
            port=8080,
            reload=True,
            log_level="info"
    )"""


if __name__ == "__main__":
    main()
