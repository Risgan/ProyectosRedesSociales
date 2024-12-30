using Pomodoro.Components.Models;
using Pomodoro.Components.Services.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Pomodoro.Components.Services
{
    public class ConfigruacionService : IConfiguracionService
    {

        private Configuracion _configuracion;


        public ConfigruacionService()
        {
            ResetDefault();
        }

        public Configuracion GetConfiguracion()
        {
            return _configuracion;
        }

        public void SetConfiguracion(Configuracion configuracion)
        {
            _configuracion = configuracion;
        }

        public void ResetDefault()
        {
            _configuracion = new Configuracion()
            {
                TiempoTrabajo = 25,
                TiempoDescansoCorto = 5,
                TiempoDescansoLargo = 15
            };
        }
        
    }
}
