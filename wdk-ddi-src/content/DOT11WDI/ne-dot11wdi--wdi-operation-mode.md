---
UID: NE.dot11wdi._WDI_OPERATION_MODE
title: WDI_OPERATION_MODE
author: windows-driver-content
description: The WDI_OPERATION_MODE enumeration defines operation modes.
old-location: netvista\wdi_operation_mode.htm
ms.assetid: 9838eeb9-6bd6-46a5-9361-6af3aa2d3014
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
req.alt-api: WDI_OPERATION_MODE
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

# WDI_OPERATION_MODE enumeration



## -description
<p>The WDI_OPERATION_MODE enumeration defines operation modes.</p>


## -syntax

````
typedef enum _WDI_OPERATION_MODE { 
  WDI_OPERATION_MODE_STA         = 0x1,
  WDI_OPERATION_MODE_P2P_DEVICE  = 0x8,
  WDI_OPERATION_MODE_P2P_CLIENT  = 0x10,
  WDI_OPERATION_MODE_P2P_GO      = 0x20
} WDI_OPERATION_MODE;
````


## -enum-fields
<dl>

### -field <a id="WDI_OPERATION_MODE_STA"></a><a id="wdi_operation_mode_sta"></a><b>WDI_OPERATION_MODE_STA</b>

<dd>
<p>Infrastructure client.</p>
</dd>

### -field <a id="WDI_OPERATION_MODE_P2P_DEVICE"></a><a id="wdi_operation_mode_p2p_device"></a><b>WDI_OPERATION_MODE_P2P_DEVICE</b>

<dd>
<p>Wi-Fi Direct Device.</p>
</dd>

### -field <a id="WDI_OPERATION_MODE_P2P_CLIENT"></a><a id="wdi_operation_mode_p2p_client"></a><b>WDI_OPERATION_MODE_P2P_CLIENT</b>

<dd>
<p>Wi-Fi Direct Client.</p>
</dd>

### -field <a id="WDI_OPERATION_MODE_P2P_GO"></a><a id="wdi_operation_mode_p2p_go"></a><b>WDI_OPERATION_MODE_P2P_GO</b>

<dd>
<p>Wi-Fi Direct Group Owner.</p>
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