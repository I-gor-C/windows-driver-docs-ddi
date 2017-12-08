---
UID: NS.iddcx.IDARG_IN_REPORTFRAMESTATISTICS
title: IDARG_IN_REPORTFRAMESTATISTICS
author: windows-driver-content
description: Gives information about frame statistics.
old-location: display\idarg_in_reportframestatistics.htm
old-project: display
ms.assetid: 3d3e0dca-bb05-4e5c-aa4a-76bb178f60bf
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_REPORTFRAMESTATISTICS,
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
req.alt-api: IDARG_IN_REPORTFRAMESTATISTICS
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

# IDARG_IN_REPORTFRAMESTATISTICS structure



## -description
<p>
                 Gives information about frame statistics.</p>


## -syntax

````
typedef struct IDARG_IN_REPORTFRAMESTATISTICS {
  IDDCX_FRAME_STATISTICS FrameStatistics;
} IDARG_IN_REPORTFRAMESTATISTICS, *IDARG_IN_REPORTFRAMESTATISTICS;
````


## -struct-fields
<dl>

### -field FrameStatistics

<dd>
<p>
                     [in] Frame statics being reported.
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