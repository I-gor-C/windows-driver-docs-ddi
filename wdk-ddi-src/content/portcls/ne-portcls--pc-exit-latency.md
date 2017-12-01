---
UID: NE.portcls._PC_EXIT_LATENCY
title: PC_EXIT_LATENCY
author: windows-driver-content
description: This topic discusses the PC_EXIT_LATENCY enum, and describes its members. The latency times map to specific maximum times in which the device must be able to exit its sleep state and enter the fully functional state (D0).
old-location: audio\pc_exit_latency.htm
old-project: audio
ms.assetid: 9D1DA7D6-4200-4B5A-9EA5-0455DF56D6D8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BarcodeSymbologyAttributesData, BarcodeSymbologyAttributesData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PC_EXIT_LATENCY
req.alt-loc: Portcls.h
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
req.iface: 
---

# PC_EXIT_LATENCY enumeration



## -description
<p>This topic discusses the PC_EXIT_LATENCY enum, and describes its members. The latency times map to specific maximum times in which the device must be able to exit its sleep state and enter the fully functional state (D0).</p>


## -syntax

````
typedef enum _PC_EXIT_LATENCY { 
  PcExitLatencyInstant     = 0,
  PcExitLatencyFast,
  PcExitLatencyResponsive
} PC_EXIT_LATENCY;
````


## -enum-fields
<dl>

### -field <a id="PcExitLatencyInstant"></a><a id="pcexitlatencyinstant"></a><a id="PCEXITLATENCYINSTANT"></a><b>PcExitLatencyInstant</b>

<dd>
<p>Indicates a 0-millisecond latency. This means "Do not power down" and it  will only be sent when a device is in the D0 state.</p>
</dd>

### -field <a id="PcExitLatencyFast"></a><a id="pcexitlatencyfast"></a><a id="PCEXITLATENCYFAST"></a><b>PcExitLatencyFast</b>

<dd>
<p>Indicates a 35-millisecond resume latency.</p>
</dd>

### -field <a id="PcExitLatencyResponsive"></a><a id="pcexitlatencyresponsive"></a><a id="PCEXITLATENCYRESPONSIVE"></a><b>PcExitLatencyResponsive</b>

<dd>
<p>Indicates a 300-millisecond resume latency.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>