---
UID: NF.portcls.PcUnregisterAdapterPowerManagement
title: PcUnregisterAdapterPowerManagement
author: windows-driver-content
description: The PcUnregisterAdapterPowerManagement function unregisters the audio adapter's power management interface from the PortCls class driver. The PcUnregisterAdapterPowerManagement function is available in Windows 7 and later versions of Windows.
old-location: audio\pcunregisteradapterpowermanagement.htm
old-project: audio
ms.assetid: a25ee83f-e267-4966-9be2-ddcbc44b5c15
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcUnregisterAdapterPowerManagement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcUnregisterAdapterPowerManagement
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL.
req.iface: 
---

# PcUnregisterAdapterPowerManagement function



## -description
<p>The <b>PcUnregisterAdapterPowerManagement</b> function unregisters the audio adapter's power management interface from the PortCls class driver. The <b>PcUnregisterAdapterPowerManagement</b> function is available in Windows 7 and later versions of Windows.</p>


## -syntax

````
PORTCLASSAPI NTSTATUS NTAPI PcUnregisterAdapterPowerManagement(
  _In_ PDEVICE_OBJECT pDeviceObject
);
````


## -parameters
<dl>

### -param <i>pDeviceObject</i> [in]

<dd>
<p>Specifies a pointer to a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure that represents the functional device object of the adapter.</p>
</dd>
</dl>

## -returns
<p>The <b>PcUnregisterAdapterPowerManagement</b> function returns STATUS_SUCCESS if the function call was successful. Otherwise, it returns the appropriate error code.</p>

## -remarks
<p>The <b>PcUnregisterAdapterPowerManagement</b> function unregisters a driver's power management interface that was registered with PortCls by using the <a href="..\portcls\nf-portcls-pcregisteradapterpowermanagement.md">PcRegisterAdapterPowerManagement</a> function. <b>PcUnregisterAdapterPowerManagement</b> helps the system to avoid making a power change request while the adapter driver is being unloaded. This function must only be called if the power management interface for the adapter was previously registered with PortCls.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\portcls\nf-portcls-pcregisteradapterpowermanagement.md">PcRegisterAdapterPowerManagement</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcUnregisterAdapterPowerManagement function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
