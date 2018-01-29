---
UID : NE:pepfx._PEP_WORK_TYPE
title : _PEP_WORK_TYPE
author : windows-driver-content
description : The PEP_WORK_TYPE enumeration describes the type of work that the platform extension plug-in (PEP) is requesting.
old-location : kernel\pep_work_type.htm
old-project : kernel
ms.assetid : 5AED6B9E-5DB8-44AF-925C-4B587D100040
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PepWorkAcpiNotify, PepWorkRequestIdleState, pepfx/PepWorkRequestPowerControl, *PPEP_WORK_TYPE, _PEP_WORK_TYPE, PepWorkCompleteIdleState, pepfx/PepWorkDeviceIdle, pepfx/PepWorkCompletePerfState, pepfx/PepWorkCompleteIdleState, PepWorkDevicePower, pepfx/PepWorkActiveComplete, pepfx/PepWorkAcpiEvaluateControlMethodComplete, PepWorkAcpiEvaluateControlMethodComplete, PEP_WORK_TYPE enumeration [Kernel-Mode Driver Architecture], pepfx/PepWorkAcpiNotify, pepfx/PEP_WORK_TYPE, PEP_WORK_TYPE, PepWorkRequestPowerControl, pepfx/PepWorkRequestIdleState, pepfx/PepWorkMax, PepWorkCompletePerfState, pepfx/PepWorkDevicePower, kernel.pep_work_type, PepWorkActiveComplete, PepWorkDeviceIdle, PepWorkMax
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : pepfx.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Supported starting with Windows 10.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : See Remarks.
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPEP_WORK_TYPE, PEP_WORK_TYPE"
---

# _PEP_WORK_TYPE Enumeration
The <b>PEP_WORK_TYPE</b> enumeration describes the type of work that the platform extension plug-in (PEP) is requesting.

## Syntax
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

## Constants

<table>

<tr>
<td>PepWorkAcpiEvaluateControlMethodComplete</td>
<td>A notification to PoFx that the PEP has asynchronously finished evaluating an ACPI control method. PoFx previously initiated the evaluation of this method by sending a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186659">PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD</a> notification to the PEP.</td>
</tr>

<tr>
<td>PepWorkAcpiNotify</td>
<td>An ACPI Notify code to describe to PoFx a hardware event that the specified device has generated.</td>
</tr>

<tr>
<td>PepWorkCompleteIdleState</td>
<td>A notification to PoFx that the PEP has asynchronously completed the transition of a component to an idle state. PoFx previously initiated this transition by sending a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186759">PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE</a> notification to the PEP.</td>
</tr>

<tr>
<td>PepWorkCompletePerfState</td>
<td>A notification to PoFx that the PEP has asynchronously completed the transition of a component to a P-state. PoFx previously initiated this transition by sending a <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186852">PEP_DPM_REQUEST_COMPONENT_PERF_STATE</a> notification to the PEP.</td>
</tr>

<tr>
<td>PepWorkMax</td>
<td>Reserved for use by operating system.</td>
</tr>

<tr>
<td>PepWorkRequestPowerControl</td>
<td>A request for the device driver to perform a custom power-control operation that uses a device-specific context that the PEP provides for the operation. The driver handles this request in its <a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a> routine.</td>
</tr>
</table>

## Remarks

This enumeration is used by the <a href="..\pepfx\ns-pepfx-_pep_work_information.md">PEP_WORK_INFORMATION</a> structure to describe the type of work item that the PEP is requesting.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pepfx.h |

## See Also

<a href="..\pepfx\ns-pepfx-_pep_work_information.md">PEP_WORK_INFORMATION</a>

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186852">PEP_DPM_REQUEST_COMPONENT_PERF_STATE</a>

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186659">PEP_NOTIFY_ACPI_EVALUATE_CONTROL_METHOD</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a>

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186759">PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_WORK_TYPE enumeration%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>