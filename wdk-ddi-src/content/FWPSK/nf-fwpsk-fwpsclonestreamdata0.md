---
UID: NF.fwpsk.FwpsCloneStreamData0
title: FwpsCloneStreamData0
author: windows-driver-content
description: The FwpsCloneStreamData0 function allocates a clone of an existing FWPS_STREAM_DATA0 data stream.Note  FwpsCloneStreamData0 is a specific version of FwpsCloneStreamData.
old-location: netvista\fwpsclonestreamdata0.htm
ms.assetid: 66041ccb-e63a-4843-85ec-d93b924bb335
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsCloneStreamData0
req.alt-loc: Fwpkclnt.lib,Fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpsCloneStreamData0
req.iface: 
---

# FwpsCloneStreamData0 function



## -description
<p>The 
  <b>FwpsCloneStreamData0</b> function allocates a clone of an existing 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a> data stream.</p>


## -syntax

````
NTSTATUS NTAPI FwpsCloneStreamData0(
  _Inout_  FWPS_STREAM_DATA0 *calloutStreamData,
  _In_opt_ NDIS_HANDLE       netBufferListPoolHandle,
  _In_opt_ NDIS_HANDLE       netBufferPoolHandle,
  _In_     ULONG             allocateCloneFlags,
  _Out_    NET_BUFFER_LIST   **netBufferListChain
);
````


## -parameters
<dl>

### -param <i>calloutStreamData</i> [in, out]

<dd>
<p>A pointer to the original 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a> structure that is to
     have its 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure cloned.</p>
</dd>

### -param <i>netBufferListPoolHandle</i> [in, optional]

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> pool handle that was
     obtained from a previous call to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561611">NdisAllocateNetBufferListPool</a> function. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>netBufferPoolHandle</i> [in, optional]

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> pool handle that was obtained from a
     previous call to the 
     <a href="https://msdn.microsoft.com/bc27758a-a793-48a1-a6ab-bd193aa9c61a">
     NdisAllocateNetBufferPool</a> function. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>allocateCloneFlags</i> [in]

<dd>
<p>There are currently no flags defined for this function. Callout drivers should set this parameter
     to zero.</p>
</dd>

### -param <i>netBufferListChain</i> [out]

<dd>
<p>A pointer to a location that receives a pointer to a chain of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures that describe
     all of the cloned stream data.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsCloneStreamData0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The clone 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a> structure was
       successfully allocated.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>This cloned stream data can be injected by a callout driver into the TCP/IP network stack at a later
    time.</p>

<p>The 
    <b>FwpsCloneStreamData0</b> function clones the entire chain of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures contained in the
    existing 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a> data stream. The
    function trims unused data such that a callout driver can successfully pass the cloned chain to the 
    <a href="https://msdn.microsoft.com/d72c3067-21df-40ee-a898-100fcdc5eaca">
    FwpsStreamInjectAsync0</a> function.</p>

<p>After stream data in the clone NET_BUFFER_LIST structure chain has been successfully injected into the
    network stack, the 
    <a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a> callout function is called for
    each clone NET_BUFFER_LIST structure, and a callout should call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a> to
    free the clone NET_BUFFER_LIST structure.</p>

<p>A callout should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551161">FwpsDiscardClonedStreamData0</a> function if the cloned stream data is to be discarded without being
    reinjected.</p>

<p>This cloned stream data can be injected by a callout driver into the TCP/IP network stack at a later
    time.</p>

<p>The 
    <b>FwpsCloneStreamData0</b> function clones the entire chain of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures contained in the
    existing 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a> data stream. The
    function trims unused data such that a callout driver can successfully pass the cloned chain to the 
    <a href="https://msdn.microsoft.com/d72c3067-21df-40ee-a898-100fcdc5eaca">
    FwpsStreamInjectAsync0</a> function.</p>

<p>After stream data in the clone NET_BUFFER_LIST structure chain has been successfully injected into the
    network stack, the 
    <a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a> callout function is called for
    each clone NET_BUFFER_LIST structure, and a callout should call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a> to
    free the clone NET_BUFFER_LIST structure.</p>

<p>A callout should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551161">FwpsDiscardClonedStreamData0</a> function if the cloned stream data is to be discarded without being
    reinjected.</p>

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
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551161">FwpsDiscardClonedStreamData0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsCloneStreamData0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
