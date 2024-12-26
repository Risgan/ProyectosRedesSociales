using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pomodoro.Components.Models
{
    public enum Secuencia
    {
        Empezar,
        Trabajo,
        DescansoCorto,
        DescansoLargo,
        Finalizado
    }

    public class SecuenciaItem
    {
        public int Id { get; set; }
        public Secuencia Secuencia { get; set; }

        public SecuenciaItem(int id, Secuencia secuencia)
        {
            Id = id;
            Secuencia = secuencia;
        }
    }
}
