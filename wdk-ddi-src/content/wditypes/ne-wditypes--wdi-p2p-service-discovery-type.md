---
UID: NE.wditypes._WDI_P2P_SERVICE_DISCOVERY_TYPE
title: WDI_P2P_SERVICE_DISCOVERY_TYPE
author: windows-driver-content
description: The WDI_P2P_SERVICE_DISCOVERY_TYPE enumeration defines the types of service discovery.
old-location: netvista\wdi_p2p_service_discovery_type.htm
old-project: netvista
ms.assetid: 5CA8F330-7AFE-44C9-BCCA-CA93479B9754
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_P2P_SERVICE_DISCOVERY_TYPE
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
req.iface: 
req.product: Windows 10 or later.
---

# WDI_P2P_SERVICE_DISCOVERY_TYPE enumeration



## -description
<p>The WDI_P2P_SERVICE_DISCOVERY_TYPE enumeration defines the types of service discovery.</p>


## -syntax

````
typedef enum _WDI_P2P_SERVICE_DISCOVERY_TYPE { 
  WDI_P2P_SERVICE_DISCOVERY_TYPE_NO_SERVICE_DISCOVERY      = 1,
  WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_NAME_ONLY         = 2,
  WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_INFORMATION       = 3,
  WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_NAME_ONLY    = 4,
  WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_INFORMATION  = 5
} WDI_P2P_SERVICE_DISCOVERY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_P2P_SERVICE_DISCOVERY_TYPE_NO_SERVICE_DISCOVERY"></a><a id="wdi_p2p_service_discovery_type_no_service_discovery"></a><b>WDI_P2P_SERVICE_DISCOVERY_TYPE_NO_SERVICE_DISCOVERY</b>

<dd>
<p>The adapter should only do a WFD discovery for WFD devices.  It should not encode service hashes in the P2P IEs.</p>
</dd>

### -field <a id="WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_NAME_ONLY"></a><a id="wdi_p2p_service_discovery_type_service_name_only"></a><b>WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_NAME_ONLY</b>

<dd>
<p>The adapter encodes service hashes in the P2P IEs during probe requests and indicates probe responses.  It does not perform any GAS queries for service information.</p>
</dd>

### -field <a id="WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_INFORMATION"></a><a id="wdi_p2p_service_discovery_type_service_information"></a><b>WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_INFORMATION</b>

<dd>
<p>The adapter encodes the service hashes in the IEs, tracks the service names from the probe responses, and does GAS queries to get service information for each responding device.  This is only applicable if the adapter supports the P2P Service Information Discovery capability.</p>
</dd>

### -field <a id="WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_NAME_ONLY"></a><a id="wdi_p2p_service_discovery_type_asp2_service_name_only"></a><b>WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_NAME_ONLY</b>

<dd>
<p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>The adapter encodes ASP2 service hashes in the P2P IEs during probe requests and indicates probe responses. It does not perform any GAS queries for service information.</p>
</dd>

### -field <a id="WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_INFORMATION"></a><a id="wdi_p2p_service_discovery_type_asp2_service_information"></a><b>WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_INFORMATION</b>

<dd>
<p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>The adapter encodes ASP2 service hashes in the P2P IEs, tracks  service names (service type and instance name) from the probe responses, and does GAS queries to get service information for each responding device.  This is only applicable if the adapter supports the P2P ASP2 Service Information Discovery capability.</p>
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