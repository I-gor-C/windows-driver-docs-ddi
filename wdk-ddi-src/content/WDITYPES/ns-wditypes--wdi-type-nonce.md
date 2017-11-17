---
UID: NS.wditypes._WDI_TYPE_NONCE
title: WDI_TYPE_NONCE
author: windows-driver-content
description: The WDI_TYPE_NONCE structure defines the SNonce or ANonce (802.11r).
old-location: netvista\wdi_type_nonce.htm
ms.assetid: 62E3A714-BA18-4DD5-ACFC-A9EFA37EABB4
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_TYPE_NONCE
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
ms.keywords: WDI_TYPE_NONCE, WDI_TYPE_NONCE, *PWDI_TYPE_NONCE
req.iface: 
req.product: Windows 10 or later.
---

# WDI_TYPE_NONCE structure



## -description
<p>The WDI_TYPE_NONCE structure defines the SNonce or ANonce (802.11r).</p>


## -syntax

````
typedef struct _WDI_TYPE_NONCE {
  UINT8 Nonce[32];
} WDI_TYPE_NONCE, *PWDI_TYPE_NONCE;
````


## -struct-fields
<dl>

### -field <b>Nonce</b>

<dd>
<p>The SNonce or ANonce.</p>
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