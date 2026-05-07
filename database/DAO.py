from database.DB_connect import DBConnect
from model.areoporto import Areoporto


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select * from airports a """

        cursor.execute(query)

        for row in cursor:
            #row = dizionario
            #il modo più semplice per impacchettare i dati è creare un dto corrispondente alle righe che leggo
            res.append(Areoporto(**row)) #faccio unpack del dizionario

        cursor.close()
        conn.close()
        return res



    @staticmethod
    def getAllEdges(distanza, idMapAO):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """SELECT f.ORIGIN_AIRPORT_ID as a1, f.DESTINATION_AIRPORT_ID as a2, AVG(DISTANCE) as media
                    from flights f
                    group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID
                    having media> %s"""

        cursor.execute(query, (distanza,))

        for row in cursor:
            # creo semplicemente una lista di tuple (a1, a1, media) invece che un oggetto che dovrei creare
            res.append((idMapAO[row["a1"]], idMapAO[row["a2"]], row["media"]))

        cursor.close()
        conn.close()
        return res