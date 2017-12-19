---
UID: NE.pepfx._PEP_WORK_TYPE
title: _PEP_WORK_TYPE
author: windows-driver-content
description: The PEP_WORK_TYPE enumeration describes the type of work that the platform extension plug-in (PEP) is requesting.
old-location: kernel\pep_work_type.htm
old-project: kernel
ms.assetid: 5AED6B9E-5DB8-44AF-925C-4B587D100040
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _PEP_WORK_TYPE, PEP_WORK_TYPE, *PPEP_WORK_TYPE, PPEP_WORK_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_WORK_TYPE
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks.
---

# _PEP_WORK_TYPE enumeration



## -description
The <b>PEP_WORK_TYPE</b> enumeration describes the type of work that the platform extension plug-in (PEP) is requesting.



## -syntax

````
typedef enum _PEP_WORK_TYPE { 
  PepWorkActiveComplete,
  PepWorkRequestIdleState,
  PepWorkDevicePower,
  PepWorkRequestPowerControl,
  PepWorkDeviceIdle,
  PepWorkCompleteIdleState,
  PepWorkCompletePerfState,
  PepWorkAcpiNotify,
  PepWorkAcpiEvaluateControlMethodComplete,
  PepWorkMax
} PEP_WORK_TYPE;
````


## -enum-fields

### -field PepWorkActiveComplete

Reserved for use by the operating system.


### -field PepWorkRequestIdleState

Reserved for use by the operating system.


### -field PepWorkDevicePower

Reserved for use by the operating system.


### -field PepWorkRequestPowerControl

A request for the device driver to perform a custom power-control operation that uses a device-specific context that the PEP provides for the operation. The driver handles this request in its <a href="kernel.powercontrolcallback">PowerControlCallback</a> routine.


### -field PepWorkDeviceIdle

A request for the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) either to start ignoring idle time-outs for the specified device, or to start monitoring these time-outs.


### -field PepWorkCompleteIdleState

A notification to PoFx that the PEP has asynchronously completed the transition of a component to an idle state. PoFx previously initiated this transition by sending a <a href="kernel.pep_dpm_notify_component_idle_state">PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE</a> notification to the PEP.


### -field PepWorkCompletePerfState

A notification to PoFx that the PEP has asynchronously completed the transition of a component to a P-state. PoFx previously initiated this transition by sending a <a href="kernel.pep_dpm_request_component_perf_state">PEP_DPM_REQUEST_COMPONENT_PERF_STATE</a> notification to the PEP.


### -field PepWorkAcpiNotify

An ACPI Notify code to describe to PoFx a hardware event that the specified device has generated.


### -field PepWorkAcpiEvaluateControlMethodComplete

A notification to PoFx that the PEP has asynchronously finished evaluating an ACPI control method. PoFx previously initiated the evaluation of this method by sending a <a href="kernel.pep_notify_acpi_evaluate_control_method">PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD</a> notification to the PEP.


### -field PepWorkMax

Reserved for use by operating system.


## -remarks
This enumeration is used by the <a href="kernel.pep_work_information">PEP_WORK_INFORMATION</a> structure to describe the type of work item that the PEP is requesting.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported starting with Windows 10.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_dpm_notify_component_idle_state">PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE</a>
</dt>
<dt>
<a href="kernel.pep_dpm_request_component_perf_state">PEP_DPM_REQUEST_COMPONENT_PERF_STATE</a>
</dt>
<dt>
<a href="kernel.pep_notify_acpi_evaluate_control_method">PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD</a>
</dt>
<dt>
<a href="kernel.pep_work_information">PEP_WORK_INFORMATION</a>
</dt>
<dt>
<a href="kernel.powercontrolcallback">PowerControlCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_WORK_TYPE enumeration%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

