---
UID: NE.wditypes._WDI_P2P_SCAN_TYPE
title: WDI_P2P_SCAN_TYPE
author: windows-driver-content
description: The WDI_P2P_SCAN_TYPE enumeration defines the Wi-Fi Direct scan types.
old-location: netvista\wdi_p2p_scan_type.htm
old-project: netvista
ms.assetid: 717847D7-D7D9-4FEE-B3DC-14B0404FA937
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
req.alt-api: WDI_P2P_SCAN_TYPE
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

# WDI_P2P_SCAN_TYPE enumeration



## -description
<p>The WDI_P2P_SCAN_TYPE enumeration defines the Wi-Fi Direct scan types.</p>


## -syntax

````
typedef enum _WDI_P2P_SCAN_TYPE { 
  WDI_P2P_SCAN_TYPE_ACTIVE   = 1,
  WDI_P2P_SCAN_TYPE_PASSIVE  = 2,
  WDI_P2P_SCAN_TYPE_AUTO     = 3
} WDI_P2P_SCAN_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_P2P_SCAN_TYPE_ACTIVE"></a><a id="wdi_p2p_scan_type_active"></a><b>WDI_P2P_SCAN_TYPE_ACTIVE</b>

<dd>
<p>Use active scanning during device discovery. Even for active scans, the port must follow regulatory restrictions on the channel and must not scan on channels that would need a passive scan.</p>
</dd>

### -field <a id="WDI_P2P_SCAN_TYPE_PASSIVE"></a><a id="wdi_p2p_scan_type_passive"></a><b>WDI_P2P_SCAN_TYPE_PASSIVE</b>

<dd>
<p>Use passive scanning during device discovery.</p>
</dd>

### -field <a id="WDI_P2P_SCAN_TYPE_AUTO"></a><a id="wdi_p2p_scan_type_auto"></a><b>WDI_P2P_SCAN_TYPE_AUTO</b>

<dd>
<p>Adapter determines scan type during device discovery. It should prefer using Active scans when possible. This is the default scan type setting.</p>
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