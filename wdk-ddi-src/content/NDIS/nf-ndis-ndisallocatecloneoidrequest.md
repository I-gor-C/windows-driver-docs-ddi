---
UID: NF.ndis.NdisAllocateCloneOidRequest
title: NdisAllocateCloneOidRequest
author: windows-driver-content
description: The NdisAllocateCloneOidRequest function allocates memory for a new NDIS_OID_REQUEST structure and copies all the information from an existing NDIS_OID_REQUEST structure to the newly allocated structure.
old-location: netvista\ndisallocatecloneoidrequest.htm
ms.assetid: 426ff4f4-7924-4115-9f66-b4152e2ba5bb
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisAllocateCloneOidRequest
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_OID_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisAllocateCloneOidRequest
req.iface: 
---

# NdisAllocateCloneOidRequest function



## -description
<p>The 
  <b>NdisAllocateCloneOidRequest</b> function allocates memory for a new 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure and copies all the
  information from an existing NDIS_OID_REQUEST structure to the newly allocated structure.</p>


## -syntax

````
NDIS_STATUS NdisAllocateCloneOidRequest(
  _In_  NDIS_HANDLE       SourceHandle,
  _In_  PNDIS_OID_REQUEST Request,
  _In_  UINT              PoolTag,
  _Out_ PNDIS_OID_REQUEST *CloneRequest
);
````


## -parameters
<dl>

### -param <i>SourceHandle</i> [in]

<dd>
<p>An NDIS handle that identifies a filter module or an intermediate driver's protocol
     binding.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>A pointer to an existing 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure from which NDIS
     copies the information to the newly allocated structure.</p>
</dd>

### -param <i>PoolTag</i> [in]

<dd>
<p>A kernel pool tag. The tag is a string, delimited by single quotation marks, with as many as four
     characters, usually specified in reverse order.</p>
</dd>

### -param <i>CloneRequest</i> [out]

<dd>
<p>A pointer to a pointer to an NDIS_OID_REQUEST structure. If NDIS returns NDIS_STATUS_SUCCESS, NDIS
     provides a pointer to the new, cloned NDIS_OID_REQUEST structure; otherwise, NDIS sets the pointer value
     to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>NdisAllocateClonedRequest</b> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS successfully allocated an NDIS_OID_REQUEST structure. The 
       <i>CloneRequest</i> parameter contains a pointer to the NDIS_OID_REQUEST structure.</p><dl>
<dt><b>NDIS_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The allocation request failed because the NDIS handle specified at 
       <i>SourceHandle</i> is not valid.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The allocation request failed because NDIS did not have sufficient resources to complete the
       allocation request.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The driver failed to allocate the cloned structure for reasons other than those in the preceding
       list.</p>

<p> </p>

## -remarks
<p>To forward a request down to the underlying drivers, an NDIS intermediate driver or filter driver must
    call 
    <b>NdisAllocateCloneOidRequest</b> to allocate a cloned 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure. A filter driver
    or intermediate driver should not forward the original NDIS_OID_REQUEST structure to underlying
    drivers.</p>

<p><b>NdisAllocateCloneOidRequest</b> allocates new memory and copies the data from an existing
    NDIS_OID_REQUEST structure to the new structure.</p>

<p>The driver must subsequently call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561845">NdisFreeCloneOidRequest</a> function
    to free the NDIS_OID_REQUEST structure.</p>

<p>To forward a request down to the underlying drivers, an NDIS intermediate driver or filter driver must
    call 
    <b>NdisAllocateCloneOidRequest</b> to allocate a cloned 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure. A filter driver
    or intermediate driver should not forward the original NDIS_OID_REQUEST structure to underlying
    drivers.</p>

<p><b>NdisAllocateCloneOidRequest</b> allocates new memory and copies the data from an existing
    NDIS_OID_REQUEST structure to the new structure.</p>

<p>The driver must subsequently call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561845">NdisFreeCloneOidRequest</a> function
    to free the NDIS_OID_REQUEST structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547990">Irql_OID_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561845">NdisFreeCloneOidRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateCloneOidRequest function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
