import pymysql
import typer

app = typer.Typer()
connection = pymysql.connect(
    host="localhost",
    user = "root",
    passwd = "",
    database = "aasthadb"
)

cursor = connection.cursor()

@app.command()
def ls():
    fetch_data = "select * from tb order by priority ASC"
    cursor.execute(fetch_data)
    for i in cursor.fetchall():
        print(str(i[0]) + "." + str(i[1]) + " [" +str(i[2])+ "]")
        

@app.command()
def delete(index):
    index = int(index)
    cursor.execute("delete from tb where id = %s ", index)
    connection.commit()
    print("task with index"+str(index)+"is deleted successfully")


@app.command()
def add(p, name):
    insert_data = "insert into tb(task, priority, state) values (%s, %s, false)"
    parr = (name,p)
    cursor.execute(insert_data, parr)
    connection.commit()
    print(name+" with priority "+ p +" is added")

@app.command()
def done(index):
    index = int(index)
    cursor.execute("update tb set state=true where id=%s",index)
    connection.commit()
    print("task with index"+str(index)+"is marked done")

@app.command()
def report():
    fetch_data = "select * from tb where state = true order by priority ASC"
    cursor.execute(fetch_data)
    print("\n completed:")
    for i in cursor.fetchall():
        print(str(i[0]) + "." + str(i[1]) + " [" +str(i[2])+ "]")
    
    fetchh_data = "select * from tb where state = false order by priority ASC "
    cursor.execute(fetchh_data)
    print("\n Incomplete:")
    for i in cursor.fetchall():
        print(str(i[0]) + "." + str(i[1]) + " [" +str(i[2])+ "]")


if __name__ == "__main__":
    app()



