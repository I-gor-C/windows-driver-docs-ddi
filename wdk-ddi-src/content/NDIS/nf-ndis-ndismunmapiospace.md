---
UID: NF.ndis.NdisMUnmapIoSpace
title: NdisMUnmapIoSpace
author: windows-driver-content
description: NdisMUnmapIoSpace releases a virtual range mapped by an initialization-time call to NdisMMapIoSpace.
old-location: netvista\ndismunmapiospace.htm
ms.assetid: 068232d3-b160-4090-b72c-63d9a31c1567
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMUnmapIoSpace (NDIS 5.1)) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMUnmapIoSpace (NDIS 5.1)) in
   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMUnmapIoSpace
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
ms.keywords: NdisMUnmapIoSpace
req.iface: 
---

# NdisMUnmapIoSpace function



## -description
<p><b>NdisMUnmapIoSpace</b> releases a virtual range mapped by an initialization-time call to 
  <a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a>.</p>


## -syntax

````
VOID NdisMUnmapIoSpace(
  _In_ NDIS_HANDLE MiniportAdapterHandle,
  _In_ PVOID       VirtualAddress,
  _In_ UINT        Length
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>Specifies the handle originally input to 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>VirtualAddress</i> [in]

<dd>
<p>Specifies the base virtual address for the mapped range that was returned by 
     <b>NdisMMapIoSpace</b>.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the number of bytes in the range that was mapped with 
     <b>NdisMMapIoSpace</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When a miniport driver is unloading, any memory range that it mapped during initialization with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a> must be released with a
    call to 
    <b>NdisMUnmapIoSpace</b>.</p>

<p>The 
    <i>Length</i> passed to 
    <b>NdisMUnmapIoSpace</b> must match the 
    <i>Length</i> originally passed to 
    <b>NdisMMapIoSpace</b>.</p>

<p><b>NdisMUnmapIoSpace</b> can be called only from a miniport driver's 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> and 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> functions.</p>

<p>When a miniport driver is unloading, any memory range that it mapped during initialization with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a> must be released with a
    call to 
    <b>NdisMUnmapIoSpace</b>.</p>

<p>The 
    <i>Length</i> passed to 
    <b>NdisMUnmapIoSpace</b> must match the 
    <i>Length</i> originally passed to 
    <b>NdisMMapIoSpace</b>.</p>

<p><b>NdisMUnmapIoSpace</b> can be called only from a miniport driver's 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> and 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> functions.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff553661">NdisMUnmapIoSpace (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMUnmapIoSpace (NDIS 5.1)</b>) in
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMUnmapIoSpace function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
