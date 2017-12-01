---
UID: NF.ndis.NdisFDirectOidRequestComplete
title: NdisFDirectOidRequestComplete
author: windows-driver-content
description: Filter drivers call the NdisFDirectOidRequestComplete function to return the final status of a direct OID request for which the driver's FilterDirectOidRequest function returned NDIS_STATUS_PENDING.
old-location: netvista\ndisfdirectoidrequestcomplete.htm
old-project: netvista
ms.assetid: b6b4d4f4-63d5-496c-9082-f2e8d1a174ec
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisFDirectOidRequestComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFDirectOidRequestComplete
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisFDirectOidRequestComplete function



## -description
<p>Filter drivers call the 
  <b>NdisFDirectOidRequestComplete</b> function to return the final status of a direct OID request for which
  the driver's 
  <a href="..\ndis\nc-ndis-filter-direct-oid-request.md">FilterDirectOidRequest</a> function
  returned NDIS_STATUS_PENDING.</p>


## -syntax

````
VOID NdisFDirectOidRequestComplete(
  _In_ NDIS_HANDLE       NdisFilterHandle,
  _In_ PNDIS_OID_REQUEST OidRequest,
  _In_ NDIS_STATUS       Status
);
````


## -parameters
<dl>

### -param <i>NdisFilterHandle</i> [in]

<dd>
<p>The NDIS handle that identifies this filter module NDIS passed the handle to the filter driver in
     a call to the 
     <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function.</p>
</dd>

### -param <i>OidRequest</i> [in]

<dd>
<p>A pointer to a buffer that is formatted as an 
     <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> structure. The filter
     driver obtained this pointer as an input parameter to its 
     <a href="..\ndis\nc-ndis-filter-direct-oid-request.md">
     FilterDirectOidRequest</a> function.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>The final status of the request operation: NDIS_STATUS_SUCCESS or any driver-determined
     NDIS_STATUS_<i>Xxx</i> value except NDIS_STATUS_PENDING.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A filter driver that returns NDIS_STATUS_PENDING from its 
    <a href="..\ndis\nc-ndis-filter-direct-oid-request.md">FilterDirectOidRequest</a> function
    must call the 
    <b>NdisFDirectOidRequestComplete</b> function after the driver has finished the request operation.</p>

<p>If an overlying driver originated the direct OID request, NDIS calls the request complete function
    (see 
    <a href="..\ndis\nc-ndis-protocol-direct-oid-request-complete.md">
    ProtocolDirectOidRequestComplete</a> and 
    <a href="..\ndis\nc-ndis-filter-direct-oid-request-complete.md">
    FilterDirectOidRequestComplete</a>) of the overlying driver that originated the request.</p>

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
<p>Supported in NDIS 6.1 and later.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-direct-oid-request.md">FilterDirectOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-direct-oid-request-complete.md">
   FilterDirectOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-direct-oid-request-complete.md">
   ProtocolDirectOidRequestComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFDirectOidRequestComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
