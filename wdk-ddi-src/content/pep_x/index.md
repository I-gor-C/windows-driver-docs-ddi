---
UID : NA:pep_x
ms.assetid : 58bb1f9b-0265-3590-af11-186f988fd807
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# pep_x.h header



pep_x.h contains the following programming interfaces:







## Structures
| Title | Description |
| ---- |:---- |
| [_PEP_COMPONENT_ACTIVE](ns-pep_x-_pep_component_active.md) | The PEP_COMPONENT_ACTIVE structure identifies a component that is making a transition between the idle condition and the active condition. |
| [_PEP_KERNEL_INFORMATION_STRUCT_V1](ns-pep_x-_pep_kernel_information_struct_v1.md) | The PEP_KERNEL_INFORMATION structure specifies the interface that the power extension plug-in (PEP) uses to request services from the Windows power management framework (PoFx). |
| [_PEP_KERNEL_INFORMATION_STRUCT_V2](ns-pep_x-_pep_kernel_information_struct_v2.md) | The PEP_KERNEL_INFORMATION structure specifies the interface that the power extension plug-in (PEP) uses to request services from the Windows power management framework (PoFx). |
| [_PEP_PPM_IDLE_CANCEL](ns-pep_x-_pep_ppm_idle_cancel.md) | The PEP_PPM_IDLE_CANCEL structure indicates why the processor could not enter the previously selected idle state. |
| [_PEP_PPM_IDLE_SELECT](ns-pep_x-_pep_ppm_idle_select.md) | The PEP_PPM_IDLE_SELECT structure describes the most energy-efficient idle state that the processor can enter and still satisfy the constraints specified by the operating system. |
| [_PEP_PPM_QUERY_IDLE_STATES](ns-pep_x-_pep_ppm_query_idle_states.md) | The PEP_PPM_QUERY_IDLE_STATES structure describes the idle states of a particular processor. |
| [_PEP_PPM_QUERY_LP_SETTINGS](ns-pep_x-_pep_ppm_query_lp_settings.md) | The PEP_PPM_QUERY_LP_SETTINGS structure contains a kernel handle to the registry key that contains the power optimization settings that the platform extension plug-in (PEP) has defined for each power scenario. |
| [_PEP_PROCESSOR_IDLE_CONSTRAINTS](ns-pep_x-_pep_processor_idle_constraints.md) | The PEP_PROCESSOR_IDLE_CONSTRAINTS structure specifies a set of constraints that the PEP uses to select a processor idle state. |
| [_PEP_PROCESSOR_IDLE_STATE](ns-pep_x-_pep_processor_idle_state.md) | The PEP_PROCESSOR_IDLE_STATE structure describes the capabilities of a processor idle state. |
| [_PEP_WORK_ACTIVE_COMPLETE](ns-pep_x-_pep_work_active_complete.md) | The PEP_WORK_ACTIVE_COMPLETE structure identifies a component that is now in the active condition. |
| [_PEP_WORK_DEVICE_IDLE](ns-pep_x-_pep_work_device_idle.md) | The PEP_WORK_DEVICE_IDLE structure indicates whether to ignore the idle time-out for the specified device. |
| [_PEP_WORK_DEVICE_POWER](ns-pep_x-_pep_work_device_power.md) | The PEP_WORK_DEVICE_POWER structure describes the new power requirements for the specified device. |
| [_PEP_WORK_IDLE_STATE](ns-pep_x-_pep_work_idle_state.md) | The PEP_WORK_IDLE_STATE structure contains a request to transition a component to an Fx power state. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [*PPEP_PROCESSOR_IDLE_CANCEL_CODE](ne-pep_x-ppep_processor_idle_cancel_code.md) | The PEP_PROCESSOR_IDLE_CANCEL_CODE enumeration values indicate reasons why a processor cannot enter an idle state that was previously selected by the platform extension plug-in (PEP). |
| [*PPEP_PROCESSOR_IDLE_TYPE](ne-pep_x-ppep_processor_idle_type.md) | The PEP_PROCESSOR_IDLE_TYPE enumeration indicates whether idle constraints apply to just the current processor or to all processors in the hardware platform. |