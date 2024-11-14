from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Tabla para la Marca de maquillaje
class Brand(Base):
    __tablename__ = 'brand'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relación de uno a muchos con productos
    products = relationship("Product", back_populates="brand")

# Tabla para los Tipos de productos de maquillaje
class ProductType(Base):
    __tablename__ = 'product_type'
    
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    
    # Relación de uno a muchos con productos
    products = relationship("Product", back_populates="product_type")

# Tabla para los productos de maquillaje
class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    
    # Claves foráneas
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)
    product_type_id = Column(Integer, ForeignKey('product_type.id'), nullable=False)
    
    # Relaciones
    brand = relationship("Brand", back_populates="products")
    product_type = relationship("ProductType", back_populates="products")

# Conexión a la base de datos
engine = create_engine('sqlite:///makeupdb.db', echo=True)

# Todas las tablas
Base.metadata.create_all(engine)

# Configuraración de sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de agregar datos
# Añadir marcas
brand1 = Brand(name="Maybelline")
brand2 = Brand(name="L'Oréal")

# Añadir tipos de productos
type1 = ProductType(description="Base")
type2 = ProductType(description="Labial")

# Añadir productos
product1 = Product(name="Fit Me Foundation", price=12, brand=brand1, product_type=type1)
product2 = Product(name="Super Stay Matte Ink", price=10, brand=brand1, product_type=type2)

# Agregar los objetos a la sesión
session.add_all([brand1, brand2, type1, type2, product1, product2])

# Confirmar los cambios en la base de datos
session.commit()

# Cerrar sesión
session.close()
