import tkinter as tk
from tkinter import messagebox, ttk



# Funciones
class Kardex:
    # Base de datos
    
    def __init__(self):
        self.base_datos = []
    
    def agregar_entrada(self, fecha, producto, cantidad, costo_unitario, documento):
        saldo_actual = self.obtener_saldo_actual(producto)
        self.base_datos.append(
                {
                    "fecha":fecha, 
                    "producto":producto, 
                    "descripcion":"Entrada",  
                    "documento":documento, 
                    "entrada":cantidad, 
                    "salida":0,
                    "saldo":saldo_actual + cantidad,
                    "costo_unitario":costo_unitario, 
                    "total_valorizado":cantidad * costo_unitario
                }
            )

    def agregar_salida(self, fecha, producto, cantidad, costo_unitario, documento):
        saldo_actual = self.obtener_saldo_actual(producto)
        if saldo_actual < cantidad:
            return f"No hay suficiente cantidad de producto"
        
        costo_unitario = self.obtener_costo_promedio(producto)

        self.base_datos.append(
                {
                    "fecha":fecha, 
                    "producto":producto, 
                    "descripcion":"Salida",  
                    "documento":documento, 
                    "entrada":0, 
                    "salida":cantidad,
                    "saldo":saldo_actual - cantidad,
                    "costo_unitario":costo_unitario, 
                    "total_valorizado":cantidad * costo_unitario
                }
            )
    
    def obtener_saldo_actual(self, producto):
        saldo = 0
        for mov in self.base_datos:
            if mov["producto"] == producto:
                saldo += mov["entrada"] - mov["salida"]
        return saldo
    
    def obtener_costo_promedio(self, producto):
        total_cantidad = 0
        total_costo = 0
        for mov in self.base_datos:
            if mov["producto"] == producto and mov["descripcion"] == "Entrada":
                total_cantidad += mov["entrada"]
                total_costo += mov["total_valorizado"]
        return total_costo / total_cantidad if total_cantidad > 0 else 0
    
    def obtener_kardex(self):
        return self.base_datos
    

class InventarioApp:
    def __init__(self, root):
        self.kardex = Kardex()
        
        root.title("Sistema de Inventario")
        root.geometry("800x600")
        # root.resizable(False, False)

        # Inputs
        tk.Label(root, text="Fecha").grid(row=0, column=0)
        self.fecha_entry = tk.Entry(root)
        self.fecha_entry.grid(row=0, column=1)

        tk.Label(root, text="Producto").grid(row=1, column=0)
        self.producto_entry = tk.Entry(root)
        self.producto_entry.grid(row=1, column=1)

        tk.Label(root, text="Cantidad").grid(row=2, column=0)
        self.cantidad_entry = tk.Entry(root)
        self.cantidad_entry.grid(row=2, column=1)

        tk.Label(root, text="Costo Unitario").grid(row=3, column=0)
        self.costo_unitario_entry = tk.Entry(root)
        self.costo_unitario_entry.grid(row=3, column=1)

        tk.Label(root, text="Documento").grid(row=4, column=0)
        self.documento_entry = tk.Entry(root)
        self.documento_entry.grid(row=4, column=1)

        # Botones
        tk.Button(root, text="Agregar Entrada", command=self.agregar_entrada).grid(row=5, column=0)
        tk.Button(root, text="Agregar Salida", command=self.agregar_salida).grid(row=5, column=1)
        tk.Button(root, text="Ver Kardex", command=self.ver_kardex).grid(row=5, column=2)

        # Tabla
        self.tree = ttk.Treeview(root, columns=("Fecha", "Producto", "Descripcion", "Documento", "Entrada", "Salida", "Saldo", "Costo Unitario", "Total Valorizado"))
        self.tree.grid(row=7, column=0, columnspan=3)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

    def agregar_entrada(self):
        try:
            fecha = self.fecha_entry.get()
            producto = self.producto_entry.get()
            cantidad = int(self.cantidad_entry.get())
            costo_unitario = float(self.costo_unitario_entry.get())
            documento = self.documento_entry.get()

            self.kardex.agregar_entrada(fecha, producto, cantidad, costo_unitario, documento)
            messagebox.showinfo("Exito", "Entrada agregada correctamente")
            self.ver_kardex()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def agregar_salida(self):
        try:
            fecha = self.fecha_entry.get()
            producto = self.producto_entry.get()
            cantidad = int(self.cantidad_entry.get())
            costo_unitario = float(self.costo_unitario_entry.get())
            documento = self.documento_entry.get()

            self.kardex.agregar_salida(fecha, producto, cantidad, costo_unitario, documento)
            messagebox.showinfo("Exito", "Salida agregada correctamente")
            self.ver_kardex()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ver_kardex(self):
        for item in self.tree.get_children():
           self.tree.delete(item)

        for mov in self.kardex.obtener_kardex():
            self.tree.insert("", tk.END, values=(mov["fecha"], mov["producto"], mov["descripcion"], mov["documento"], mov["entrada"], mov["salida"], mov["saldo"], mov["costo_unitario"], mov["total_valorizado"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()