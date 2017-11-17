---
UID: NS.netdispumdddi.MIRACAST_WFD_CONNECTION_STATS
title: MIRACAST_WFD_CONNECTION_STATS
author: windows-driver-content
description: Contains bit rate info on the Wi-Fi Direct connection.
old-location: display\miracast_wfd_connection_stats.htm
ms.assetid: 3d5dd27f-8d0e-46e8-adbd-139db322cf6e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MIRACAST_WFD_CONNECTION_STATS
req.alt-loc: Netdispumdddi.h
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
ms.keywords: MIRACAST_WFD_CONNECTION_STATS, MIRACAST_WFD_CONNECTION_STATS
req.iface: 
---

# MIRACAST_WFD_CONNECTION_STATS structure



## -description
<p>Contains bit rate info on the Wi-Fi Direct connection.</p>


## -syntax

````
typedef struct {
  UINT64 CurrentBitRate;
  UINT64 LocalMaxBitRate;
  UINT64 RemoteMaxBitRate;
} MIRACAST_WFD_CONNECTION_STATS;
````


## -struct-fields
<dl>

### -field <b>CurrentBitRate</b>

<dd>
<p>The bit rate, in bits per second, that the operating system recommends that the audio/video encoder uses.</p>
</dd>

### -field <b>LocalMaxBitRate</b>

<dd>
<p>The maximum bit rate, in bits per second, that the local Wi-Fi Direct hardware can support.</p>
</dd>

### -field <b>RemoteMaxBitRate</b>

<dd>
<p>The maximum bit rate, in bits per second, that the Miracast sink hardware can support.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>