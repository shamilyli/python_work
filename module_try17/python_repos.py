import requests

#excute api read and store the response 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

#store the api response into a variable
response_dict = r.json()

print("Total respositories returned: ", response_dict['total_count'])

#searching the relevant respositories info
repo_dicts = response_dict['items']
print("Respositories returned: ", len(repo_dicts))

#studying the first respository
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

print("\nSelected information about each respositories:")
# print('Name: ', repo_dict['name'])
# print('Owner: ', repo_dict['owner']['login'])
# print('Status: ', repo_dict['stargazers_count'])
# print('Respository', repo_dict['html_url'])
# print('Created: ', repo_dict['created_at'])
# print('Updated: ', repo_dict['updated_at'])
# print('Description: ', repo_dict['description'])

#for all respositories
for repo_dict in repo_dicts:
	print("\n")
	print('Name: ', repo_dict['name'])
	print('Owner: ', repo_dict['owner']['login'])
	print('Status: ', repo_dict['stargazers_count'])
	print('Respository', repo_dict['html_url'])
	print('Description: ', repo_dict['description'])