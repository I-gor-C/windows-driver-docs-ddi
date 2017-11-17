---
UID: NE.dot11wdi._WDI_TXRX_PEER_QOS_CAPS
title: WDI_TXRX_PEER_QOS_CAPS
author: windows-driver-content
description: The WDI_TXRX_PEER_QOS_CAPS enumeration defines the Quality of Service (QoS) capabilities.
old-location: netvista\wdi_txrx_peer_qos_caps.htm
ms.assetid: 34d53daa-3501-4532-82e3-e5b0ed452b66
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_TXRX_PEER_QOS_CAPS
req.alt-loc: dot11wdi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
req.iface: ISynthSinkDMus
---

# WDI_TXRX_PEER_QOS_CAPS enumeration



## -description
<p>The WDI_TXRX_PEER_QOS_CAPS enumeration defines the Quality of Service (QoS) capabilities.</p>


## -syntax

````
typedef enum _WDI_TXRX_PEER_QOS_CAPS { 
  WDI_TXRX_PeerCfgQosNone       = 0,
  WDI_TXRX_PeerCfgQosCapable    = 1,
  WDI_TXRX_PeerCfgQosUapsdTids  = 2
} WDI_TXRX_PEER_QOS_CAPS;
````


## -enum-fields
<dl>

### -field <a id="WDI_TXRX_PeerCfgQosNone"></a><a id="wdi_txrx_peercfgqosnone"></a><a id="WDI_TXRX_PEERCFGQOSNONE"></a><b>WDI_TXRX_PeerCfgQosNone</b>

<dd>
<p>Specifies that QoS was not negotiated for this peer during association.</p>
</dd>

### -field <a id="WDI_TXRX_PeerCfgQosCapable"></a><a id="wdi_txrx_peercfgqoscapable"></a><a id="WDI_TXRX_PEERCFGQOSCAPABLE"></a><b>WDI_TXRX_PeerCfgQosCapable</b>

<dd>
<p>Specifies that QoS was negotiated for this peer during association.</p>
</dd>

### -field <a id="WDI_TXRX_PeerCfgQosUapsdTids"></a><a id="wdi_txrx_peercfgqosuapsdtids"></a><a id="WDI_TXRX_PEERCFGQOSUAPSDTIDS"></a><b>WDI_TXRX_PeerCfgQosUapsdTids</b>

<dd>
<p>Reserved.</p>
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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>