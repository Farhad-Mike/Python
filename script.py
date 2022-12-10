bookmarks = open(r'D:\bookmarks.txt')

newBookmarks = []

completedBookmarks = []

for bookmark in bookmarks:
    if bookmark.find('torrents-igruha.org') != -1:
        newBookmarks.append(bookmark)


for bookmark in newBookmarks:
    position = bookmark.find('torrents-igruha.org')
    completedBookmarks.append('https://' + bookmark[position:])

print(completedBookmarks)

newFile = open(r'D:\newBookmarks.txt', 'w')
newFile.write('')
newFile.close()
newFile = open(r'D:\newBookmarks.txt', 'a')

for _ in completedBookmarks:
    newFile.write(_)


newFile.close()