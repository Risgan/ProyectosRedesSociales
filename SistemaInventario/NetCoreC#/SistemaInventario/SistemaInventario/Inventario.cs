using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace SistemaInventario
{
    public partial class Inventario : Form
    {
        private baseDatosService _baseDatosService = new baseDatosService();
        public Inventario()
        {
            InitializeComponent();
            //dataGridView.Rows.Add(nombre, cantidad, precio);
            //dataGridView.Rows.Clear();


        }

        private void btn_entrada_Click(object sender, EventArgs e)
        {
            base_datos db = new base_datos();
            db.fecha = inp_fecha.Value;
            db.producto = inp_producto.Text;
            db.descripcion = "Entrada";
            db.documento = inp_documento.Text;
            db.entrada = Convert.ToInt32(inp_cantidad.Value);
            db.salida = 0;
            db.saldo = _baseDatosService.getSaldo(db.producto);
            db.costo_unitario = Convert.ToInt32(inp_cu.Text);
            db.total = db.costo_unitario * db.entrada;
            _baseDatosService.Registro(db);
            btn_kardex_Click(sender, e);

        }

        private void btn_salida_Click(object sender, EventArgs e)
        {
            base_datos db = new base_datos();
            db.fecha = inp_fecha.Value;
            db.producto = inp_producto.Text;
            db.descripcion = "Salida";
            db.documento = inp_documento.Text;
            db.entrada = 0;
            db.salida = Convert.ToInt32(inp_cantidad.Value);
            db.saldo = _baseDatosService.getSaldo(db.producto);
            db.costo_unitario = Convert.ToInt32(inp_cu.Text);
            db.total = db.costo_unitario * db.salida;
            _baseDatosService.Registro(db);
            btn_kardex_Click(sender, e);
        }

        private void btn_kardex_Click(object sender, EventArgs e)
        {
            dataGridView.Rows.Clear();
            foreach (var item in _baseDatosService.getKardex())
            {
                dataGridView.Rows.Add(
                    item.fecha, 
                    item.producto, 
                    item.descripcion, 
                    item.documento, 
                    item.entrada, 
                    item.salida, 
                    item.saldo, 
                    item.costo_unitario, 
                    item.total
                    );
            }

        }
    }
}
