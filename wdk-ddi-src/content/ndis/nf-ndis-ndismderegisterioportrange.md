---
UID: NF.ndis.NdisMDeregisterIoPortRange
title: NdisMDeregisterIoPortRange
author: windows-driver-content
description: NdisMDeregisterIoPortRange releases a mapping that was set up with NdisMRegisterIoPortRange during driver initialization.
old-location: netvista\ndismderegisterioportrange.htm
old-project: netvista
ms.assetid: b5b6a608-af1f-4030-b83a-a6f64ff3a264
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMDeregisterIoPortRange
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMDeregisterIoPortRange
   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMDeregisterIoPortRange
   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMDeregisterIoPortRange
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisMDeregisterIoPortRange function



## -description
<p><b>NdisMDeregisterIoPortRange</b> releases a mapping that was set up with 
  <a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a> during
  driver initialization.</p>


## -syntax

````
VOID NdisMDeregisterIoPortRange(
  _In_ NDIS_HANDLE MiniportAdapterHandle,
  _In_ UINT        InitialPort,
  _In_ UINT        NumberOfPorts,
  _In_ PVOID       PortOffset
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>Specifies the handle input to 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>InitialPort</i> [in]

<dd>
<p>Specifies the bus-relative address of the first port in the range of ports.</p>
</dd>

### -param <i>NumberOfPorts</i> [in]

<dd>
<p>Specifies the number of ports in the range.</p>
</dd>

### -param <i>PortOffset</i> [in]

<dd>
<p>Specifies the mapped base port address returned by 
     <b>NdisMRegisterIoPortRange</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The miniport driver must pass the same 
    <i>InitialPort</i> and 
    <i>NumberOfPorts</i> to 
    <b>NdisMDeregisterIoPortRange</b> that were passed when 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a> to get
    the mapped 
    <i>PortOffset</i> value. That is, a miniport driver cannot call 
    <b>NdisMDeregisterIoPortRange</b> to release a subrange of a mapped port range.</p>

<p><b>NdisMDeregisterIoPortRange</b> can be called from the 
    <i>MiniportInitializeEx</i> or 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> functions only if 
    <i>MiniportInitializeEx</i> previously made a successful call to 
    <b>NdisMRegisterIoPortRange</b>.</p>

<p><b>NdisMDeregisterIoPortRange</b> also releases the driver's claim on the I/O port range in the
    registry.</p>

<p>After it calls 
    <b>NdisMRegisterIoPortRange</b>, the miniport driver can no longer access the NIC's port range with calls
    to the 
    <b>NdisRaw..Port<i>Xxx</i></b> functions.</p>

<p>The miniport driver must pass the same 
    <i>InitialPort</i> and 
    <i>NumberOfPorts</i> to 
    <b>NdisMDeregisterIoPortRange</b> that were passed when 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a> to get
    the mapped 
    <i>PortOffset</i> value. That is, a miniport driver cannot call 
    <b>NdisMDeregisterIoPortRange</b> to release a subrange of a mapped port range.</p>

<p><b>NdisMDeregisterIoPortRange</b> can be called from the 
    <i>MiniportInitializeEx</i> or 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> functions only if 
    <i>MiniportInitializeEx</i> previously made a successful call to 
    <b>NdisMRegisterIoPortRange</b>.</p>

<p><b>NdisMDeregisterIoPortRange</b> also releases the driver's claim on the I/O port range in the
    registry.</p>

<p>After it calls 
    <b>NdisMRegisterIoPortRange</b>, the miniport driver can no longer access the NIC's port range with calls
    to the 
    <b>NdisRaw..Port<i>Xxx</i></b> functions.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/d2903c80-8a6b-4050-9630-5ebd52a0fbb5">NdisMDeregisterIoPortRange
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMDeregisterIoPortRange
   (NDIS 5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMDeregisterIoPortRange function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
