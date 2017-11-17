---
UID: NF.ndis.NdisMRegisterIoPortRange
title: NdisMRegisterIoPortRange
author: windows-driver-content
description: NdisMRegisterIoPortRange sets up driver access to device I/O ports with the NdisRawReadPortXxx and NdisRawWritePortXxx functions and claims the range of I/O port addresses in the registry for that driver's NIC.
old-location: netvista\ndismregisterioportrange.htm
ms.assetid: 3e7fc02b-9562-44b9-8659-793a1d96d1e9
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMRegisterIoPortRange (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMRegisterIoPortRange (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMRegisterIoPortRange
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function, NdisMRegisterIoPortRange
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisMRegisterIoPortRange
req.iface: 
---

# NdisMRegisterIoPortRange function



## -description
<p><b>NdisMRegisterIoPortRange</b> sets up driver access to device I/O ports with the 
  <b>NdisRawReadPort<i>Xxx</i></b> and 
  <b>NdisRawWritePort<i>Xxx</i></b> functions and claims the range of I/O port addresses in the registry for that driver's
  NIC.</p>


## -syntax

````
NDIS_STATUS NdisMRegisterIoPortRange(
  _Out_ PVOID       *PortOffset,
  _In_  NDIS_HANDLE MiniportAdapterHandle,
  _In_  UINT        InitialPort,
  _In_  UINT        NumberOfPorts
);
````


## -parameters
<dl>

### -param <i>PortOffset</i> [out]

<dd>
<p>Specifies a caller-supplied variable in which this function returns the mapped base virtual
     address for the given bus-relative I/O port range specified by 
     <i>InitialPort</i> and 
     <i>NumberOfPorts</i> .</p>
</dd>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>Specifies the handle input to 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>InitialPort</i> [in]

<dd>
<p>Specifies the bus-relative base port address for a range of ports to be mapped.</p>
</dd>

### -param <i>NumberOfPorts</i> [in]

<dd>
<p>Specifies the number of ports in the range to be mapped.</p>
</dd>
</dl>

## -returns
<p><b>NdisMRegisterIoPortRange</b> can return one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The given range of I/O ports was mapped successfully so the value at 
       <i>PortOffset</i> is valid and the mapped range has been claimed in the registry for the NIC.</p><dl>
<dt><b>NDIS_STATUS_RESOURCE_CONFLICT</b></dt>
</dl><p>An attempt to claim the I/O port range in the registry has failed, possibly because another
       driver already claimed the range for its device. 
       <b>NdisMRegisterIoPortRange</b> logs an error if this occurs.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The port range could not be mapped or NDIS could not allocate resources to check the registry
       for hardware-resource conflicts.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>Either the bus type or bus number is out of range or the given 
       <i>InitialPort</i> and 
       <i>NumberOfPorts</i> were invalid (possibly not within the I/O port space of the current
       platform).</p>

<p> </p>

## -remarks
<p>A miniport driver calls 
    <b>NdisMRegisterIoPortRange</b> from its 
    <i>MiniportInitializeEx</i> function. 
    <i>MiniportInitializeEx</i> must call 
    <a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
    NdisMSetMiniportAttributes</a> before calling 
    <b>NdisMRegisterIoPortRange</b>.</p>

<p><b>NdisMRegisterIoPortRange</b> maps a bus-relative device address range that the miniport driver can use
    subsequently to access an I/O port range on a NIC by calling the 
    <b>NdisRaw<i>Xxx</i></b> functions. A successful call claims the specified range of I/O ports in the registry for the
    caller's NIC.</p>

<p>Because the parameters passed to the 
    <b>NdisRaw<i>Xxx</i></b> have been mapped, these functions run significantly faster than the corresponding 
    <b>NdisImmediate..Port<i>Xxx</i></b>. After a successful call to 
    <b>NdisMRegisterIoPortRange</b>, a miniport driver cannot call any of the 
    <b>NdisImmediate..Port<i>Xxx</i></b> functions with either bus-relative addresses or mapped virtual addresses within such an I/O
    port range.</p>

<p>If its call to 
    <b>NdisMRegisterIoPortRange</b> fails, 
    <i>MiniportInitializeEx</i> should release all resources it already allocated for a NIC and, then, fail
    initialization for that NIC.</p>

<p>Drivers of NICs with device registers in the host memory space call 
    <b>NdisMMapIoSpace</b> and, subsequently, the 
    <b>NdisRead/WriteRegister<i>Xxx</i></b> functions to access the NIC registers.</p>

<p>A miniport driver calls 
    <b>NdisMRegisterIoPortRange</b> from its 
    <i>MiniportInitializeEx</i> function. 
    <i>MiniportInitializeEx</i> must call 
    <a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
    NdisMSetMiniportAttributes</a> before calling 
    <b>NdisMRegisterIoPortRange</b>.</p>

<p><b>NdisMRegisterIoPortRange</b> maps a bus-relative device address range that the miniport driver can use
    subsequently to access an I/O port range on a NIC by calling the 
    <b>NdisRaw<i>Xxx</i></b> functions. A successful call claims the specified range of I/O ports in the registry for the
    caller's NIC.</p>

<p>Because the parameters passed to the 
    <b>NdisRaw<i>Xxx</i></b> have been mapped, these functions run significantly faster than the corresponding 
    <b>NdisImmediate..Port<i>Xxx</i></b>. After a successful call to 
    <b>NdisMRegisterIoPortRange</b>, a miniport driver cannot call any of the 
    <b>NdisImmediate..Port<i>Xxx</i></b> functions with either bus-relative addresses or mapped virtual addresses within such an I/O
    port range.</p>

<p>If its call to 
    <b>NdisMRegisterIoPortRange</b> fails, 
    <i>MiniportInitializeEx</i> should release all resources it already allocated for a NIC and, then, fail
    initialization for that NIC.</p>

<p>Drivers of NICs with device registers in the host memory space call 
    <b>NdisMMapIoSpace</b> and, subsequently, the 
    <b>NdisRead/WriteRegister<i>Xxx</i></b> functions to access the NIC registers.</p>

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
   <a href="https://msdn.microsoft.com/5b57d289-0438-410c-81a5-9a8940988b5f">NdisMRegisterIoPortRange (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMRegisterIoPortRange (NDIS
   5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563577">NdisMDeregisterIoPortRange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563782">NdisRawReadPortBufferUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563785">NdisRawReadPortBufferUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563791">NdisRawReadPortBufferUshort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563794">NdisRawReadPortUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563801">NdisRawReadPortUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563808">NdisRawReadPortUshort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563811">NdisRawWritePortBufferUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563816">NdisRawWritePortBufferUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563824">NdisRawWritePortBufferUshort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563829">NdisRawWritePortUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563832">NdisRawWritePortUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564510">NdisRawWritePortUshort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564513">NdisReadRegisterUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564514">NdisReadRegisterUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564515">NdisReadRegisterUshort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564678">NdisWriteRegisterUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564683">NdisWriteRegisterUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564685">NdisWriteRegisterUshort</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMRegisterIoPortRange function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
