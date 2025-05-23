﻿using Microsoft.Extensions.Logging;
using Pomodoro.Components.Services;
using Pomodoro.Components.Services.Interfaces;

namespace Pomodoro
{
    public static class MauiProgram
    {
        public static MauiApp CreateMauiApp()
        {
            var builder = MauiApp.CreateBuilder();
            builder
                .UseMauiApp<App>()
                .ConfigureFonts(fonts =>
                {
                    fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
                });

            builder.Services.AddMauiBlazorWebView();

            builder.Services.AddSingleton<ITimerService, TimerService>();
            builder.Services.AddSingleton<IConfiguracionService, ConfigruacionService>();
            builder.Services.AddSingleton<ISecuenciaService, SecuenciaService>();

#if DEBUG
            builder.Services.AddBlazorWebViewDeveloperTools();
    		builder.Logging.AddDebug();
#endif

            return builder.Build();
        }
    }
}
