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

        private const string ConfiguracionKey = "ConfiguracionPomodoro";

        private readonly Configuracion configuracionPorDefecto = new Configuracion
        {
            TiempoTrabajo = 25,
            TiempoDescansoCorto = 5,
            TiempoDescansoLargo = 15
        };

        public async Task ActualizarConfiguracionAsync(Configuracion nuevaConfiguracion)
        {
            if(nuevaConfiguracion == null)
            {
                throw new ArgumentNullException(nameof(nuevaConfiguracion));
            }

            if (nuevaConfiguracion.TiempoTrabajo <= 0 || 
                nuevaConfiguracion.TiempoDescansoCorto <= 0 ||
                nuevaConfiguracion.TiempoDescansoLargo <=0)
            {
                throw new ArgumentException("El tiempo debe ser mayor a 0", nameof(nuevaConfiguracion));
            }

            string configuracionJson = JsonConvert.SerializeObject(nuevaConfiguracion);

            Preferences.Set(ConfiguracionKey, configuracionJson);

            await Task.CompletedTask;
        }

        public async Task<Configuracion> ObtenerConfiguracionAsync()
        {
            string configuracionJson = Preferences.Get(ConfiguracionKey, string.Empty);

            if (string.IsNullOrEmpty(configuracionJson))
            {
                return configuracionPorDefecto;
            }

            try
            {
                Configuracion config = JsonConvert.DeserializeObject<Configuracion>(configuracionJson);
                return config ?? configuracionPorDefecto;
            }
            catch (Exception)
            {

                return configuracionPorDefecto;
            }
        }
    }
}
