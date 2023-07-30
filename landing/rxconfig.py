import reflex as rx

class LandingConfig(rx.Config):
    pass

config = LandingConfig(
    app_name="landing",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)