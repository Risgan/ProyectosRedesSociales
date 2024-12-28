using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SistemaInventario
{
    public class baseDatosService
    {

        private readonly List<base_datos> _db;

        public baseDatosService()
        {
            _db = new List<base_datos>();
        }

        public baseDatosService(List<base_datos> db)
        {
            _db = db;
        }

        public void Registro(base_datos db)
        {
            _db.Add(db);
        }

        public List<base_datos> getKardex()
        {
            return _db;
        }

        public int getSaldo(string producto)
        {
            return _db.Where(x => x.producto == producto).Sum(x => x.entrada) - _db.Where(x => x.producto == producto).Sum(x => x.salida);

        }
    }
}
