# create Read full file named "story.txt" and prints the full content
# f=open("story.txt","x")
# f=open("story.txt", "w")
# story_content = input("Enter the content of the story: ")
# f.write(story_content)
# f.close()

with open("story.txt", "r") as f:
    content = f.read()
    print(content)