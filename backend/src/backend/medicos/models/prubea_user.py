from sqlalchemy import inspect

from backend.core.database import Base, SessionLocal, engine
from backend.medicos.models.user import User
from backend.core.segurity import hash_password

#Crear las tablas 
Base.metadata.create_all(bind=engine)

inspector = inspect(engine)
print("Tablas:", inspector.get_table_names())
print("Columnas:", [c["tables"] for c in inspector.get_columns("users")])

#Insertar un usuario de prueba
db = SessionLocal()
user = User(
    email:"ramses23@gmail.com",
    full_name:"Ramses Alfonso",
    hashed_password:password("Holamundo!485")
)

#Añadir los datos del usuario a la tabla de la BD
db.add(user)
db.commit() #Realizar los cambios
db.refresh(user) #Actualizar la BD

print("Creado:", user.id, user.email) # Imprimir resultado

# Leerlo de vuelta
encontrado = db.get(User, user.id)



