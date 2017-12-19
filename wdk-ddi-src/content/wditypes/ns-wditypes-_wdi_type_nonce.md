---
UID: NS.WDITYPES._WDI_TYPE_NONCE
title: _WDI_TYPE_NONCE
author: windows-driver-content
description: The WDI_TYPE_NONCE structure defines the SNonce or ANonce (802.11r).
old-location: netvista\wdi_type_nonce.htm
old-project: NetVista
ms.assetid: 62E3A714-BA18-4DD5-ACFC-A9EFA37EABB4
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WDI_TYPE_NONCE, *PWDI_TYPE_NONCE, PWDI_TYPE_NONCE, WDI_TYPE_NONCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
req.irql: 
req.product: Windows 10 or later.
---

# _WDI_TYPE_NONCE structure



## -description
The WDI_TYPE_NONCE structure defines the SNonce or ANonce (802.11r).



## -syntax

````
typedef struct _WDI_TYPE_NONCE {
  UINT8 Nonce[32];
} WDI_TYPE_NONCE, *PWDI_TYPE_NONCE;
````


## -struct-fields

### -field Nonce

The SNonce or ANonce.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>