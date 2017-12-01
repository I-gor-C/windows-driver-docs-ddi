---
UID: NS.wditypes._WDI_TYPE_PMK_NAME
title: WDI_TYPE_PMK_NAME
author: windows-driver-content
description: The WDI_TYPE_PMK_NAME structure defines the PMKR0Name or PMKR1Name (802.11r).
old-location: netvista\wdi_type_pmk_name.htm
old-project: netvista
ms.assetid: 71020A3E-0839-4D73-B1B7-8A979BD0F5E0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.alt-api: WDI_TYPE_PMK_NAME
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

# WDI_TYPE_PMK_NAME structure



## -description
<p>The WDI_TYPE_PMK_NAME structure defines the PMKR0Name or PMKR1Name (802.11r).</p>


## -syntax

````
typedef struct _WDI_TYPE_PMK_NAME {
  UINT8 Name[16];
} WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME;
````


## -struct-fields
<dl>

### -field <b>Name</b>

<dd>
<p>the PMKR0Name or PMKR1Name.</p>
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