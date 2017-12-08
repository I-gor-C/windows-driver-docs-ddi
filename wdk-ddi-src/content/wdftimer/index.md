# Wdftimer.h header


This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdftimer.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WDF_TIMER_CONFIG_INIT function](nf-wdftimer-wdf-timer-config-init.md) | The WDF_TIMER_CONFIG_INIT function initializes a WDF_TIMER_CONFIG structure for a timer that will use a single due time. |
| [WDF_TIMER_CONFIG_INIT_PERIODIC function](nf-wdftimer-wdf-timer-config-init-periodic.md) | The WDF_TIMER_CONFIG_INIT_PERIODIC function initializes a WDF_TIMER_CONFIG structure for a periodic timer. |
| [WdfTimerCreate function](nf-wdftimer-wdftimercreate.md) | The WdfTimerCreate method creates a framework timer object. |
| [WdfTimerGetParentObject function](nf-wdftimer-wdftimergetparentobject.md) | The WdfTimerGetParentObject method returns a handle to the parent object of a specified framework timer object. |
| [WdfTimerStart function](nf-wdftimer-wdftimerstart.md) | The WdfTimerStart method starts a timer's clock. |
| [WdfTimerStop function](nf-wdftimer-wdftimerstop.md) | The WdfTimerStop method stops a timer's clock. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [WDF_TIMER_CONFIG structure](ns-wdftimer--wdf-timer-config.md) | The WDF_TIMER_CONFIG structure contains configuration information for a framework timer object. |
