---
UID: NS.iddcx.IDDCX_FRAME_STATISTICS_STEP
title: IDDCX_FRAME_STATISTICS_STEP
author: windows-driver-content
description: Gives information about the frame processing step being used by the driver.
old-location: display\iddcx_frame_statistics_step.htm
old-project: display
ms.assetid: a0d1f5b3-d527-417e-8d93-26d8277b7f12
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_FRAME_STATISTICS_STEP,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_FRAME_STATISTICS_STEP
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_FRAME_STATISTICS_STEP structure



## -description
<p>
                 Gives information about the frame processing step being used by the driver.</p>


## -syntax

````
typedef struct IDDCX_FRAME_STATISTICS_STE {
  UINT                             Size;
  IDDCX_FRAME_STATISTICS_STEP_TYPE Type;
  UINT64                           QpcTime;
  UINT32                           Data;
} IDDCX_FRAME_STATISTICS_STEP, *IDDCX_FRAME_STATISTICS_STEP;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>
                     Total size of the structure
                 </p>
</dd>

### -field <b>Type</b>

<dd>
<p>
                     The type of frame processing step
                 </p>
</dd>

### -field <b>QpcTime</b>

<dd>
<p>
                     Provides the system QPC time of the step
                 </p>
</dd>

### -field <b>Data</b>

<dd>
<p>
                     When driver defined processing part is used, then the driver can store additional data here
                 </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>