---
UID: NE.wditypes._WDI_P2P_DISCOVER_TYPE
title: WDI_P2P_DISCOVER_TYPE
author: windows-driver-content
description: The WDI_P2P_DISCOVER_TYPE enumeration defines the Wi-Fi Direct discovery types.
old-location: netvista\wdi_p2p_discover_type.htm
old-project: netvista
ms.assetid: AE9910F7-A3B8-4C13-A5DC-7B9600C8C873
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
req.alt-api: WDI_P2P_DISCOVER_TYPE
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

# WDI_P2P_DISCOVER_TYPE enumeration



## -description
<p>The WDI_P2P_DISCOVER_TYPE enumeration defines the Wi-Fi Direct discovery types.</p>


## -syntax

````
typedef enum _WDI_P2P_DISCOVER_TYPE { 
  WDI_P2P_DISCOVER_TYPE_SCAN_ONLY             = 1,
  WDI_P2P_DISCOVER_TYPE_FIND_ONLY             = 2,
  WDI_P2P_DISCOVER_TYPE_AUTO                  = 3,
  WDI_P2P_DISCOVER_TYPE_SCAN_SOCIAL_CHANNELS  = 4
} WDI_P2P_DISCOVER_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_P2P_DISCOVER_TYPE_SCAN_ONLY"></a><a id="wdi_p2p_discover_type_scan_only"></a><b>WDI_P2P_DISCOVER_TYPE_SCAN_ONLY</b>

<dd>
<p>Device discovery occurs only during the scan phase. Adapter should scan each channel at least once every 250 milliseconds.</p>
</dd>

### -field <a id="WDI_P2P_DISCOVER_TYPE_FIND_ONLY"></a><a id="wdi_p2p_discover_type_find_only"></a><b>WDI_P2P_DISCOVER_TYPE_FIND_ONLY</b>

<dd>
<p>Device discovery occurs only during the find phase.</p>
</dd>

### -field <a id="WDI_P2P_DISCOVER_TYPE_AUTO"></a><a id="wdi_p2p_discover_type_auto"></a><b>WDI_P2P_DISCOVER_TYPE_AUTO</b>

<dd>
<p>Device discovery is determined by the port.</p>
</dd>

### -field <a id="WDI_P2P_DISCOVER_TYPE_SCAN_SOCIAL_CHANNELS"></a><a id="wdi_p2p_discover_type_scan_social_channels"></a><b>WDI_P2P_DISCOVER_TYPE_SCAN_SOCIAL_CHANNELS</b>

<dd>
<p>Port must perform device discovery by scanning only Wi-Fi Direct social channels. In this setting, the adapter should scan each social channel at least once every 250 milliseconds.</p>
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