---
UID: NF.ntifs.IoGetAttachedDevice
title: IoGetAttachedDevice
author: windows-driver-content
description: The IoGetAttachedDevice routine returns a pointer to the highest-level device object associated with the specified device.
old-location: ifsk\iogetattacheddevice.htm
old-project: ifsk
ms.assetid: 18083431-37b5-49e9-9c69-8b6cd7b5f736
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IoGetAttachedDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetAttachedDevice
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# IoGetAttachedDevice function



## -description
<p>The <b>IoGetAttachedDevice</b> routine returns a pointer to the highest-level device object associated with the specified device.</p>


## -syntax

````
PDEVICE_OBJECT IoGetAttachedDevice(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to the device object for which the topmost attached device is to be returned.</p>
</dd>
</dl>

## -returns
<p><b>IoGetAttachedDevice</b> returns the highest-level device attached to the specified device. </p>

## -remarks
<p>If the device object specified by <i>DeviceObject</i> has no other device objects attached to it, <i>DeviceObject</i> and the returned pointer are equal.</p>

<p><b>IoGetAttachedDevice</b> differs from <a href="https://msdn.microsoft.com/library/windows/hardware/ff549145">IoGetAttachedDeviceReference</a> in the following respects:</p>

<p><b>IoGetAttachedDevice</b> does not increment the reference count on the device object. (Thus no matching call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> is required.)</p>

<p>Callers of <b>IoGetAttachedDevice</b> must ensure that no device objects are added to or removed from the stack while <b>IoGetAttachedDevice</b> is executing. Callers that cannot do this must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549145">IoGetAttachedDeviceReference</a> instead.</p>

<p>If the device object specified by <i>DeviceObject</i> has no other device objects attached to it, <i>DeviceObject</i> and the returned pointer are equal.</p>

<p><b>IoGetAttachedDevice</b> differs from <a href="https://msdn.microsoft.com/library/windows/hardware/ff549145">IoGetAttachedDeviceReference</a> in the following respects:</p>

<p><b>IoGetAttachedDevice</b> does not increment the reference count on the device object. (Thus no matching call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> is required.)</p>

<p>Callers of <b>IoGetAttachedDevice</b> must ensure that no device objects are added to or removed from the stack while <b>IoGetAttachedDevice</b> is executing. Callers that cannot do this must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549145">IoGetAttachedDeviceReference</a> instead.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549145">IoGetAttachedDeviceReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoGetAttachedDevice routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
