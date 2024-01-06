import requests
import plotly.express as px

# GitHub API URL for searching repositories written in Python with more than 10,000 stars, sorted by stars
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

# Specify the headers for the GitHub API request
headers = {"accept": "application/vnd.github.v3+json"}

# Send GET request to the GitHub API
r = requests.get(url, headers=headers)

# Print the HTTP status code
print(f"Status code: {r.status_code}")

# Parse the JSON response
response_dict = r.json()

# Print total number of repositories and whether the results are complete
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Extract information about each repository from the response
repo_dicts = response_dict["items"]
repo_links, stars, hover_texts = [], [], []

# Iterate through each repository in the response
for repo_dict in repo_dicts:
    # Extract repository name and URL
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    # Extract the number of stars for the repository
    stars.append(repo_dict["stargazers_count"])

    # Extract owner's login, and repository description for hover text
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Specify the title and axis labels for the plot
title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}

# Create a bar chart using Plotly Express
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Customize the layout of the plot
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(
        showgrid=True,
        gridcolor="LightGray",
        gridwidth=0.5
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="LightGray",
        gridwidth=0.5
    )
)

# Customize the appearance of the bars in the plot
fig.update_traces(marker_color="#3498db", marker_line_color="black", marker_line_width=1, opacity=0.8)

# Update the font style
fig.update_layout(font=dict(family="Arial, sans-serif", size=12, color="RebeccaPurple"))

# Show the plot
fig.show()
