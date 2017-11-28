# Pep_X.h header


This header is used by unknown technology.

Pep_X.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [PEP_COMPONENT_ACTIVE structure](ns-pep-x--pep-component-active.md) | The PEP_COMPONENT_ACTIVE structure identifies a component that is making a transition between the idle condition and the active condition. |
| [PEP_PPM_IDLE_CANCEL structure](ns-pep-x--pep-ppm-idle-cancel.md) | The PEP_PPM_IDLE_CANCEL structure indicates why the processor could not enter the previously selected idle state. |
| [PEP_PPM_IDLE_SELECT structure](ns-pep-x--pep-ppm-idle-select.md) | The PEP_PPM_IDLE_SELECT structure describes the most energy-efficient idle state that the processor can enter and still satisfy the constraints specified by the operating system. |
| [PEP_PPM_QUERY_IDLE_STATES structure](ns-pep-x--pep-ppm-query-idle-states.md) | The PEP_PPM_QUERY_IDLE_STATES structure describes the idle states of a particular processor. |
| [PEP_PPM_QUERY_LP_SETTINGS structure](ns-pep-x--pep-ppm-query-lp-settings.md) | The PEP_PPM_QUERY_LP_SETTINGS structure contains a kernel handle to the registry key that contains the power optimization settings that the platform extension plug-in (PEP) has defined for each power scenario. |
| [PEP_PROCESSOR_IDLE_CONSTRAINTS structure](ns-pep-x--pep-processor-idle-constraints.md) | The PEP_PROCESSOR_IDLE_CONSTRAINTS structure specifies a set of constraints that the PEP uses to select a processor idle state. |
| [PEP_PROCESSOR_IDLE_STATE structure](ns-pep-x--pep-processor-idle-state.md) | The PEP_PROCESSOR_IDLE_STATE structure describes the capabilities of a processor idle state. |
| [PEP_WORK_ACTIVE_COMPLETE structure](ns-pep-x--pep-work-active-complete.md) | The PEP_WORK_ACTIVE_COMPLETE structure identifies a component that is now in the active condition. |
| [PEP_WORK_DEVICE_IDLE structure](ns-pep-x--pep-work-device-idle.md) | The PEP_WORK_DEVICE_IDLE structure indicates whether to ignore the idle time-out for the specified device. |
| [PEP_WORK_DEVICE_POWER structure](ns-pep-x--pep-work-device-power.md) | The PEP_WORK_DEVICE_POWER structure describes the new power requirements for the specified device. |
| [PEP_WORK_IDLE_STATE structure](ns-pep-x--pep-work-idle-state.md) | The PEP_WORK_IDLE_STATE structure contains a request to transition a component to an Fx power state. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [PPEP_PROCESSOR_IDLE_CANCEL_CODE enumeration](ne-pep-x-ppep-processor-idle-cancel-code.md) | The PEP_PROCESSOR_IDLE_CANCEL_CODE enumeration values indicate reasons why a processor cannot enter an idle state that was previously selected by the platform extension plug-in (PEP). |
| [PPEP_PROCESSOR_IDLE_TYPE enumeration](ne-pep-x-ppep-processor-idle-type.md) | The PEP_PROCESSOR_IDLE_TYPE enumeration indicates whether idle constraints apply to just the current processor or to all processors in the hardware platform. |
