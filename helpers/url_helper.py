from config.config_manager import ConfigManager


def get_exercise_full_url_by_exercise_number(exercise_number) -> str:
    exercises_domain_path = "/exercises"
    base_url = ConfigManager.get_base_url()
    exercise_sub_path = ConfigManager.get_exercise(exercise_number)
    seed = ConfigManager.get_seed()
    return f'{base_url}{exercises_domain_path}{exercise_sub_path}?seed={seed}'
