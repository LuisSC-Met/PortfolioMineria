import reflex as rx

config = rx.Config(
    app_name="Portfolio",
    cors_allowed_origins=[
        "https://localhost:3000",
        "https://portfolio-silver-moon.reflex.run"
    ],
    api_url="https://aedb6aa0-c037-4fb4-bdf2-9f6b1ef1839c.fly.dev",
    deploy_url="https://portfolio-silver-moon.reflex.run",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    show_built_with_reflex=False
)