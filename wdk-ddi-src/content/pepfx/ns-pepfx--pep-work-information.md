---
UID: NS.pepfx._PEP_WORK_INFORMATION
title: PEP_WORK_INFORMATION
author: windows-driver-content
description: The PEP_WORK_INFORMATION structure describes a work item that the PEP is submitting to the Windows power management framework (PoFx).
old-location: kernel\pep_work_information.htm
old-project: kernel
ms.assetid: 7A3B2A94-AE6F-4DCC-9CDF-E2D5799C9F0D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_WORK_INFORMATION, PEP_WORK_INFORMATION, *PPEP_WORK_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_WORK_INFORMATION
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PEP_WORK_INFORMATION structure



## -description
<p>The <b>PEP_WORK_INFORMATION</b> structure describes a work item that the PEP is submitting to the Windows <a href="https://msdn.microsoft.com/9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF">power management framework</a> (PoFx).</p>


## -syntax

````
typedef struct _PEP_WORK_INFORMATION {
  PEP_WORK_TYPE WorkType;
  union {
    PEP_WORK_POWER_CONTROL                         PowerControl;
    PEP_WORK_COMPLETE_IDLE_STATE                   CompleteIdleState;
    PEP_WORK_COMPLETE_PERF_STATE                   CompletePerfState;
    PEP_WORK_ACPI_NOTIFY                           AcpiNotify;
    PEP_WORK_ACPI_EVALUATE_CONTROL_METHOD_COMPLETE ControlMethodComplete;
  };
} PEP_WORK_INFORMATION, *PPEP_WORK_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>WorkType</b>

<dd>
<p>A <a href="..\pepfx\ne-pepfx--pep-work-type.md">PEP_WORK_TYPE</a> enumeration value. This member indicates the type of work requested by the PEP, which also determines the type of structure that is contained in the unnamed union in the <b>PEP_WORK_INFORMATION</b> structure.</p>
</dd>

### -field ( <i>unnamed union</i> )

<dd>
<p>The data structure that is associated with the type of work specified by the <b>WorkType</b> member.</p>
<dl>

### -field <b>PowerControl</b>

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-work-power-control.md">PEP_WORK_POWER_CONTROL</a> structure. This structure is used if <b>WorkType</b> = <b>PepWorkRequestPowerControl</b>.</p>
</dd>

### -field <b>CompleteIdleState</b>

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-work-complete-idle-state.md">PEP_WORK_COMPLETE_IDLE_STATE</a> structure. This structure is used if <b>WorkType</b> = <b>PepWorkCompleteIdleState</b>.</p>
</dd>

### -field <b>CompletePerfState</b>

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-work-complete-perf-state.md">PEP_WORK_COMPLETE_PERF_STATE</a> structure. This structure is used if <b>WorkType</b> = <b>PepWorkCompletePerfState</b>.</p>
</dd>

### -field <b>AcpiNotify</b>

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-work-acpi-notify.md">PEP_WORK_ACPI_NOTIFY</a> structure. This structure is used if <b>WorkType</b> = <b>PepWorkAcpiNotify</b>.</p>
</dd>

### -field <b>ControlMethodComplete</b>

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-work-acpi-evaluate-control-method-complete.md">PEP_WORK_ACPI_EVALUATE_CONTROL_METHOD_COMPLETE</a> structure. This structure is used if <b>WorkType</b> = <b>PepWorkAcpiEvaluateControlMethodComplete</b>.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>WorkInformation</b> member of the <a href="..\pepfx\ns-pepfx--pep-work.md">PEP_WORK</a> structure is a pointer to a <b>PEP_WORK_INFORMATION</b> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="kernel.pep_dpm_work">PEP_DPM_WORK</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work.md">PEP_WORK</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work-acpi-notify.md">PEP_WORK_ACPI_NOTIFY</a>
</dt>
<dt>
<a href="..\pep_x\ns-pep-x--pep-work-active-complete.md">PEP_WORK_ACTIVE_COMPLETE</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work-complete-idle-state.md">PEP_WORK_COMPLETE_IDLE_STATE</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work-complete-perf-state.md">PEP_WORK_COMPLETE_PERF_STATE</a>
</dt>
<dt>
<a href="..\pep_x\ns-pep-x--pep-work-device-idle.md">PEP_WORK_DEVICE_IDLE</a>
</dt>
<dt>
<a href="..\pep_x\ns-pep-x--pep-work-device-power.md">PEP_WORK_DEVICE_POWER</a>
</dt>
<dt>
<a href="..\pep_x\ns-pep-x--pep-work-idle-state.md">PEP_WORK_IDLE_STATE</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work-power-control.md">PEP_WORK_POWER_CONTROL</a>
</dt>
<dt>
<a href="..\pepfx\ne-pepfx--pep-work-type.md">PEP_WORK_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_WORK_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
