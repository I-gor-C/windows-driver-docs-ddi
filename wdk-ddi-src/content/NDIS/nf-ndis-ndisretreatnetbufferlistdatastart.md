---
UID: NF.ndis.NdisRetreatNetBufferListDataStart
title: NdisRetreatNetBufferListDataStart
author: windows-driver-content
description: Call the NdisRetreatNetBufferListDataStart function to increase the used data space in all the NET_BUFFER structures in a NET_BUFFER_LIST structure.
old-location: netvista\ndisretreatnetbufferlistdatastart.htm
ms.assetid: 76a1294f-d098-4751-9b59-923993379c6e
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRetreatNetBufferListDataStart
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
ms.keywords: NdisRetreatNetBufferListDataStart
req.iface: 
---

# NdisRetreatNetBufferListDataStart function



## -description
<p>Call the 
  <b>NdisRetreatNetBufferListDataStart</b> function to increase the 
  <i>used data space</i> in all the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures in a 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
NDIS_STATUS NdisRetreatNetBufferListDataStart(
  _In_     PNET_BUFFER_LIST                NetBufferList,
  _In_     ULONG                           DataOffsetDelta,
  _In_     ULONG                           DataBackFill,
  _In_opt_ NET_BUFFER_ALLOCATE_MDL_HANDLER AllocateMdlHandler,
  _In_opt_ NET_BUFFER_FREE_MDL_HANDLER     FreeMdlHandler
);
````


## -parameters
<dl>

### -param <i>NetBufferList</i> [in]

<dd>
<p>A pointer to a previously allocated NET_BUFFER_LIST structure.</p>
</dd>

### -param <i>DataOffsetDelta</i> [in]

<dd>
<p>The amount of additional 
     <i>used data space</i> in each NET_BUFFER structure. If there is not enough 
     <i>unused data space</i> to satisfy the request, NDIS allocates more memory.</p>
</dd>

### -param <i>DataBackFill</i> [in]

<dd>
<p>If NDIS must allocate memory, this parameter specifies the amount of data space in addition to the
     value of the 
     <i>DataOffsetDelta</i> parameter to allocate.</p>
</dd>

### -param <i>AllocateMdlHandler</i> [in, optional]

<dd>
<p>An optional entry point for an 
     <a href="https://msdn.microsoft.com/14247f48-7ef8-481c-aa1e-e657475812fa">NetAllocateMdl</a> function. If the caller
     specifies an entry point for the 
     <i>NetAllocateMdl</i> function, NDIS calls 
     <i>NetAllocateMdl</i> to allocate an MDL and memory.</p>
</dd>

### -param <i>FreeMdlHandler</i> [in, optional]

<dd>
<p>An optional entry point for an 
     <a href="https://msdn.microsoft.com/a92b2de9-231d-4dcc-8220-857063a35eb1">NetFreeMdl</a> function. If the caller
     specifies an entry point for the 
     <i>NetFreeMdl</i> function, NDIS calls 
     <i>NetFreeMdl</i> to free an MDL and memory.</p>
</dd>
</dl>

## -returns
<p><b>NdisRetreatNetBufferListDataStart</b> returns one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><b>NdisRetreatNetBufferListDataStart</b> successfully allocated the data space on all the NET_BUFFER
       structures either by reducing the value of the 
       <b>DataOffset</b> member or by allocating new storage.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p><b>NdisRetreatNetBufferListDataStart</b> failed due to insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p><b>NdisRetreatNetBufferListDataStart</b> failed for reasons other than insufficient resources.</p>

<p> </p>

## -remarks
<p>Calling 
    <b>NdisRetreatNetBufferListDataStart</b> is the equivalent of calling the 
    <a href="https://msdn.microsoft.com/4b58a1dc-8a5a-464b-a2a2-deb952febe25">
    NdisRetreatNetBufferDataStart</a> function for every 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure on the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. 
    <b>NdisRetreatNetBufferListDataStart</b> attempts to satisfy the request by reducing the value of the 
    <b>DataOffset</b> member in every NET_BUFFER structure. If there is not enough 
    <i>unused data space</i> available, this function allocates a new buffer and MDL, and then chains the new
    MDL to the beginning of the MDL chain on the NET_BUFFER structure.</p>

<p>Call the 
    <a href="https://msdn.microsoft.com/819ac05b-15c2-4a24-ae6b-8a47991a4e7a">
    NdisAdvanceNetBufferListDataStart</a> function to release data space that was claimed in a previous 
    <b>NdisRetreatNetBufferListDataStart</b> call. Alternatively, the driver can call the 
    <a href="https://msdn.microsoft.com/49b69282-137d-4bb5-92f5-4d27cedbb6d4">
    NdisAdvanceNetBufferDataStart</a> function for each NET_BUFFER structure on the NET_BUFFER_LIST
    structure. Calling 
    <b>NdisAdvanceNetBufferListDataStart</b> is more efficient.</p>

<p>Calling 
    <b>NdisRetreatNetBufferListDataStart</b> is the equivalent of calling the 
    <a href="https://msdn.microsoft.com/4b58a1dc-8a5a-464b-a2a2-deb952febe25">
    NdisRetreatNetBufferDataStart</a> function for every 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure on the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. 
    <b>NdisRetreatNetBufferListDataStart</b> attempts to satisfy the request by reducing the value of the 
    <b>DataOffset</b> member in every NET_BUFFER structure. If there is not enough 
    <i>unused data space</i> available, this function allocates a new buffer and MDL, and then chains the new
    MDL to the beginning of the MDL chain on the NET_BUFFER structure.</p>

<p>Call the 
    <a href="https://msdn.microsoft.com/819ac05b-15c2-4a24-ae6b-8a47991a4e7a">
    NdisAdvanceNetBufferListDataStart</a> function to release data space that was claimed in a previous 
    <b>NdisRetreatNetBufferListDataStart</b> call. Alternatively, the driver can call the 
    <a href="https://msdn.microsoft.com/49b69282-137d-4bb5-92f5-4d27cedbb6d4">
    NdisAdvanceNetBufferDataStart</a> function for each NET_BUFFER structure on the NET_BUFFER_LIST
    structure. Calling 
    <b>NdisAdvanceNetBufferListDataStart</b> is more efficient.</p>

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
<a href="https://msdn.microsoft.com/14247f48-7ef8-481c-aa1e-e657475812fa">NetAllocateMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a92b2de9-231d-4dcc-8220-857063a35eb1">NetFreeMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/49b69282-137d-4bb5-92f5-4d27cedbb6d4">
   NdisAdvanceNetBufferDataStart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/819ac05b-15c2-4a24-ae6b-8a47991a4e7a">
   NdisAdvanceNetBufferListDataStart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4b58a1dc-8a5a-464b-a2a2-deb952febe25">
   NdisRetreatNetBufferDataStart</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisRetreatNetBufferListDataStart function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
