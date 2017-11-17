---
UID: NS.netdispumdddi.MIRACAST_DATARATE_STATS
title: MIRACAST_DATARATE_STATS
author: windows-driver-content
description: Contains info used in the wireless display (Miracast) pfnDataRateNotify function about the audio/video encoder bit rate and failed or retried Wi-Fi frames.
old-location: display\miracast_datarate_stats.htm
ms.assetid: d4249b81-0ee7-49dd-9886-cdc5842f02d8
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
req.alt-api: MIRACAST_DATARATE_STATS
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
ms.keywords: MIRACAST_DATARATE_STATS, MIRACAST_DATARATE_STATS
req.iface: 
---

# MIRACAST_DATARATE_STATS structure



## -description
<p>Contains info used in the wireless display (Miracast) <a href="https://msdn.microsoft.com/5eb004d1-7cf8-45a3-aad5-2932b1a83bb8">pfnDataRateNotify</a> function about the audio/video encoder bit rate and failed or retried Wi-Fi frames.</p>


## -syntax

````
typedef struct {
  UINT64 EncoderBitRate;
  UINT64 CurrentMaxTxDataRate;
  UINT64 TransmittedFrameCount;
  UINT64 FailedFrameCount;
  UINT64 RetriedFrameCount;
  UINT64 MultipleRetryFrameCount;
} MIRACAST_DATARATE_STATS;
````


## -struct-fields
<dl>

### -field <b>EncoderBitRate</b>

<dd>
<p>The bit rate, in bits per second, that the operating system recommends that the audio/video encoder uses.</p>
</dd>

### -field <b>CurrentMaxTxDataRate</b>

<dd>
<p>The theoretical maximum speed, in bits per second, reported by the Wi-Fi driver.</p>
</dd>

### -field <b>TransmittedFrameCount</b>

<dd>
<p>The total number of Wi-Fi frames that were sent with zero retries since the previous time step.</p>
</dd>

### -field <b>FailedFrameCount</b>

<dd>
<p>The total number of Wi-Fi frames that exhausted the maximum number of retries since the previous time step.</p>
</dd>

### -field <b>RetriedFrameCount</b>

<dd>
<p>The total number of Wi-Fi frames that succeeded after a single retry since the previous time step.</p>
</dd>

### -field <b>MultipleRetryFrameCount</b>

<dd>
<p>The total number of Wi-Fi frames that succeeded after more than one retry since the previous time step.</p>
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