---
UID: NS.dot11wdi._WDI_TXRX_MPDU_PN
title: WDI_TXRX_MPDU_PN
author: windows-driver-content
description: The WDI_TXRX_MPDU_PN union defines the parameters that are passed down to the TXRX component.
old-location: netvista\wdi_txrx_mpdu_pn.htm
old-project: netvista
ms.assetid: F03F5BE6-B2F2-4A9A-8D6D-1ACC9F08C890
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDI_TXRX_MPDU_PN, WDI_TXRX_MPDU_PN
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
req.alt-api: WDI_TXRX_MPDU_PN
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
req.iface: 
---

# WDI_TXRX_MPDU_PN structure



## -description
<p>The 
  WDI_TXRX_MPDU_PN union defines the parameters that are passed down to the TXRX component.</p>


## -syntax

````
typedef union _WDI_TXRX_MPDU_PN {
  UINT32 Pn24;
  UINT64 Pn48;
  UINT64 Pn128[2];
} WDI_TXRX_MPDU_PN;
````


## -struct-fields
<dl>

### -field <b>Pn24</b>

<dd>
<p>WEP: 24-bit PN</p>
</dd>

### -field <b>Pn48</b>

<dd>
<p>TKIP or CCMP: 48-bit PN</p>
</dd>

### -field <b>Pn128</b>

<dd>
<p>WAPI: 128-bit PN</p>
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