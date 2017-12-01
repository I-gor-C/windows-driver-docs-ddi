---
UID: NS.pep_x._PEP_WORK_IDLE_STATE
title: PEP_WORK_IDLE_STATE
author: windows-driver-content
description: The PEP_WORK_IDLE_STATE structure contains a request to transition a component to an Fx power state.
old-location: kernel\pep_work_idle_state.htm
old-project: kernel
ms.assetid: DD8C454D-D0F6-456B-B59A-2E4DF2D757B5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_WORK_IDLE_STATE, PEP_WORK_IDLE_STATE, *PPEP_WORK_IDLE_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
req.include-header: Pepfx.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_WORK_IDLE_STATE
req.alt-loc: pep_x.h
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

# PEP_WORK_IDLE_STATE structure



## -description
<p>The <b>PEP_WORK_IDLE_STATE</b> structure contains a request to transition a component to an F<i>x</i> power state.</p>


## -syntax

````
typedef struct _PEP_WORK_IDLE_STATE {
  POHANDLE DeviceHandle;
  ULONG    Component;
  ULONG    State;
} PEP_WORK_IDLE_STATE, *PPEP_WORK_IDLE_STATE;
````


## -struct-fields
<dl>

### -field <b>DeviceHandle</b>

<dd>
<p>A handle that represents the registration of the device with the Windows <a href="https://msdn.microsoft.com/9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF">power management framework</a> (PoFx). A POHANDLE value that represents the registration of the device with PoFx. The platform extension plug-in (PEP) previously received this handle from PoFx during the <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification that informed the PEP that the device's driver stack registered the device with PoFx.</p>
</dd>

### -field <b>Component</b>

<dd>
<p>[in] The index that identifies the component. This member is an index into the <b>Components</b> array in the <a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a> structure that the PEP previously supplied in response to the <b>PEP_DPM_REGISTER_DEVICE</b> notification for this device. If the <b>Components</b> array contains N elements, component indexes range from 0 to N–1.</p>
</dd>

### -field <b>State</b>

<dd>
<p>The target F<i>x</i> power state to transition the component to. If this parameter is 0, the target state is F0; if this parameter is 1, the target state is F1; and so on. For more information about F<i>x</i> power states, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450935">Component-Level Power Management</a>.</p>
</dd>
</dl>

## -remarks
<p>The <b>IdleState</b> member of the <a href="..\pepfx\ns-pepfx--pep-work-information.md">PEP_WORK_INFORMATION</a> structure is a <b>PEP_WORK_IDLE_STATE</b> structure.</p>

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
<dt>Pep_x.h (include Pepfx.h)</dt>
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
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-work-information.md">PEP_WORK_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_WORK_IDLE_STATE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
