---
UID: NS.wditypes._WDI_TYPE_MIC
title: WDI_TYPE_MIC
author: windows-driver-content
description: The WDI_TYPE_MIC structure defines the MIC (802.11r).
old-location: netvista\wdi_type_mic.htm
old-project: netvista
ms.assetid: A21EEC35-98F2-4B68-A851-1C45D7F55194
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_MIC, WDI_TYPE_MIC, *PWDI_TYPE_MIC
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
req.alt-api: WDI_TYPE_MIC
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

# WDI_TYPE_MIC structure



## -description
<p>The WDI_TYPE_MIC structure defines the MIC (802.11r).</p>


## -syntax

````
typedef struct _WDI_TYPE_MIC {
  UINT8 Value[16];
} WDI_TYPE_MIC, *PWDI_TYPE_MIC;
````


## -struct-fields
<dl>

### -field <b>Value</b>

<dd>
<p>The MIC.</p>
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