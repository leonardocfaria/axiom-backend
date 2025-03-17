from dynaconf import Dynaconf

config = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[ '.secrets.toml'],
    root_path="../../.."
)