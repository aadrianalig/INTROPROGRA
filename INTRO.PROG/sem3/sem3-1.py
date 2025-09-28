precioProducto=int(input('Escribe el precio: '))
porcentajeDescuento=int(input('Escribe el porcentaje de descuento: '))
precio=precioProducto-(precioProducto*(porcentajeDescuento/100))
print('el precio es de:',precio)
