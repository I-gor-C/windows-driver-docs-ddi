---
UID: NF.ndis.NdisAdvanceNetBufferListDataStart
title: NdisAdvanceNetBufferListDataStart
author: windows-driver-content
description: Call the NdisAdvanceNetBufferListDataStart function to release data space that was claimed in previous calls to the NdisRetreatNetBufferListDataStart function.
old-location: netvista\ndisadvancenetbufferlistdatastart.htm
old-project: netvista
ms.assetid: 819ac05b-15c2-4a24-ae6b-8a47991a4e7a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisAdvanceNetBufferListDataStart
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisAdvanceNetBufferListDataStart
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_NetBuffer_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisAdvanceNetBufferListDataStart function



## -description
<p>Call the 
  <b>NdisAdvanceNetBufferListDataStart</b> function to release data space that was claimed in previous calls
  to the 
  <a href="..\ndis\nf-ndis-ndisretreatnetbufferlistdatastart.md">
  NdisRetreatNetBufferListDataStart</a> function.</p>


## -syntax

````
VOID NdisAdvanceNetBufferListDataStart(
  _In_     PNET_BUFFER_LIST            NetBufferList,
  _In_     ULONG                       DataOffsetDelta,
  _In_     BOOLEAN                     FreeMdl,
  _In_opt_ NET_BUFFER_FREE_MDL_HANDLER FreeMdlHandler
);
````


## -parameters
<dl>

### -param <i>NetBufferList</i> [in]

<dd>
<p>A pointer to a previously allocated 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>
</dd>

### -param <i>DataOffsetDelta</i> [in]

<dd>
<p>The amount of 
     <i>used data space</i> to release.</p>
</dd>

### -param <i>FreeMdl</i> [in]

<dd>
<p>If <b>TRUE</b> and NDIS allocated memory to satisfy the corresponding 
     <b>NdisRetreatNetBufferListDataStart</b> call, this function frees the memory that was allocated and the
     associated MDL.</p>
</dd>

### -param <i>FreeMdlHandler</i> [in, optional]

<dd>
<p>An optional entry point for an 
     <a href="..\ndis\nc-ndis-net-buffer-free-mdl-handler.md">NetFreeMdl</a> function. If the caller
     specifies an entry point for the 
     <i>NetFreeMdl</i> function, NDIS calls 
     <i>NetFreeMdl</i> to free an MDL and memory.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisAdvanceNetBufferListDataStart</b> releases 
    <i>used data space</i> for all the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures in a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. If 
    <i>FreeMdl</i> is <b>TRUE</b> and 
    <a href="..\ndis\nf-ndis-ndisretreatnetbufferlistdatastart.md">
    NdisRetreatNetBufferListDataStart</a> allocated memory to satisfy the corresponding allocation request,
    
    <b>NdisAdvanceNetBufferListDataStart</b> frees the allocated memory. Calling this function is equivalent
    to calling 
    <a href="..\ndis\nf-ndis-ndisadvancenetbufferdatastart.md">
    NdisAdvanceNetBufferDataStart</a> for every NET_BUFFER structure on the NET_BUFFER_LIST structure.
    However, calling 
    <b>NdisAdvanceNetBufferListDataStart</b> is more efficient.</p>

<p>When protocol drivers call 
    <b>NdisAdvanceNetBufferListDataStart</b> on the receive path to access the various transport headers, the
    MDL chain should not be modified and 
    <i>FreeMdl</i> is <b>FALSE</b>.</p>

<p><b>NdisAdvanceNetBufferListDataStart</b> releases 
    <i>used data space</i> for all the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures in a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. If 
    <i>FreeMdl</i> is <b>TRUE</b> and 
    <a href="..\ndis\nf-ndis-ndisretreatnetbufferlistdatastart.md">
    NdisRetreatNetBufferListDataStart</a> allocated memory to satisfy the corresponding allocation request,
    
    <b>NdisAdvanceNetBufferListDataStart</b> frees the allocated memory. Calling this function is equivalent
    to calling 
    <a href="..\ndis\nf-ndis-ndisadvancenetbufferdatastart.md">
    NdisAdvanceNetBufferDataStart</a> for every NET_BUFFER structure on the NET_BUFFER_LIST structure.
    However, calling 
    <b>NdisAdvanceNetBufferListDataStart</b> is more efficient.</p>

<p>When protocol drivers call 
    <b>NdisAdvanceNetBufferListDataStart</b> on the receive path to access the various transport headers, the
    MDL chain should not be modified and 
    <i>FreeMdl</i> is <b>FALSE</b>.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547985">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-net-buffer-allocate-mdl-handler.md">NetAllocateMdl</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-net-buffer-free-mdl-handler.md">NetFreeMdl</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisadvancenetbufferdatastart.md">
   NdisAdvanceNetBufferDataStart</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisretreatnetbufferlistdatastart.md">
   NdisRetreatNetBufferListDataStart</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAdvanceNetBufferListDataStart function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
