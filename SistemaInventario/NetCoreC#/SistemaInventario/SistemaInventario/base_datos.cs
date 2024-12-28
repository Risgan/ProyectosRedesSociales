using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SistemaInventario
{
    public class base_datos
    {
        public DateTime fecha { get; set; }
        public string producto { get; set; }
        public string descripcion { get; set; }
        public string documento { get; set; }
        public int entrada { get; set; }
        public int salida { get; set; }
        public int saldo { get; set; }
        public int costo_unitario { get; set; }
        public int total { get; set; }
    }
}
