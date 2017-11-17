---
UID: NF.portcls.PcUnregisterIoTimeout
title: PcUnregisterIoTimeout
author: windows-driver-content
description: The PcUnregisterIoTimeout function unregisters a driver-supplied I/O-timer callback routine for a specified device object.
old-location: audio\pcunregisteriotimeout.htm
ms.assetid: 4266c775-a2e9-46f0-91ad-6f6cce06bea0
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcUnregisterIoTimeout function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcUnregisterIoTimeout
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
req.irql: PASSIVE_LEVEL
ms.keywords: PcUnregisterIoTimeout
req.iface: 
---

# PcUnregisterIoTimeout function



## -description
<p>The <b>PcUnregisterIoTimeout</b> function unregisters a driver-supplied I/O-timer callback routine for a specified device object.</p>


## -syntax

````
NTSTATUS PcUnregisterIoTimeout(
  _In_ PDEVICE_OBJECT    pDeviceObject,
  _In_ PIO_TIMER_ROUTINE pTimerRoutine,
  _In_ PVOID             pContext
);
````


## -parameters
<dl>

### -param <i>pDeviceObject</i> [in]

<dd>
<p>Pointer to the same device object that the driver supplied when it previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff537725">PcRegisterIoTimeout</a>. The device object is a system structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>.</p>
</dd>

### -param <i>pTimerRoutine</i> [in]

<dd>
<p>Pointer to the same I/O-timer callback routine that the driver supplied when it previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff537725">PcRegisterIoTimeout</a>
</p>
</dd>

### -param <i>pContext</i> [in]

<dd>
<p>Pointer to the same driver-determined context that the driver supplied when it previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff537725">PcRegisterIoTimeout</a>
</p>
</dd>
</dl>

## -returns
<p><b>PcUnregisterIoTimeout</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code. The following table shows some of the possible error codes.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>Indicates that no timer callback with the same device object, callback routine, and context is currently registered.</p>

<p> </p>

## -remarks
<p>This call succeeds only if a time-out callback with the same device object, timer routine, and context was previously registered with a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537725">PcRegisterIoTimeout</a> function.</p>

<p>This call succeeds only if a time-out callback with the same device object, timer routine, and context was previously registered with a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537725">PcRegisterIoTimeout</a> function.</p>

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
<p>The PortCls system driver implements the PcUnregisterIoTimeout function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537725">PcRegisterIoTimeout</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcUnregisterIoTimeout function%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
