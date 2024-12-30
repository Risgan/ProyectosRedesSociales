using System;
using System.Timers;
using Pomodoro.Components.Models;
using Pomodoro.Components.Services.Interfaces;
using Timer = System.Timers.Timer;

namespace Pomodoro.Components.Services
{
    public class TimerService : ITimerService
    {
        private Timer _timer;
        private TimeSpan _tiempoTrabajo;
        private TimeSpan _descansoCorto;
        private TimeSpan _descansoLargo;
        private TimeSpan _duracion;
        private bool _isPaused;

        private int timeExecution = 10;

        public event Action<TimeSpan> OnTick;
        public event Action OnPomodoroCompleted;
        public event Action OnShortBreakCompleted;
        public event Action OnLongBreakCompleted;
        public event Action<bool> IsPaused;

        public void ConfigPomodoro(TimeSpan tiempoTrabajo, TimeSpan descansoCorto, TimeSpan descansoLargo)
        {
            _tiempoTrabajo = tiempoTrabajo;
            _descansoCorto = descansoCorto;
            _descansoLargo = descansoLargo;
            SetDuration(_tiempoTrabajo);
            _isPaused = false;
        }

        public void StartPomodoro()
        {
            _timer = new Timer(timeExecution);
            _timer.Elapsed += TimerElapsed;
            _timer.Start();
        }

        private void TimerElapsed(object sender, ElapsedEventArgs e)
        {
            if (_isPaused) return;

            _duracion = _duracion.Subtract(TimeSpan.FromSeconds(1));
            OnTick?.Invoke(_duracion);

            if (_duracion.TotalSeconds <= 0)
            {
                Stop();
                OnPomodoroCompleted?.Invoke();
            }
        }

        public void Pause()
        {
            _isPaused = true;
            notifyPause();
        }

        public void Resume()
        {
            _isPaused = false;
            notifyPause();
        }

        public void Stop()
        {
            _timer?.Stop();
            _timer?.Dispose();
            _timer = null;
            Resume();
        }

        public void SetDuration(TimeSpan duracion)
        {
            _duracion = duracion;
        }

        private void notifyPause()
        {
            IsPaused.Invoke(_isPaused);
        }
    }
}