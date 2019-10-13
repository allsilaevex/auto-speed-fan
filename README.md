# auto-speed-fan
Utility for automatic fan speed control.

For example, you can use [this](https://github.com/neduard/acer_5750G_fan_maximiser) controller.

### Usage
Simple start:
```
sudo python3 ./main.py
```
Configured start:
```
sudo python3 ./main.py --path ./my_fan_controller.pl --temp 85 --sleep 15 --log 1 --log_path ./logs.log
```

### Parameters

- `path` - path to fan controller (default: `./fan_controller.pl`)
- `temp` - upper limit to enable max mode (default: `75`)
- `sleep` - time between temperature checks (default: `5`)
- `log` - activate logging (default: `false`)
- `log_path` - path to log file (default: `./app.log`)
