---
UID: NS.wditypes._WDI_CHANNEL_MAPPING_ENTRY
title: WDI_CHANNEL_MAPPING_ENTRY
author: windows-driver-content
description: The WDI_CHANNEL_MAPPING_ENTRY structure defines a channel mapping entry.
old-location: netvista\wdi_channel_mapping_entry.htm
old-project: netvista
ms.assetid: F05DAD5F-C0A4-46E0-8069-7CEF5B6C5707
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDI_CHANNEL_MAPPING_ENTRY,
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
req.alt-api: WDI_CHANNEL_MAPPING_ENTRY
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

# WDI_CHANNEL_MAPPING_ENTRY structure



## -description
<p>The 
  WDI_CHANNEL_MAPPING_ENTRY structure defines a channel mapping entry.</p>


## -syntax

````
typedef struct _WDI_CHANNEL_MAPPING_ENTRY {
  UINT32 ChannelNumber;
  UINT32 ChannelCenterFrequency;
} WDI_CHANNEL_MAPPING_ENTRY, *PWDI_CHANNEL_MAPPING_ENTRY;
````


## -struct-fields
<dl>

### -field <b>ChannelNumber</b>

<dd>
<p>Specifies the logical channel number.</p>
</dd>

### -field <b>ChannelCenterFrequency</b>

<dd>
<p>Specifies the center frequency for the channel in MHz.</p>
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