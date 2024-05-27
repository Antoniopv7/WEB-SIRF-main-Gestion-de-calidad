from .entities.Profesor import Profesor

class ModelUser2():
    @classmethod
    def login(self, db, profesor):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id_profesor, nombre, password, rut FROM profesor WHERE rut = %s"
            cursor.execute(sql, (profesor.rut,))
            row = cursor.fetchone()
            if row:
                if row[2] == profesor.password:  # Comparar directamente la contraseña
                    profesor = Profesor(row[0], row[1], row[2], row[3])
                    return profesor
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        finally:
            cursor.close()