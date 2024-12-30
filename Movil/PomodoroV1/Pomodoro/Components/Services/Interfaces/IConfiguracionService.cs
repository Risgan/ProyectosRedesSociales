using Pomodoro.Components.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pomodoro.Components.Services.Interfaces
{
    public interface IConfiguracionService
    {
        Configuracion GetConfiguracion();
        void SetConfiguracion(Configuracion configuracion);
        void ResetDefault();

    }
}
