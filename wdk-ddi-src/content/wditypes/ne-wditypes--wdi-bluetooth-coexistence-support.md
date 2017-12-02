---
UID: NE.wditypes._WDI_BLUETOOTH_COEXISTENCE_SUPPORT
title: WDI_BLUETOOTH_COEXISTENCE_SUPPORT
author: windows-driver-content
description: The WDI_BLUETOOTH_COEXISTENCE_SUPPORT enumeration defines Bluetooth coexistence support values.
old-location: netvista\wdi_bluetooth_coexistence_support.htm
old-project: netvista
ms.assetid: 88642615-D5DD-4C0E-BAAA-308EB6050E77
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: WDI_BLUETOOTH_COEXISTENCE_SUPPORT
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

# WDI_BLUETOOTH_COEXISTENCE_SUPPORT enumeration



## -description
<p>The WDI_BLUETOOTH_COEXISTENCE_SUPPORT enumeration defines Bluetooth coexistence support values.</p>


## -syntax

````
typedef enum _WDI_BLUETOOTH_COEXISTENCE_SUPPORT { 
  WDI_BLUETOOTH_COEXISTENCE_UNKNOWN                   = 0,
  WDI_BLUETOOTH_COEXISTENCE_PERFORMANCE_MAINTAINED    = 1,
  WDI_BLUETOOTH_COEXISTENCE_WIFI_DEGRADED_TO_1x1      = 2,
  WDI_BLUETOOTH_COEXISTENCE_WIFI_THROUGHPUT_DEGRADED  = 3,
  WDI_BLUETOOTH_COEXISTENCE_MUTUALLY_EXCLUSIVE        = 4
} WDI_BLUETOOTH_COEXISTENCE_SUPPORT;
````


## -enum-fields
<dl>

### -field WDI_BLUETOOTH_COEXISTENCE_UNKNOWN

<dd>
<p>Unknown.</p>
</dd>

### -field WDI_BLUETOOTH_COEXISTENCE_PERFORMANCE_MAINTAINED

<dd>
<p>Wi-Fi and Bluetooth work at the same performance level during coexistence.</p>
</dd>

### -field WDI_BLUETOOTH_COEXISTENCE_WIFI_DEGRADED_TO_1x1

<dd>
<p>Wi-Fi centered. On a 2X2 device, Wi-Fi and Bluetooth coexists. Wi-Fi performance is reduced to 1X1 level.</p>
</dd>

### -field WDI_BLUETOOTH_COEXISTENCE_WIFI_THROUGHPUT_DEGRADED

<dd>
<p>Bluetooth centered. When coexisting, Bluetooth has priority and restricts Wi-Fi performance.</p>
</dd>

### -field WDI_BLUETOOTH_COEXISTENCE_MUTUALLY_EXCLUSIVE

<dd>
<p>Wi-Fi and Bluetooth are mutually exclusive. One of the two stops working.</p>
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