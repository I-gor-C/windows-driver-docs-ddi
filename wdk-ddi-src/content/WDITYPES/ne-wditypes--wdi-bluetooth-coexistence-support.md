---
UID: NE.wditypes._WDI_BLUETOOTH_COEXISTENCE_SUPPORT
title: WDI_BLUETOOTH_COEXISTENCE_SUPPORT
author: windows-driver-content
description: The WDI_BLUETOOTH_COEXISTENCE_SUPPORT enumeration defines Bluetooth coexistence support values.
old-location: netvista\wdi_bluetooth_coexistence_support.htm
ms.assetid: 88642615-D5DD-4C0E-BAAA-308EB6050E77
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
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
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

### -field <a id="WDI_BLUETOOTH_COEXISTENCE_UNKNOWN"></a><a id="wdi_bluetooth_coexistence_unknown"></a><b>WDI_BLUETOOTH_COEXISTENCE_UNKNOWN</b>

<dd>
<p>Unknown.</p>
</dd>

### -field <a id="WDI_BLUETOOTH_COEXISTENCE_PERFORMANCE_MAINTAINED"></a><a id="wdi_bluetooth_coexistence_performance_maintained"></a><b>WDI_BLUETOOTH_COEXISTENCE_PERFORMANCE_MAINTAINED</b>

<dd>
<p>Wi-Fi and Bluetooth work at the same performance level during coexistence.</p>
</dd>

### -field <a id="WDI_BLUETOOTH_COEXISTENCE_WIFI_DEGRADED_TO_1x1"></a><a id="wdi_bluetooth_coexistence_wifi_degraded_to_1x1"></a><a id="WDI_BLUETOOTH_COEXISTENCE_WIFI_DEGRADED_TO_1X1"></a><b>WDI_BLUETOOTH_COEXISTENCE_WIFI_DEGRADED_TO_1x1</b>

<dd>
<p>Wi-Fi centered. On a 2X2 device, Wi-Fi and Bluetooth coexists. Wi-Fi performance is reduced to 1X1 level.</p>
</dd>

### -field <a id="WDI_BLUETOOTH_COEXISTENCE_WIFI_THROUGHPUT_DEGRADED"></a><a id="wdi_bluetooth_coexistence_wifi_throughput_degraded"></a><b>WDI_BLUETOOTH_COEXISTENCE_WIFI_THROUGHPUT_DEGRADED</b>

<dd>
<p>Bluetooth centered. When coexisting, Bluetooth has priority and restricts Wi-Fi performance.</p>
</dd>

### -field <a id="WDI_BLUETOOTH_COEXISTENCE_MUTUALLY_EXCLUSIVE"></a><a id="wdi_bluetooth_coexistence_mutually_exclusive"></a><b>WDI_BLUETOOTH_COEXISTENCE_MUTUALLY_EXCLUSIVE</b>

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