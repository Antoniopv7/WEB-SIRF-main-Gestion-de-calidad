from .entities.Profesor import Profesor

class ModelUser2():
    @classmethod
    def login(self, db, profesor, cursor):
        try:
            sql = "SELECT id_profesor, nombre, password, rut FROM profesor WHERE rut = %s"
            cursor.execute(sql, (profesor.rut,))
            row = cursor.fetchone()
            if row:
                profesor = Profesor(row[0], row[1], Profesor.check_password(row[2], profesor.password), row[3])
                return profesor
            else:
                return None
        except Exception as ex:
            raise Exception(ex)