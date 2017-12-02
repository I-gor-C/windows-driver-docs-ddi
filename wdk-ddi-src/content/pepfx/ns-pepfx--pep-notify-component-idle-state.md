---
UID: NS.pepfx._PEP_NOTIFY_COMPONENT_IDLE_STATE
title: PEP_NOTIFY_COMPONENT_IDLE_STATE
author: windows-driver-content
description: The PEP_NOTIFY_COMPONENT_IDLE_STATE structure contains status information about a component's pending transition to a new Fx power state.
old-location: kernel\pep_notify_component_idle_state.htm
old-project: kernel
ms.assetid: 63DB9626-BB05-43C4-BBC0-3A63ED5D6E94
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_NOTIFY_COMPONENT_IDLE_STATE, PEP_NOTIFY_COMPONENT_IDLE_STATE, *PPEP_NOTIFY_COMPONENT_IDLE_STATE
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
req.alt-api: PEP_NOTIFY_COMPONENT_IDLE_STATE
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

# PEP_NOTIFY_COMPONENT_IDLE_STATE structure



## -description
<p>The <b>PEP_NOTIFY_COMPONENT_IDLE_STATE</b> structure contains status information about a component's pending transition to a new F<i>x</i> power state.</p>


## -syntax

````
typedef struct _PEP_NOTIFY_COMPONENT_IDLE_STATE {
  PEPHANDLE DeviceHandle;
  ULONG     Component;
  ULONG     IdleState;
  BOOLEAN   DriverNotified;
  BOOLEAN   Completed;
} PEP_NOTIFY_COMPONENT_IDLE_STATE, *PPEP_NOTIFY_COMPONENT_IDLE_STATE;
````


## -struct-fields
<dl>

### -field DeviceHandle

<dd>
<p>[in] A PEPHANDLE value that identifies the device. The PEP supplied this handle in response to a previous <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification.</p>
</dd>

### -field Component

<dd>
<p>[in] The index that identifies the component. This member is an index into the <b>Components</b> array in the <a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a> structure that the PEP previously supplied in response to the <b>PEP_DPM_REGISTER_DEVICE</b> notification for this device. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -field IdleState

<dd>
<p>[in] The new F<i>x</i> power state that the component will transition to. If this parameter is zero, the new state is F0; if this parameter is one, the new state is F1; and so on.</p>
</dd>

### -field DriverNotified

<dd>
<p>[in] Whether the driver for the device has already been notified of the pending transition to the new F<i>x</i> state. If TRUE, the <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) already notified the driver by calling the driver's <a href="kernel.componentidlestatecallback">ComponentIdleStateCallback</a> callback routine. If FALSE, PoFx has not yet notified the driver.</p>
</dd>

### -field Completed

<dd>
<p>[out] Whether the PEP has completed all necessary preparations for the specified component to enter the new F<i>x</i> state. Set to TRUE to indicate that the PEP has completed all necessary preparations, or to FALSE to indicate that is has not.</p>
<p>If FALSE, the PEP must complete the necessary preparations at a later time and then inform PoFx when the preparations have been completed. To do so, the PEP calls the <a href="kernel.requestworker">RequestWorker</a> routine to request a work item, and then responds to the ensuing <a href="kernel.pep_dpm_work">PEP_DPM_WORK</a> notification by submitting a work request of type <b>PepWorkCompleteIdleState</b> to inform PoFx that the preparations are complete.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_dpm_notify_component_idle_state">PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE</a> notification. The first four members of this structure contain input values that are supplied by PoFx. The <b>Completed</b> member contains an output value that the PEP writes to the structure in response to this notification.</p>

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
<a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a>
</dt>
<dt>
<a href="kernel.pep_dpm_notify_component_idle_state">PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="kernel.pep_dpm_work">PEP_DPM_WORK</a>
</dt>
<dt>
<a href="kernel.requestworker">RequestWorker</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_NOTIFY_COMPONENT_IDLE_STATE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
