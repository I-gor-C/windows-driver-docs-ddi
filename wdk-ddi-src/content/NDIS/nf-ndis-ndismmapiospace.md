---
UID: NF.ndis.NdisMMapIoSpace
title: NdisMMapIoSpace
author: windows-driver-content
description: NdisMMapIoSpace maps a given bus-relative &#0034;physical&#0034; range of device RAM or registers onto a system-space virtual range.
old-location: netvista\ndismmapiospace.htm
ms.assetid: 16c62146-ed8d-4bf7-9d5e-0c5dbbf3c9c4
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMMapIoSpace (NDIS 5.1)) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMMapIoSpace (NDIS 5.1)) in
   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMMapIoSpace
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function, NdisMMapIoSpace
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisMMapIoSpace
req.iface: 
---

# NdisMMapIoSpace function



## -description
<p><b>NdisMMapIoSpace</b> maps a given bus-relative "physical" range of device RAM or registers onto a
  system-space virtual range.</p>


## -syntax

````
NDIS_STATUS NdisMMapIoSpace(
  _Out_ PVOID                 *VirtualAddress,
  _In_  NDIS_HANDLE           MiniportAdapterHandle,
  _In_  NDIS_PHYSICAL_ADDRESS PhysicalAddress,
  _In_  UINT                  Length
);
````


## -parameters
<dl>

### -param <i>VirtualAddress</i> [out]

<dd>
<p>Pointer to a caller-supplied variable that is set to the converted virtual address if the call is
     successful.</p>
</dd>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>Specifies the handle input to 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>PhysicalAddress</i> [in]

<dd>
<p>Specifies the bus-relative base physical address of the device memory range to be mapped.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the number of bytes to be mapped.</p>
</dd>
</dl>

## -returns
<p><b>NdisMMapIoSpace</b> can return any of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The device memory range was mapped successfully so the value at 
       <i>VirtualAddress</i> is valid and the mapped range has been claimed in the registry for the
       NIC.</p><dl>
<dt><b>NDIS_STATUS_RESOURCE_CONFLICT</b></dt>
</dl><p>An attempt to claim the device memory range in the registry has failed, possibly because another
       driver has already claimed the range for its device. 
       <b>NdisMMapIoSpace</b> logs an error if this occurs.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The memory could not be mapped or sufficient virtual memory could not be allocated.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>Either the bus type or bus number is out of range or the given 
       <i>PhysicalAddress</i> and 
       <i>Length</i> were invalid (possibly not within the I/O space of the current platform).</p>

<p> </p>

## -remarks
<p>This function is called by drivers of NICs that have on-board memory or a bank of device registers
    appearing in the I/O space of the host. For example, the driver of a NIC that uses PIO calls 
    <b>NdisMMapIoSpace</b>.</p>

<p>A successful call to 
    <b>NdisMMapIoSpace</b> claims hardware resources in the registry for the driver's NIC. Consequently, only 
    <i>MiniportInitializeEx</i> functions call 
    <b>NdisMMapIoSpace</b>.</p>

<p><b>NdisMMapIoSpace</b> sets the variable at 
    <i>VirtualAddress</i> to <b>NULL</b> if it does not return NDIS_STATUS_SUCCESS.</p>

<p>MiniportInitializeEx either gets the 
    <i>PhysicalAddress</i> value from the driver's 
    <b>Parameters</b> registry key or by calling a bus-type-specific 
    <b>Ndis<i>Xxx</i></b> configuration function. The given physical address range must fall within the I/O space of the
    current platform. It is a programming error to call 
    <b>NdisMMapIoSpace</b> with a host physical memory address.</p>

<p>This function is called by drivers of NICs that have on-board memory or a bank of device registers
    appearing in the I/O space of the host. For example, the driver of a NIC that uses PIO calls 
    <b>NdisMMapIoSpace</b>.</p>

<p>A successful call to 
    <b>NdisMMapIoSpace</b> claims hardware resources in the registry for the driver's NIC. Consequently, only 
    <i>MiniportInitializeEx</i> functions call 
    <b>NdisMMapIoSpace</b>.</p>

<p><b>NdisMMapIoSpace</b> sets the variable at 
    <i>VirtualAddress</i> to <b>NULL</b> if it does not return NDIS_STATUS_SUCCESS.</p>

<p>MiniportInitializeEx either gets the 
    <i>PhysicalAddress</i> value from the driver's 
    <b>Parameters</b> registry key or by calling a bus-type-specific 
    <b>Ndis<i>Xxx</i></b> configuration function. The given physical address range must fall within the I/O space of the
    current platform. It is a programming error to call 
    <b>NdisMMapIoSpace</b> with a host physical memory address.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff553549">NdisMMapIoSpace (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMMapIoSpace (NDIS 5.1)</b>) in
   Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563591">NdisMGetBusData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563691">NdisMUnmapIoSpace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975122">NdisOpenConfigurationEx</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMMapIoSpace function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
