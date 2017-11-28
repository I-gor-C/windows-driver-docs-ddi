---
UID: NS.wditypes._WDI_DATA_RATE_ENTRY
title: WDI_DATA_RATE_ENTRY
author: windows-driver-content
description: The WDI_DATA_RATE_ENTRY structure defines a data rate entry.
old-location: netvista\wdi_data_rate_entry.htm
old-project: netvista
ms.assetid: 16A4B49B-9912-40BE-80E8-68416B966B71
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDI_DATA_RATE_ENTRY,
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
req.alt-api: WDI_DATA_RATE_ENTRY
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

# WDI_DATA_RATE_ENTRY structure



## -description
<p>The 
  WDI_DATA_RATE_ENTRY structure defines a data rate entry.</p>


## -syntax

````
typedef struct _WDI_DATA_RATE_ENTRY {
  UINT8  DataRateFlag;
  UINT16 DataRateValue;
} WDI_DATA_RATE_ENTRY, *PWDI_DATA_RATE_ENTRY;
````


## -struct-fields
<dl>

### -field <b>DataRateFlag</b>

<dd>
<p>Specifies data rate flags as defined in WDI_DATA_RATE_FLAGS.</p>
</dd>

### -field <b>DataRateValue</b>

<dd>
<p>Specifies the data rate in units of 500 kilobits per second. The value is in the range from 0x0002 through 0xffff.
</p>
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