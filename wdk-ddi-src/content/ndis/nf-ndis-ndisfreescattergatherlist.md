---
UID: NF.ndis.NdisFreeScatterGatherList
title: NdisFreeScatterGatherList function
author: windows-driver-content
description: The NdisFreeScatterGatherList function frees a scatter/gather list.
old-location: netvista\ndisfreescattergatherlist.htm
old-project: netvista
ms.assetid: 140be989-e578-4bfe-8b9e-56abb274933a
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisFreeScatterGatherList
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
req.alt-api: NdisFreeScatterGatherList
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
---

# NdisFreeScatterGatherList function



## -description
The 
  <b>NdisFreeScatterGatherList</b> function frees a scatter/gather list.


## -syntax

````
VOID NdisFreeScatterGatherList(
  _In_ NDIS_HANDLE          NdisHandle,
  _In_ PSCATTER_GATHER_LIST ScatterGatherListBuffer,
  _In_ BOOLEAN              WriteToDevice
);
````


## -parameters

### -param NdisHandle [in]

An NDIS driver or instance handle that was obtained during caller initialization. This should be
     the same handle that was passed to the 
     <a href="netvista.ndisbuildscattergatherlist">
     NdisBuildScatterGatherList</a> function when the scatter/gather list was created.

### -param ScatterGatherListBuffer [in]

A pointer to a caller-provided 
     <a href="kernel.scatter_gather_list">SCATTER_GATHER_LIST</a> structure to free.
     This must be the same buffer that was passed to the 
     <b>NdisBuildScatterGatherList</b> function when the scatter/gather list was allocated.

### -param WriteToDevice [in]

A BOOLEAN value that is set to <b>TRUE</b> if the scatter/gather list was used for writing to the device.
     Otherwise, it is <b>FALSE</b>.

## -returns
None

## -remarks
NDIS drivers call the 
    <b>NdisFreeScatterGatherList</b> function to free a scatter/gather list that was created with the 
    <a href="netvista.ndisbuildscattergatherlist">
    NdisBuildScatterGatherList</a> function.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported in NDIS 6.20 and later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
= DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisbuildscattergatherlist">NdisBuildScatterGatherList</a>
</dt>
<dt>
<a href="kernel.scatter_gather_list">SCATTER_GATHER_LIST</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFreeScatterGatherList function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
