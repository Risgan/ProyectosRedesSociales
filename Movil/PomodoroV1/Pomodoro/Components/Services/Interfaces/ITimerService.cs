using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Timers;

namespace Pomodoro.Components.Services.Interfaces
{
    public interface ITimerService
    {
        event Action<TimeSpan> OnTimerTick;
        event Action OnTimerComplete;
        void StartTimer(TimeSpan duration);
        void StopTimer();
        void PauseTimer();
        void RestarTimer(TimeSpan duration);
    }
}
