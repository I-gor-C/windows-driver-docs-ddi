---
UID: NS.hbapiwmi._MS_SMHBA_SASPHYSTATISTICS
title: MS_SMHBA_SASPHYSTATISTICS
author: windows-driver-content
description: The MS_SMHBA_SASPHYSTATISTICS structure reports the traffic statistics for a SAS physical link.
old-location: storage\ms_smhba_sasphystatistics.htm
ms.assetid: bb2ab242-9002-4760-86b2-1aaf203ff710
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MS_SMHBA_SASPHYSTATISTICS
req.alt-loc: hbapiwmi.h
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
ms.keywords: MS_SMHBA_SASPHYSTATISTICS, MS_SMHBA_SASPHYSTATISTICS, *PMS_SMHBA_SASPHYSTATISTICS
req.iface: 
---

# MS_SMHBA_SASPHYSTATISTICS structure



## -description
<p>The MS_SMHBA_SASPHYSTATISTICS structure reports the traffic statistics for a SAS physical link.</p>


## -syntax

````
typedef struct _MS_SMHBA_SASPHYSTATISTICS {
  LONGLONG SecondsSinceLastReset;
  LONGLONG TxFrames;
  LONGLONG TxWords;
  LONGLONG RxFrames;
  LONGLONG RxWords;
  LONGLONG InvalidDwordCount;
  LONGLONG RunningDisparityErrorCount;
  LONGLONG LossofDwordSyncCount;
  LONGLONG PhyResetProblemCount;
} MS_SMHBA_SASPHYSTATISTICS, *PMS_SMHBA_SASPHYSTATISTICS;
````


## -struct-fields
<dl>

### -field <b>SecondsSinceLastReset</b>

<dd>
<p>The number of seconds since the statistics were last reset.</p>
</dd>

### -field <b>TxFrames</b>

<dd>
<p>The number of transmitted SAS frames across all protocols and classes.</p>
</dd>

### -field <b>TxWords</b>

<dd>
<p>The number of transmitted SAS words across all protocols and classes.</p>
</dd>

### -field <b>RxFrames</b>

<dd>
<p>The number of received SAS frames across all protocols and classes.</p>
</dd>

### -field <b>RxWords</b>

<dd>
<p>The number of received SAS words across all protocols and classes.</p>
</dd>

### -field <b>InvalidDwordCount</b>

<dd>
<p>The number of invalid DWORDs.</p>
</dd>

### -field <b>RunningDisparityErrorCount</b>

<dd>
<p>The number of disparity error counts.</p>
</dd>

### -field <b>LossofDwordSyncCount</b>

<dd>
<p>The loss of synchronization count.</p>
</dd>

### -field <b>PhyResetProblemCount</b>

<dd>
<p>A count of the number of physical link reset problems.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>