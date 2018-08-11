from settings import dataBaseDjangoDir
a = 1
class SensiTags:

    def __init__(self):
        pass

    def getInfo(self):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""select * from tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        return query
