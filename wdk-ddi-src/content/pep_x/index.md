---
UID: NA:
---

# Pep_X.h header

## -description

This header is used by Windows kernel. For more information, see
- [Windows kernel](../_kernel/index.md)

Pep_X.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_PEP_COMPONENT_ACTIVE structure](ns-pep_x-_pep_component_active.md) | The PEP_COMPONENT_ACTIVE structure identifies a component that is making a transition between the idle condition and the active condition. |
| [_PEP_PPM_IDLE_CANCEL structure](ns-pep_x-_pep_ppm_idle_cancel.md) | The PEP_PPM_IDLE_CANCEL structure indicates why the processor could not enter the previously selected idle state. |
| [_PEP_PPM_IDLE_SELECT structure](ns-pep_x-_pep_ppm_idle_select.md) | The PEP_PPM_IDLE_SELECT structure describes the most energy-efficient idle state that the processor can enter and still satisfy the constraints specified by the operating system. |
| [_PEP_PPM_QUERY_IDLE_STATES structure](ns-pep_x-_pep_ppm_query_idle_states.md) | The PEP_PPM_QUERY_IDLE_STATES structure describes the idle states of a particular processor. |
| [_PEP_PPM_QUERY_LP_SETTINGS structure](ns-pep_x-_pep_ppm_query_lp_settings.md) | The PEP_PPM_QUERY_LP_SETTINGS structure contains a kernel handle to the registry key that contains the power optimization settings that the platform extension plug-in (PEP) has defined for each power scenario. |
| [_PEP_PROCESSOR_IDLE_CONSTRAINTS structure](ns-pep_x-_pep_processor_idle_constraints.md) | The PEP_PROCESSOR_IDLE_CONSTRAINTS structure specifies a set of constraints that the PEP uses to select a processor idle state. |
| [_PEP_PROCESSOR_IDLE_STATE structure](ns-pep_x-_pep_processor_idle_state.md) | The PEP_PROCESSOR_IDLE_STATE structure describes the capabilities of a processor idle state. |
| [_PEP_WORK_ACTIVE_COMPLETE structure](ns-pep_x-_pep_work_active_complete.md) | The PEP_WORK_ACTIVE_COMPLETE structure identifies a component that is now in the active condition. |
| [_PEP_WORK_DEVICE_IDLE structure](ns-pep_x-_pep_work_device_idle.md) | The PEP_WORK_DEVICE_IDLE structure indicates whether to ignore the idle time-out for the specified device. |
| [_PEP_WORK_DEVICE_POWER structure](ns-pep_x-_pep_work_device_power.md) | The PEP_WORK_DEVICE_POWER structure describes the new power requirements for the specified device. |
| [_PEP_WORK_IDLE_STATE structure](ns-pep_x-_pep_work_idle_state.md) | The PEP_WORK_IDLE_STATE structure contains a request to transition a component to an Fx power state. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [PPEP_PROCESSOR_IDLE_CANCEL_CODE enumeration](ne-pep_x-ppep_processor_idle_cancel_code.md) | The PEP_PROCESSOR_IDLE_CANCEL_CODE enumeration values indicate reasons why a processor cannot enter an idle state that was previously selected by the platform extension plug-in (PEP). |
| [PPEP_PROCESSOR_IDLE_TYPE enumeration](ne-pep_x-ppep_processor_idle_type.md) | The PEP_PROCESSOR_IDLE_TYPE enumeration indicates whether idle constraints apply to just the current processor or to all processors in the hardware platform. |
