using Pomodoro.Components.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pomodoro.Components.Services.Interfaces
{
    public interface ISecuenciaService
    {
        Secuencia[] GetAllSecuencias();
        Secuencia GetSecuenciaById(int id);
        Secuencia GetSecuenciaByName(string name);
        void SetSecuencia(Secuencia nuevaSecuencia);
        Secuencia GetSecuenciaActual();
        List<SecuenciaItem> GetEjecucionall();
        Secuencia GetEjecucionById(int id);
    }
}
