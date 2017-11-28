---
UID: NF.wdm.IoDisconnectInterrupt
title: IoDisconnectInterrupt
author: windows-driver-content
description: The IoDisconnectInterrupt routine releases a device driver's set of interrupt object(s) when the device is paused or removed, or when the driver is being unloaded.
old-location: kernel\iodisconnectinterrupt.htm
old-project: kernel
ms.assetid: 06130ec3-7031-4c40-932a-7342c26b7e15
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoDisconnectInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoDisconnectInterrupt
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive4, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoDisconnectInterrupt function



## -description
<p>The <b>IoDisconnectInterrupt</b> routine releases a device driver's set of interrupt object(s) when the device is paused or removed, or when the driver is being unloaded.</p>


## -syntax

````
VOID IoDisconnectInterrupt(
  _In_ PKINTERRUPT InterruptObject
);
````


## -parameters
<dl>

### -param <i>InterruptObject</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554237">KINTERRUPT</a> structure. The caller obtained this pointer from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a> call that previously connected the interrupt or interrupts.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The driver should configure the device to issue interrupts only when these interrupts are connected. Failure to prevent a device from issuing interrupts when the interrupts are disconnected might cause system instability. For example, if a device shares a level-triggered interrupt line with other devices, and the device issues an interrupt request when the device's interrupts are disconnected, the other devices on the line will not acknowledge the interrupt and the interrupt will continue to fire. Before calling <b>IoDisconnectInterrupt</b>, the driver should configure the device to stop issuing interrupts. After calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, the driver should configure the device to start issuing interrupts.</p>

<p>If the driver stored the pointer to its interrupt object(s) in the device extension of its device object or in the controller extension of its controller object, it must call <b>IoDisconnectInterrupt</b> before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549083">IoDeleteDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549078">IoDeleteController</a>. </p>

<p>The driver should configure the device to issue interrupts only when these interrupts are connected. Failure to prevent a device from issuing interrupts when the interrupts are disconnected might cause system instability. For example, if a device shares a level-triggered interrupt line with other devices, and the device issues an interrupt request when the device's interrupts are disconnected, the other devices on the line will not acknowledge the interrupt and the interrupt will continue to fire. Before calling <b>IoDisconnectInterrupt</b>, the driver should configure the device to stop issuing interrupts. After calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>, the driver should configure the device to start issuing interrupts.</p>

<p>If the driver stored the pointer to its interrupt object(s) in the device extension of its device object or in the controller extension of its controller object, it must call <b>IoDisconnectInterrupt</b> before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549083">IoDeleteDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549078">IoDeleteController</a>. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547787">IrqlIoPassive4</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548371">IoConnectInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549078">IoDeleteController</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549083">IoDeleteDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554237">KINTERRUPT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoDisconnectInterrupt routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
