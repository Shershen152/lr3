import requests

def search_repositories(query):
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "per_page": 100}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["items"]
    else:
        print("Помилка при отриманні даних:", response.status_code)
        return []

def get_repository_details(full_name):
    url = f"https://api.github.com/repos/{full_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Помилка при отриманні деталей репозиторію:", response.status_code)
        return None

def main():
    query = input("Введіть текст для пошуку репозиторіїв: ")
    repositories = search_repositories(query)
    
    if not repositories:
        print("Репозиторії не знайдено.")
        return
    
    print("\nЗнайдені репозиторії:")
    for i, repo in enumerate(repositories, start=1):
        print(f"{i}. {repo['full_name']} (* {repo['stargazers_count']})")
    
    choice = input("\nВиберіть номер репозиторію для перегляду деталей (або натисніть Enter для виходу): ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(repositories)):
        print("Вихід.")
        return
    
    repo_details = get_repository_details(repositories[int(choice) - 1]['full_name'])
    if repo_details:
        print("\nДетальна інформація:")
        print(f"Назва: {repo_details['name']}")
        print(f"Опис: {repo_details['description']}")
        print(f"Власник: {repo_details['owner']['login']}")
        print(f"Зірки: {repo_details['stargazers_count']}")
        print(f"Форки: {repo_details['forks_count']}")
        print(f"URL: {repo_details['html_url']}")

if __name__ == "__main__":
    main()
