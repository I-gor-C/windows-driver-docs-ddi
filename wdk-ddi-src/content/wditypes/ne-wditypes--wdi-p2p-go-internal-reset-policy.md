---
UID: NE.wditypes._WDI_P2P_GO_INTERNAL_RESET_POLICY
title: WDI_P2P_GO_INTERNAL_RESET_POLICY
author: windows-driver-content
description: The WDI_P2P_GO_INTERNAL_RESET_POLICY enumeration defines the Wi-Fi Direct Group Owner internal reset policies.
old-location: netvista\wdi_p2p_go_internal_reset_policy.htm
old-project: netvista
ms.assetid: 7932A2BB-DD6D-4DF7-BDF9-4E476B06B0B5
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: WDI_P2P_GO_INTERNAL_RESET_POLICY
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

# WDI_P2P_GO_INTERNAL_RESET_POLICY enumeration



## -description
<p>The WDI_P2P_GO_INTERNAL_RESET_POLICY enumeration defines the Wi-Fi Direct Group Owner internal reset policies.</p>


## -syntax

````
typedef enum _WDI_P2P_GO_INTERNAL_RESET_POLICY { 
  WDI_P2P_GO_INTERNAL_RESET_POLICY_USE_LAST_CHANNEL            = 1,
  WDI_P2P_GO_INTERNAL_RESET_POLICY_ALLOW_CHANNEL_OPTIMIZATION  = 2
} WDI_P2P_GO_INTERNAL_RESET_POLICY;
````


## -enum-fields
<dl>

### -field <a id="WDI_P2P_GO_INTERNAL_RESET_POLICY_USE_LAST_CHANNEL"></a><a id="wdi_p2p_go_internal_reset_policy_use_last_channel"></a><b>WDI_P2P_GO_INTERNAL_RESET_POLICY_USE_LAST_CHANNEL</b>

<dd>
<p>If an internal-to-firmware Group Owner reset is performed, post-reset Group Owner must operate on the same operating channel as before the internal reset operation.</p>
</dd>

### -field <a id="WDI_P2P_GO_INTERNAL_RESET_POLICY_ALLOW_CHANNEL_OPTIMIZATION"></a><a id="wdi_p2p_go_internal_reset_policy_allow_channel_optimization"></a><b>WDI_P2P_GO_INTERNAL_RESET_POLICY_ALLOW_CHANNEL_OPTIMIZATION</b>

<dd>
<p>If an internal-to-firmware Group Owner reset is performed, firmware may freely decide its new operating channel. For example, firmware may choose to minimize channel switching by adopting station port channel. If there is no optimization to be done, fall back to selecting previous operating channel.</p>
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