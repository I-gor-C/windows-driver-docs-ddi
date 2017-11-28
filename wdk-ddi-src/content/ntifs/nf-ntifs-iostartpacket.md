---
UID: NF.ntifs.IoStartPacket
title: IoStartPacket
author: windows-driver-content
description: The IoStartPacket routine calls the driver's StartIo routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy.
old-location: kernel\iostartpacket.htm
old-project: kernel
ms.assetid: b1fa148e-73e2-437f-bd3a-e879bd457c76
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoStartPacket
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoStartPacket
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
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
---

# IoStartPacket function



## -description
<p>The <b>IoStartPacket</b> routine calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff563858">StartIo</a> routine with the given IRP or inserts the IRP into the device queue associated with the given device object if the device is already busy. </p>


## -syntax

````
VOID IoStartPacket(
  _In_     PDEVICE_OBJECT DeviceObject,
  _In_     PIRP           Irp,
  _In_opt_ PULONG         Key,
  _In_opt_ PDRIVER_CANCEL CancelFunction
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the target device object for the IRP.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the IRP to be processed.</p>
</dd>

### -param <i>Key</i> [in, optional]

<dd>
<p>Pointer to a value that determines where to insert the packet into the device queue. If this is zero, the packet is inserted at the tail of the device queue.</p>
</dd>

### -param <i>CancelFunction</i> [in, optional]

<dd>
<p>Specifies the entry point for a driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/hh406716">Cancel</a> routine.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If the driver is already busy processing a request for the target device object, then the packet is queued in the device queue. Otherwise, this routine calls the driver's <i>StartIo</i> routine with the specified IRP.</p>

<p>If a non-NULL <i>CancelFunction</i> pointer is supplied, it is set in the IRP so the driver's <i>Cancel</i> routine is called if the IRP is canceled before its completion.</p>

<p>Drivers that do not have a <i>StartIo</i> routine cannot call <b>IoStartPacket</b>.</p>

<p>Callers of <b>IoStartPacket</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Usually, this routine is called from a device driver's Dispatch routine at IRQL = PASSIVE_LEVEL.</p>

<p>If the driver is already busy processing a request for the target device object, then the packet is queued in the device queue. Otherwise, this routine calls the driver's <i>StartIo</i> routine with the specified IRP.</p>

<p>If a non-NULL <i>CancelFunction</i> pointer is supplied, it is set in the IRP so the driver's <i>Cancel</i> routine is called if the IRP is canceled before its completion.</p>

<p>Drivers that do not have a <i>StartIo</i> routine cannot call <b>IoStartPacket</b>.</p>

<p>Callers of <b>IoStartPacket</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Usually, this routine is called from a device driver's Dispatch routine at IRQL = PASSIVE_LEVEL.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549422">IoMarkIrpPending</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549674">IoSetCancelRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550358">IoStartNextPacket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550363">IoStartNextPacketByKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoStartPacket routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
