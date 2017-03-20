import imghdr

author = zhihu.Author('http://www.zhihu.com/people/zord-vczh')

os.mkdir('vczh')
for followee in author.followees:
    try:
        filename = followee.name + ' - ' + followee.id + '.jpeg'
        print(filename)
        with open('vczh/' + filename, 'wb') as f:
            f.write(requests.get(followee.photo_url).content)
    except KeyboardInterrupt:
        break

for root, dirs, files in os.walk('vczh'):
    for filename in files:
        filename = os.path.join(root, filename)
        img_type = imghdr.what(filename)
        if img_type != 'jpeg' and img_type is not None:
            print(filename, '--->', img_type)
            os.rename(filename, filename[:-4] + img_type)
