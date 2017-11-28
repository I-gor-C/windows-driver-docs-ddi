---
UID: NS.windot11._DOT11_WFD_CHANNEL
title: DOT11_WFD_CHANNEL
author: windows-driver-content
description: The DOT11_WFD_CHANNEL structure contains the channel information for a Peer-to-Pear (P2P) group.
old-location: netvista\dot11_wfd_channel.htm
old-project: netvista
ms.assetid: FE05F3D9-B1F0-4DC3-9265-22A76209A3E1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_WFD_CHANNEL,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_WFD_CHANNEL
req.alt-loc: Windot11.h
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
req.product: Windows 10 or later.
---

# DOT11_WFD_CHANNEL structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_CHANNEL {
  DOT11_COUNTRY_OR_REGION_STRING CountryRegionString;
  UCHAR                          OperatingClass;
  UCHAR                          ChannelNumber;
} DOT11_WFD_CHANNEL, *PDOT11_WFD_CHANNEL;
````


## -struct-fields
<dl>

### -field <b>CountryRegionString</b>

<dd>
<p>The country or region code where <b>OperatingClass</b> and <b>ChannelNumber</b> are valid.</p>
</dd>

### -field <b>OperatingClass</b>

<dd>
<p>The frequency band for <b>ChannelNumber</b>.</p>
</dd>

### -field <b>ChannelNumber</b>

<dd>
<p>The channel number for the P2P group.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with   Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>