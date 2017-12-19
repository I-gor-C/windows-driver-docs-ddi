---
UID: NF.ks.KsTerminateDevice
title: KsTerminateDevice function
author: windows-driver-content
description: The KsTerminateDevice function removes an AVStream device.
old-location: stream\ksterminatedevice.htm
old-project: stream
ms.assetid: 3d6ad381-0bd9-47d8-a4dd-e434b62bf5a1
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KsTerminateDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsTerminateDevice
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# KsTerminateDevice function



## -description
The<b> KsTerminateDevice </b>function removes an AVStream device.



## -syntax

````
void KsTerminateDevice(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters

### -param DeviceObject [in]

A pointer to a <a href="kernel.device_object">DEVICE_OBJECT</a> structure corresponding to the device for which to remove AVStream support.


## -returns
None


## -remarks
Normally, AVStream calls <b>KsTerminateDevice</b> upon receipt of a PnP remove device IRP (IRP_MN_REMOVE_DEVICE). Most minidrivers do not call this function directly; however, it can be used to remove AVStream support for the device given in <i>DeviceObject</i>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksinitializedriver">KsInitializeDriver</a>
</dt>
<dt>
<a href="stream.ksinitializedevice">KsInitializeDevice</a>
</dt>
<dt>
<a href="stream.ksadddevice">KsAddDevice</a>
</dt>
<dt>
<a href="stream.kscreatedevice">KsCreateDevice</a>
</dt>
<dt>
<a href="stream.ksdevice">KSDEVICE</a>
</dt>
<dt>
<a href="kernel.driver_object">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="kernel.device_object">DEVICE_OBJECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsTerminateDevice function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

