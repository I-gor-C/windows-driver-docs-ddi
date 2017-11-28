---
UID: NF.ndis.NdisBuildScatterGatherList
title: NdisBuildScatterGatherList
author: windows-driver-content
description: The NdisBuildScatterGatherList function builds a scatter/gather list by using the specified parameters.
old-location: netvista\ndisbuildscattergatherlist.htm
old-project: netvista
ms.assetid: 439d68ec-9d27-484b-b6a3-9bae732d142e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisBuildScatterGatherList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisBuildScatterGatherList
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: = DISPATCH_LEVEL
req.iface: 
---

# NdisBuildScatterGatherList function



## -description
<p>The 
  <b>NdisBuildScatterGatherList</b> function builds a scatter/gather list by using the specified
  parameters.</p>


## -syntax

````
NDIS_STATUS NdisBuildScatterGatherList(
  _In_ NDIS_HANDLE                          NdisHandle,
  _In_ PNDIS_SCATTER_GATHER_LIST_PARAMETERS SGListParameters
);
````


## -parameters
<dl>

### -param <i>NdisHandle</i> [in]

<dd>
<p>An NDIS driver or instance handle that was obtained during caller initialization. For example, a
     miniport driver can use the NDIS handle that it obtained from the 
     <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
     NdisMRegisterMiniportDriver</a> or 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function.
     Other NDIS drivers can use the handles from the following functions:
     </p>
<dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564520">NdisRegisterProtocolDriver</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</p>
</dd>
</dl>
</dd>

### -param <i>SGListParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
     NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structure that specifies the parameters for allocating the
     scatter/gather list.</p>
</dd>
</dl>

## -returns
<p><b>NdisBuildScatterGatherList</b> can return the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_BUFFER_TOO_SHORT</b></dt>
</dl><p>The operation failed because the buffer length that is specified in the 
       <b>ScatterGatherListBufferSize</b> member of the 
       <a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
       NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structure was too short. In this case, NDIS provided the
       required buffer size in the 
       <b>ScatterGatherListBufferSizeNeeded</b> member.</p>

<p> </p>

## -remarks
<p>NDIS drivers call the 
    <b>NdisBuildScatterGatherList</b> function to build a scatter/gather list for a buffer. To call this
    function, a miniport driver specifies a miniport adapter handle or a protocol driver specifies an NDIS
    binding handle.</p>

<p>The underlying miniport adapter must have called 
    <a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
    NdisMRegisterScatterGatherDma</a> before a driver can call 
    <b>NdisBuildScatterGatherList</b>.</p>

<p>NDIS calls the 
    <a href="..\ndis\nc-ndis-ndis-process-sg-list.md">NetProcessSGList</a> function that is
    specified at the 
    <b>ProcessSGListHandler</b> member of the 
    <a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
    NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structure within the context of 
    <b>NdisBuildScatterGatherList</b>.</p>

<p>The drivers must call the 
    <a href="..\ndis\nf-ndis-ndisfreescattergatherlist.md">
    NdisFreeScatterGatherList</a> function to free a scatter/gather list that was created with the 
    <b>
    NdisBuildScatterGatherList</b> function.</p>

<p>NDIS drivers call the 
    <b>NdisBuildScatterGatherList</b> function to build a scatter/gather list for a buffer. To call this
    function, a miniport driver specifies a miniport adapter handle or a protocol driver specifies an NDIS
    binding handle.</p>

<p>The underlying miniport adapter must have called 
    <a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
    NdisMRegisterScatterGatherDma</a> before a driver can call 
    <b>NdisBuildScatterGatherList</b>.</p>

<p>NDIS calls the 
    <a href="..\ndis\nc-ndis-ndis-process-sg-list.md">NetProcessSGList</a> function that is
    specified at the 
    <b>ProcessSGListHandler</b> member of the 
    <a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
    NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structure within the context of 
    <b>NdisBuildScatterGatherList</b>.</p>

<p>The drivers must call the 
    <a href="..\ndis\nf-ndis-ndisfreescattergatherlist.md">
    NdisFreeScatterGatherList</a> function to free a scatter/gather list that was created with the 
    <b>
    NdisBuildScatterGatherList</b> function.</p>

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
<p>Supported in NDIS 6.20 and later.</p>
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
<p>= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
   NDIS_SCATTER_GATHER_LIST_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
   NdisMRegisterScatterGatherDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564520">NdisRegisterProtocolDriver</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-process-sg-list.md">NetProcessSGList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisBuildScatterGatherList function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
