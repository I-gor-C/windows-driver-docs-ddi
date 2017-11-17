---
UID: NS.dot11wdi._WDI_TX_COMPLETE_DATA
title: WDI_TX_COMPLETE_DATA
author: windows-driver-content
description: The WDI_TX_COMPLETE_DATA structure defines TX completion data.
old-location: netvista\wdi_tx_complete_data.htm
ms.assetid: bf7951de-3368-4faf-9bae-272c6d76d1a0
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_TX_COMPLETE_DATA
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
ms.keywords: WDI_TX_COMPLETE_DATA, WDI_TX_COMPLETE_DATA, *PWDI_TX_COMPLETE_DATA
req.iface: 
---

# WDI_TX_COMPLETE_DATA structure



## -description
<p>The WDI_TX_COMPLETE_DATA structure defines TX completion data.</p>


## -syntax

````
typedef struct _WDI_TX_COMPLETE_DATA {
  UINT16           SeqCtl;
  UINT8            PnLength;
  UINT8            RetryCount;
  UINT16           wPad;
  WDI_TXRX_MPDU_PN MpduPN;
  UINT64           ReplayIHVReserved0;
  UINT64           ReplayIHVReserved1;
} WDI_TX_COMPLETE_DATA, *PWDI_TX_COMPLETE_DATA;
````


## -struct-fields
<dl>

### -field <b>SeqCtl</b>

<dd>
<p>The value of the sequence control field from the frame transmission.</p>
</dd>

### -field <b>PnLength</b>

<dd>
<p>The MPDU PN length for the transmitted frame.</p>
</dd>

### -field <b>RetryCount</b>

<dd>
<p>The number of attempts to transmit the frame.</p>
</dd>

### -field <b>wPad</b>

<dd>
<p>This member is reserved.</p>
</dd>

### -field <b>MpduPN</b>

<dd>
<p>The MPDU PN.</p>
</dd>

### -field <b>ReplayIHVReserved0</b>

<dd>
<p>Reserved for IHV use.</p>
</dd>

### -field <b>ReplayIHVReserved1</b>

<dd>
<p>Reserved for IHV use.</p>
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