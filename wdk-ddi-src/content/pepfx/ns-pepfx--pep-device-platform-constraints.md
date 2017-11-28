---
UID: NS.pepfx._PEP_DEVICE_PLATFORM_CONSTRAINTS
title: PEP_DEVICE_PLATFORM_CONSTRAINTS
author: windows-driver-content
description: The PEP_DEVICE_PLATFORM_CONSTRAINTS structure specifies the constraints for entry to the various Dx power states that are supported by a device.
old-location: kernel\pep_device_platform_constraints.htm
old-project: kernel
ms.assetid: C9CC652F-16D4-4F88-BE8F-6CC7008F65DB
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_DEVICE_PLATFORM_CONSTRAINTS, PEP_DEVICE_PLATFORM_CONSTRAINTS, *PPEP_DEVICE_PLATFORM_CONSTRAINTS
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
req.alt-api: PEP_DEVICE_PLATFORM_CONSTRAINTS
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

# PEP_DEVICE_PLATFORM_CONSTRAINTS structure



## -description
<p>The <b>PEP_DEVICE_PLATFORM_CONSTRAINTS</b> structure specifies the constraints for entry to the various D<i>x</i> power states that are supported by a device.</p>


## -syntax

````
typedef struct _PEP_DEVICE_PLATFORM_CONSTRAINTS {
  PEPHANDLE           DeviceHandle;
  PDEVICE_POWER_STATE MinimumDStates;
  ULONG               PlatformStateCount;
} PEP_DEVICE_PLATFORM_CONSTRAINTS, *PPEP_DEVICE_PLATFORM_CONSTRAINTS;
````


## -struct-fields
<dl>

### -field <b>DeviceHandle</b>

<dd>
<p>[in] A PEPHANDLE value that identifies the device. The PEP supplied this handle in response to a previous <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification.</p>
</dd>

### -field <b>MinimumDStates</b>

<dd>
<p>[in] A pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a> enumeration values that indicate the lowest-powered D<i>x</i> (device power) state the device can enter for each platform idle state.</p>
</dd>

### -field <b>PlatformStateCount</b>

<dd>
<p>[in] The number of elements in the array pointed to by the <b>MinimumDStates</b> member. This member contains the platform state count that the PEP supplied in response to a previous <a href="kernel.pep_notify_ppm_query_platform_states">PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES</a> notification.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_dpm_device_idle_constraints">PEP_DPM_DEVICE_IDLE_CONSTRAINTS</a> notification. All three members of this structure contain input values that are supplied by the Windows power management framework (PoFx). In response to this notification, the PEP writes <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a> enumeration values to the elements of the array pointed to by the <b>MinimumDStates</b> member. PoFx allocates the storage for this array before sending the notification.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a>
</dt>
<dt>
<a href="kernel.pep_dpm_device_idle_constraints">PEP_DPM_DEVICE_IDLE_CONSTRAINTS</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_DEVICE_PLATFORM_CONSTRAINTS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
