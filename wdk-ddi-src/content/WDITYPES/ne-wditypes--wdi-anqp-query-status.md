---
UID: NE.wditypes._WDI_ANQP_QUERY_STATUS
title: WDI_ANQP_QUERY_STATUS
author: windows-driver-content
description: The WDI_ANQP_QUERY_STATUS enumeration defines the Access Network Query Protocol (ANQP) query status values.
old-location: netvista\wdi_anqp_query_status.htm
ms.assetid: 5EC1B41D-2A6F-43B7-9E22-8A65CF4E11CA
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_ANQP_QUERY_STATUS
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDI_ANQP_QUERY_STATUS enumeration



## -description
<p>The WDI_ANQP_QUERY_STATUS enumeration defines the Access Network Query Protocol (ANQP) query status values.</p>


## -syntax

````
typedef enum _WDI_ANQP_QUERY_STATUS { 
  WDI_ANQP_QUERY_STATUS_SUCCESS                                         = 0,
  WDI_ANQP_QUERY_STATUS_FAILURE                                         = 1,
  WDI_ANQP_QUERY_STATUS_TIMED_OUT                                       = 2,
  WDI_ANQP_QUERY_STATUS_RESOURCES                                       = 3,
  WDI_ANQP_QUERY_STATUS_ADVERTISEMENT_PROTOCOL_NOT_SUPPORTED_ON_REMOTE  = 4,
  WDI_ANQP_QUERY_STATUS_GAS_PROTOCOL_FAILURE                            = 5,
  WDI_ANQP_QUERY_STATUS_ADVERTISEMENT_SERVER_NOT_RESPONDING             = 6,
  WDI_ANQP_QUERY_STATUS_ACCESS_ISSUES                                   = 7
} WDI_ANQP_QUERY_STATUS;
````


## -enum-fields
<dl>

### -field <a id="WDI_ANQP_QUERY_STATUS_SUCCESS"></a><a id="wdi_anqp_query_status_success"></a><b>WDI_ANQP_QUERY_STATUS_SUCCESS</b>

<dd>
<p>Maps to SUCCESS.</p>
</dd>

### -field <a id="WDI_ANQP_QUERY_STATUS_FAILURE"></a><a id="wdi_anqp_query_status_failure"></a><b>WDI_ANQP_QUERY_STATUS_FAILURE</b>

<dd>
<p>The failure did not map to any of the other status codes.</p>
</dd>

### -field <a id="WDI_ANQP_QUERY_STATUS_TIMED_OUT"></a><a id="wdi_anqp_query_status_timed_out"></a><b>WDI_ANQP_QUERY_STATUS_TIMED_OUT</b>

<dd>
<p>  Maps to GAS_QUERY_TIMEOUT. The STA timed out waiting for a GAS response.</p>
</dd>

### -field <a id="WDI_ANQP_QUERY_STATUS_RESOURCES"></a><a id="wdi_anqp_query_status_resources"></a><b>WDI_ANQP_QUERY_STATUS_RESOURCES</b>

<dd>
<p>The operating system is unable to allocate sufficient resources to complete the request.</p>
</dd>

### -field <a id="WDI_ANQP_QUERY_STATUS_ADVERTISEMENT_PROTOCOL_NOT_SUPPORTED_ON_REMOTE"></a><a id="wdi_anqp_query_status_advertisement_protocol_not_supported_on_remote"></a><b>WDI_ANQP_QUERY_STATUS_ADVERTISEMENT_PROTOCOL_NOT_SUPPORTED_ON_REMOTE</b>

<dd>
<p>Maps to GAS_ADVERTISEMENT_PROTOCOL_NOT_SUPPORTED. The GAS advertisement protocol is not supported on the remote device. </p>
</dd>

### -field <a id="WDI_ANQP_QUERY_STATUS_GAS_PROTOCOL_FAILURE"></a><a id="wdi_anqp_query_status_gas_protocol_failure"></a><b>WDI_ANQP_QUERY_STATUS_GAS_PROTOCOL_FAILURE</b>

<dd>
<p>Mapped for any of the following errors.</p>
<ul>
<li>NO_OUTSTANDING_GAS_REQUEST</li>
<li>GAS_QUERY_RESPONSE_TOO_LARGE</li>
<li>TRANSMISSION_FAILURE</li>
</ul>
</dd>

### -field <a id="WDI_ANQP_QUERY_STATUS_ADVERTISEMENT_SERVER_NOT_RESPONDING"></a><a id="wdi_anqp_query_status_advertisement_server_not_responding"></a><b>WDI_ANQP_QUERY_STATUS_ADVERTISEMENT_SERVER_NOT_RESPONDING</b>

<dd>
<p>Mapped for any of the following errors.</p>
<ul>
<li>GAS_RESPONSE_NOT_RECEIVED_FROM_SERVER</li>
<li>GAS_QUERY_TIMEOUT</li>
<li>SERVER_UNREACHABLE</li>
</ul>
</dd>

### -field <a id="WDI_ANQP_QUERY_STATUS_ACCESS_ISSUES"></a><a id="wdi_anqp_query_status_access_issues"></a><b>WDI_ANQP_QUERY_STATUS_ACCESS_ISSUES</b>

<dd>
<p>Mapped for any of the following errors.</p>
<ul>
<li>REJECTED_HOME_WITH_SUGGESTED_CHANGES</li>
<li>REJECTED_FOR_SSP_PERMISSIONS</li>
<li>AP does not support unauthenticated access</li>
</ul>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>