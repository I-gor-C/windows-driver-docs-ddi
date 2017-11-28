---
UID: NE.ntddndis._NDIS_REQUEST_TYPE
title: NDIS_REQUEST_TYPE
author: windows-driver-content
description: The NDIS_REQUEST_TYPE enumeration identifies the request type in an OID request.
old-location: netvista\ndis_request_type.htm
old-project: netvista
ms.assetid: c4352eab-8bbd-429e-93ad-190372d29f2c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_REQUEST_TYPE
req.alt-loc: Ntddndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_REQUEST_TYPE enumeration



## -description
<p>The NDIS_REQUEST_TYPE enumeration identifies the request type in an OID request.</p>


## -syntax

````
typedef enum _NDIS_REQUEST_TYPE { 
  NdisRequestQueryInformation,
  NdisRequestSetInformation,
  NdisRequestQueryStatistics,
  NdisRequestOpen,
  NdisRequestClose,
  NdisRequestSend,
  NdisRequestTransferData,
  NdisRequestReset,
  NdisRequestGeneric1,
  NdisRequestGeneric2,
  NdisRequestGeneric3,
  NdisRequestGeneric4,
  NdisRequestMethod
} NDIS_REQUEST_TYPE, *PNDIS_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdisRequestQueryInformation"></a><a id="ndisrequestqueryinformation"></a><a id="NDISREQUESTQUERYINFORMATION"></a><b>NdisRequestQueryInformation</b>

<dd>
<p>A query-information request. For certain requests, NDIS satisfies the request. Otherwise,
     NDIS forwards such requests to the underlying driver's 
     <i>MiniportOidRequest</i> function. This type of request can originate in a user-mode application, filter module, or protocol driver.</p>
<div class="alert"><b>Note</b>  Drivers should treat <b>NdisRequestQueryInformation</b> and <b>NdisRequestQueryStatistics</b> queries identically.</div>
<div> </div>
</dd>

### -field <a id="NdisRequestSetInformation"></a><a id="ndisrequestsetinformation"></a><a id="NDISREQUESTSETINFORMATION"></a><b>NdisRequestSetInformation</b>

<dd>
<p>A set-information request. NDIS forwards such a request to the underlying driver's 
     <i>MiniportOidRequest</i> function.</p>
</dd>

### -field <a id="NdisRequestQueryStatistics"></a><a id="ndisrequestquerystatistics"></a><a id="NDISREQUESTQUERYSTATISTICS"></a><b>NdisRequestQueryStatistics</b>

<dd>
<p>A query-statistics request. For certain requests, NDIS satisfies the request. Otherwise,
     NDIS forwards such requests to the underlying driver's 
     <i>MiniportOidRequest</i> function. This type of request can originate in a user-mode application, filter module, or protocol driver.</p>
<div class="alert"><b>Note</b>  Drivers should treat <b>NdisRequestQueryInformation</b> and <b>NdisRequestQueryStatistics</b> queries identically.</div>
<div> </div>
</dd>

### -field <a id="NdisRequestOpen"></a><a id="ndisrequestopen"></a><a id="NDISREQUESTOPEN"></a><b>NdisRequestOpen</b>

<dd>
<p>This type is obsolete.</p>
</dd>

### -field <a id="NdisRequestClose"></a><a id="ndisrequestclose"></a><a id="NDISREQUESTCLOSE"></a><b>NdisRequestClose</b>

<dd>
<p>This type is obsolete.</p>
</dd>

### -field <a id="NdisRequestSend"></a><a id="ndisrequestsend"></a><a id="NDISREQUESTSEND"></a><b>NdisRequestSend</b>

<dd>
<p>This type is obsolete.</p>
</dd>

### -field <a id="NdisRequestTransferData"></a><a id="ndisrequesttransferdata"></a><a id="NDISREQUESTTRANSFERDATA"></a><b>NdisRequestTransferData</b>

<dd>
<p>This type is obsolete.</p>
</dd>

### -field <a id="NdisRequestReset"></a><a id="ndisrequestreset"></a><a id="NDISREQUESTRESET"></a><b>NdisRequestReset</b>

<dd>
<p>This type is obsolete.</p>
</dd>

### -field <a id="NdisRequestGeneric1"></a><a id="ndisrequestgeneric1"></a><a id="NDISREQUESTGENERIC1"></a><b>NdisRequestGeneric1</b>

<dd>
<p>A request that is specific to the type of the miniport driver.</p>
</dd>

### -field <a id="NdisRequestGeneric2"></a><a id="ndisrequestgeneric2"></a><a id="NDISREQUESTGENERIC2"></a><b>NdisRequestGeneric2</b>

<dd>
<p>A request that is specific to the type of the miniport driver.</p>
</dd>

### -field <a id="NdisRequestGeneric3"></a><a id="ndisrequestgeneric3"></a><a id="NDISREQUESTGENERIC3"></a><b>NdisRequestGeneric3</b>

<dd>
<p>A request that is specific to the type of the miniport driver.</p>
</dd>

### -field <a id="NdisRequestGeneric4"></a><a id="ndisrequestgeneric4"></a><a id="NDISREQUESTGENERIC4"></a><b>NdisRequestGeneric4</b>

<dd>
<p>A request that is specific to the type of the miniport driver.</p>
</dd>

### -field <a id="NdisRequestMethod"></a><a id="ndisrequestmethod"></a><a id="NDISREQUESTMETHOD"></a><b>NdisRequestMethod</b>

<dd>
<p>A method request. NDIS forwards such a request to the underlying driver's 
     <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_REQUEST_TYPE enumeration is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure.</p>

<p>The NDIS_REQUEST_TYPE enumeration is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure.</p>

<p>The NDIS_REQUEST_TYPE enumeration is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure.</p>

## -requirements
<table>
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
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_REQUEST_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
