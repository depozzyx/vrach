from ini_config_parser import IniParserSingleton

ini_parser_singleton = IniParserSingleton().get_environment_from_file(".env")
ini_parser_singleton.print_running_environment()
config = ini_parser_singleton.config

PG_HOST = config("PG_HOST")
PG_PORT = config("PG_PORT")

PG_USERNAME = config("PG_USERNAME")
PG_DBNAME = config("PG_DBNAME")
PG_PASSWORD = config("PG_PASSWORD")
