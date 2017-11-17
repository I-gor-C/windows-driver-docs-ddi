---
UID: NS.dot11wdi._WDI_TXRX_PEER_CFG
title: WDI_TXRX_PEER_CFG
author: windows-driver-content
description: The WDI_TXRX_PEER_CFG structure defines peer configuration.
old-location: netvista\wdi_txrx_peer_cfg.htm
ms.assetid: 5d2a97a3-3214-4f23-bf9d-d0ed292a46f0
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_TXRX_PEER_CFG
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
req.irql: PASSIVE_LEVEL
ms.keywords: WDI_TXRX_PEER_CFG, WDI_TXRX_PEER_CFG, *PWDI_TXRX_PEER_CFG
req.iface: 
---

# WDI_TXRX_PEER_CFG structure



## -description
<p>The WDI_TXRX_PEER_CFG structure defines peer configuration.</p>


## -syntax

````
typedef struct _WDI_TXRX_PEER_CFG {
  WDI_TXRX_PEER_QOS_CAPS PeerQoSConfig;
} WDI_TXRX_PEER_CFG, *PWDI_TXRX_PEER_CFG;
````


## -struct-fields
<dl>

### -field <b>PeerQoSConfig</b>

<dd>
<p>The peer's QoS capability as defined in <a href="https://msdn.microsoft.com/library/windows/hardware/dn898191">WDI_TXRX_PEER_QOS_CAPS</a>.</p>
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