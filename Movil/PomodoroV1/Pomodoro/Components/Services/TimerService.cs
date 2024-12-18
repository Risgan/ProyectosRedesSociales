using Pomodoro.Components.Services.Interfaces;
using System;
using System.Timers;
using Timer = System.Timers.Timer;

namespace Pomodoro.Components.Services
{
    public class TimerService : ITimerService, IDisposable
    {
        private Timer _timer;
        private TimeSpan _timeRemaining;
        private bool _isPaused = false;


        public event Action<TimeSpan> OnTimerTick;
        public event Action OnTimerComplete;

        public void PauseTimer()
        {
            if (_timer != null && _timer.Enabled)
            {
                _timer.Stop();
                _isPaused = true;
            }
        }

        public void RestarTimer(TimeSpan duration)
        {
            StopTimer();
            StartTimer(duration);
        }

        public void StartTimer(TimeSpan duration)
        {
            _timeRemaining = duration;
            _isPaused = false;

            if(_timer == null)
            {
                _timer = new Timer(1000);
                _timer.Elapsed += TimerElapsed;
                _timer.AutoReset = true;
            }

            _timer.Start();
            OnTimerTick?.Invoke(_timeRemaining);
        }

        public void StopTimer()
        {
            if (_timer != null)
            {
                _timer.Stop();
                _timer.Dispose();
                _timer = null;
            }

            _timeRemaining = TimeSpan.Zero;
            _isPaused = false;
            OnTimerTick?.Invoke(_timeRemaining);
        }

        private void TimerElapsed(object sender, ElapsedEventArgs e)
        {
            if (!_isPaused)
            {
                _timeRemaining = _timeRemaining.Subtract(TimeSpan.FromSeconds(1));

                if(_timeRemaining <= TimeSpan.Zero)
                {
                    _timer.Stop();
                    OnTimerTick?.Invoke(TimeSpan.Zero);
                    OnTimerComplete?.Invoke();
                }
                else
                {
                    OnTimerTick?.Invoke(_timeRemaining);
                }
            }
        }

        public void Dispose()
        {
            if (_timer != null)
            {
                _timer.Stop();
                _timer.Elapsed -= TimerElapsed;
                _timer.Dispose();
                _timer = null;
            }
        }
    }
}
