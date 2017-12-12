---
UID: NS.DOT11WDI._WDI_TXRX_PEER_CFG
title: _WDI_TXRX_PEER_CFG
author: windows-driver-content
description: The WDI_TXRX_PEER_CFG structure defines peer configuration.
old-location: netvista\wdi_txrx_peer_cfg.htm
old-project: netvista
ms.assetid: 5d2a97a3-3214-4f23-bf9d-d0ed292a46f0
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _WDI_TXRX_PEER_CFG, *PWDI_TXRX_PEER_CFG, WDI_TXRX_PEER_CFG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# _WDI_TXRX_PEER_CFG structure



## -description
The WDI_TXRX_PEER_CFG structure defines peer configuration.



## -syntax

````
typedef struct _WDI_TXRX_PEER_CFG {
  WDI_TXRX_PEER_QOS_CAPS PeerQoSConfig;
} WDI_TXRX_PEER_CFG, *PWDI_TXRX_PEER_CFG;
````


## -struct-fields

### -field PeerQoSConfig

The peer's QoS capability as defined in <a href="netvista.wdi_txrx_peer_qos_caps">WDI_TXRX_PEER_QOS_CAPS</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>