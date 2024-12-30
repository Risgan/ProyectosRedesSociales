using Pomodoro.Components.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Timers;

namespace Pomodoro.Components.Services.Interfaces
{
    public interface ITimerService
    {
        event Action<TimeSpan> OnTick;
        event Action OnPomodoroCompleted;
        event Action OnShortBreakCompleted;
        event Action OnLongBreakCompleted;
        event Action<bool> IsPaused;

        void ConfigPomodoro(TimeSpan tiempoTrabajo, TimeSpan descansoCorto, TimeSpan descansoLargo);
        void StartPomodoro();
        void Pause();
        void Resume();
        void Stop();
        void SetDuration(TimeSpan duracion);

    }
}
