using Pomodoro.Components.Models;
using Pomodoro.Components.Services.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pomodoro.Components.Services
{
    public class SecuenciaService : ISecuenciaService
    {
        private Secuencia _secuenciaActual;
        private List<SecuenciaItem> Ejecucion = new List<SecuenciaItem>()
        {
            new SecuenciaItem(0, Secuencia.Empezar),
            new SecuenciaItem(1, Secuencia.Trabajo),
            new SecuenciaItem(2, Secuencia.DescansoCorto),
            new SecuenciaItem(3, Secuencia.Trabajo),
            new SecuenciaItem(4, Secuencia.DescansoCorto),
            new SecuenciaItem(5, Secuencia.Trabajo),
            new SecuenciaItem(6, Secuencia.DescansoCorto),
            new SecuenciaItem(7, Secuencia.Trabajo),
            new SecuenciaItem(8, Secuencia.DescansoLargo),
            new SecuenciaItem(9, Secuencia.Finalizado)
        };

        public Secuencia[] GetAllSecuencias()
        {
            return (Secuencia[])Enum.GetValues(typeof(Secuencia));
        }

        public Secuencia GetSecuenciaById(int id)
        {
            return (Secuencia)id;
        }

        public Secuencia GetSecuenciaByName(string name)
        {
            return (Secuencia)Enum.Parse(typeof(Secuencia), name);
        }

        public void SetSecuencia(Secuencia nuevaSecuencia)
        {
            _secuenciaActual = nuevaSecuencia;
        }

        public Secuencia GetSecuenciaActual()
        {
            return _secuenciaActual;
        }

        public List<SecuenciaItem> GetEjecucionall()
        {
            return Ejecucion;
        }

        public Secuencia GetEjecucionById(int id)
        {
            return Ejecucion.FirstOrDefault(x => x.Id == id).Secuencia;
        }
    }
}
