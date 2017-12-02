---
UID: NF.fwpsk.FwpsAllocateNetBufferAndNetBufferList0
title: FwpsAllocateNetBufferAndNetBufferList0
author: windows-driver-content
description: The FwpsAllocateNetBufferAndNetBufferList0 function allocates a new NET_BUFFER_LIST structure.Note  FwpsAllocateNetBufferAndNetBufferList0 is a specific version of FwpsAllocateNetBufferAndNetBufferList.
old-location: netvista\fwpsallocatenetbufferandnetbufferlist0.htm
old-project: netvista
ms.assetid: d7f2d3c0-f2c9-4624-b3e1-9fbbf64c7186
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FwpsAllocateNetBufferAndNetBufferList0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsAllocateNetBufferAndNetBufferList0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
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
req.iface: 
---

# FwpsAllocateNetBufferAndNetBufferList0 function



## -description
<p>The 
  <b>FwpsAllocateNetBufferAndNetBufferList0</b> function allocates a new 
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
NTSTATUS NTAPI FwpsAllocateNetBufferAndNetBufferList0(
  _In_     NDIS_HANDLE     poolHandle,
  _In_     USHORT          contextSize,
  _In_     USHORT          contextBackFill,
  _In_opt_ MDL             *mdlChain,
  _In_     ULONG           dataOffset,
  _In_     SIZE_T          dataLength,
  _Out_    NET_BUFFER_LIST **netBufferList
);
````


## -parameters
<dl>

### -param poolHandle [in]

<dd>
<p>A 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> pool handle that was
     obtained from a previous call to the 
     <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">NdisAllocateNetBufferListPool</a> function.</p>
</dd>

### -param contextSize [in]

<dd>
<p>The size, in bytes, of used data space in the 
     <a href="..\ndis\ns-ndis--net-buffer-list-context.md">NET_BUFFER_LIST_CONTEXT</a> structure
     to reserve for the callout driver. The value of this parameter must be a multiple of the value defined
     by <b>MEMORY_ALLOCATION_ALIGNMENT</b>.</p>
</dd>

### -param contextBackFill [in]

<dd>
<p>The size, in bytes, of 
     unused data space (backfill space) that the callout driver requires. The 
     <b>FwpsAllocateNetBufferAndNetBufferList0</b> function adds this value to the value specified in the 
     <i>ContextSize</i> parameter and allocates additional space. The value of this parameter must be a
     multiple of the value defined by <b>MEMORY_ALLOCATION_ALIGNMENT</b>.</p>
</dd>

### -param mdlChain [in, optional]

<dd>
<p>A pointer to an MDL chain that is used to initialize the preallocated NET_BUFFER structure. This
     parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param dataOffset [in]

<dd>
<p>The initial offset, in bytes, from the start of the buffer to the start of the 
     used data space in the MDL chain. Data space ahead of this offset is 
     unused data space. Therefore, this value also represents the initial amount of available backfill
     space in the MDL chain.</p>
</dd>

### -param dataLength [in]

<dd>
<p>The length, in bytes, of the 
     used data space in the MDL chain.</p>
</dd>

### -param netBufferList [out]

<dd>
<p>A pointer to a variable that receives a pointer to the new 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsAllocateNetBufferAndNetBufferList0</b> function returns one of the following NTSTATUS
     codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The new 
       <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure was
       successfully allocated.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsAllocateNetBufferAndNetBufferList0</b> function to allocate a new 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>

<p>This function is a wrapper around the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
    NdisAllocateNetBufferAndNetBufferList</a> function, but it is specialized for use by WFP 
    <a href="netvista.packet_injection_functions">packet injection functions</a>.</p>

<p>After the data described by the new <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure has been successfully injected into the
    network stack, the callout driver frees the new <b>NET_BUFFER_LIST</b> structure by calling the 
    <a href="..\fwpsk\nf-fwpsk-fwpsfreenetbufferlist0.md">
    FwpsFreeNetBufferList0</a> function.</p>

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
<a href="..\fwpsk\nf-fwpsk-fwpsfreenetbufferlist0.md">FwpsFreeNetBufferList0</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
   NdisAllocateNetBufferAndNetBufferList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
   NdisAllocateNetBufferListPool</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list-context.md">NET_BUFFER_LIST_CONTEXT</a>
</dt>
<dt>
<a href="netvista.packet_injection_functions">Packet Injection Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsAllocateNetBufferAndNetBufferList0 function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
