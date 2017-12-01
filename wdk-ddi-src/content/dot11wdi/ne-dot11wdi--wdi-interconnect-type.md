---
UID: NE.dot11wdi._WDI_INTERCONNECT_TYPE
title: WDI_INTERCONNECT_TYPE
author: windows-driver-content
description: The WDI_INTERCONNECT_TYPE enumeration defines the interconnect types.
old-location: netvista\wdi_interconnect_type.htm
old-project: netvista
ms.assetid: 58cb1ead-94a1-4587-bb2a-7b8e23f42eeb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_INTERCONNECT_TYPE
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
req.iface: ISynthSinkDMus
---

# WDI_INTERCONNECT_TYPE enumeration



## -description
<p>The WDI_INTERCONNECT_TYPE enumeration defines the interconnect types.</p>


## -syntax

````
typedef enum _WDI_INTERCONNECT_TYPE { 
  WDI_INTERCONNECT_MEMORY_MAPPED  = 0,
  WDI_INTERCONNECT_MESSAGE_BASED  = 1,
  WDI_INTERCONNECT_UNKNOWN        = 0xFF
} WDI_INTERCONNECT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_INTERCONNECT_MEMORY_MAPPED"></a><a id="wdi_interconnect_memory_mapped"></a><b>WDI_INTERCONNECT_MEMORY_MAPPED</b>

<dd>
<p>Target can access system memory (for example, PCI-based interconnect).</p>
</dd>

### -field <a id="WDI_INTERCONNECT_MESSAGE_BASED"></a><a id="wdi_interconnect_message_based"></a><b>WDI_INTERCONNECT_MESSAGE_BASED</b>

<dd>
<p>Message based interconnect (for example, USB or SDIO).</p>
</dd>

### -field <a id="WDI_INTERCONNECT_UNKNOWN"></a><a id="wdi_interconnect_unknown"></a><b>WDI_INTERCONNECT_UNKNOWN</b>

<dd>
<p>Unspecified interconnect type.</p>
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