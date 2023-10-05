with open("poems.txt","r") as f:
    text = f.read()
    text = text.replace('twinke','#####')

    with open ('poems.txt','w') as f:
        f.write(text)