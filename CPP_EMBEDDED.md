# Embedded C++ companion

Bounded metric dependency DAG validator for telemetry firmware. The C++ companion uses caller-owned static string literals and integer IDs, not Python's metadata dictionaries, JSON export, or dynamic storage. Do not pass temporary C strings. Cycle detection is fail-closed.

Run: `cmake -S . -B build && cmake --build build && ctest --test-dir build --output-on-failure`.

The original Python implementation and its tests are unchanged. C++ uses fixed-capacity storage and rejects invalid inputs. Capacity overflow latches a fault; call reset only after handling the fault. Host tests are not hardware verification. No physical Arduino/ESP32 wiring, sensor calibration, watchdog, power-loss recovery, or actuator safety is supplied. Keep this logic isolated from live actuators until validated on the target board.
