# Declarations in the wdftimer header
This header Wdftimer contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFTIMERGETPARENTOBJECT callback function](nc-wdftimer-pfn-wdftimergetparentobject.md) | TBD |
| [PFN_WDFTIMERSTART callback function](nc-wdftimer-pfn-wdftimerstart.md) | TBD |
| [PFN_WDFTIMERCREATE callback function](nc-wdftimer-pfn-wdftimercreate.md) | TBD |
| [*PFN_WDFTIMERSTOP callback function](nc-wdftimer-pfn-wdftimerstop.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfTimerStart function](nf-wdftimer-wdftimerstart.md) | The WdfTimerStart method starts a timer's clock. |
| [WdfTimerGetParentObject function](nf-wdftimer-wdftimergetparentobject.md) | The WdfTimerGetParentObject method returns a handle to the parent object of a specified framework timer object. |
| [WdfTimerStop function](nf-wdftimer-wdftimerstop.md) | The WdfTimerStop method stops a timer's clock. |
| [WdfTimerCreate function](nf-wdftimer-wdftimercreate.md) | The WdfTimerCreate method creates a framework timer object. |
| [WDF_TIMER_CONFIG_INIT function](nf-wdftimer-wdf-timer-config-init.md) | The WDF_TIMER_CONFIG_INIT function initializes a WDF_TIMER_CONFIG structure for a timer that will use a single due time. |
| [WDF_TIMER_CONFIG_INIT_PERIODIC function](nf-wdftimer-wdf-timer-config-init-periodic.md) | The WDF_TIMER_CONFIG_INIT_PERIODIC function initializes a WDF_TIMER_CONFIG structure for a periodic timer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_TIMER_CONFIG structure](ns-wdftimer--wdf-timer-config.md) | The WDF_TIMER_CONFIG structure contains configuration information for a framework timer object. |

This header is used in these topics:

- [wdf](..content/_wdf)
