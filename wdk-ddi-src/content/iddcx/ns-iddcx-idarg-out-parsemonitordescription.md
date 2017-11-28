---
UID: NS.iddcx.IDARG_OUT_PARSEMONITORDESCRIPTION
title: IDARG_OUT_PARSEMONITORDESCRIPTION
author: windows-driver-content
description: Gives information about the number of monitor modes and preferred monitor mode of a monitor.
old-location: display\idarg_out_parsemonitordescription.htm
old-project: display
ms.assetid: 30f4c178-5ef8-4650-b396-1e4bc9cc9125
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_OUT_PARSEMONITORDESCRIPTION,
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
req.alt-api: IDARG_OUT_PARSEMONITORDESCRIPTION
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

# IDARG_OUT_PARSEMONITORDESCRIPTION structure



## -description
<p>
                 Gives information about the number of monitor modes and  preferred monitor mode of a monitor.</p>


## -syntax

````
typedef struct IDARG_OUT_PARSEMONITORDESCRIPTION {
  UINT MonitorModeBufferOutputCount;
  UINT PreferredMonitorModeIdx;
} IDARG_OUT_PARSEMONITORDESCRIPTION, *IDARG_OUT_PARSEMONITORDESCRIPTION;
````


## -struct-fields
<dl>

### -field <b>MonitorModeBufferOutputCount</b>

<dd>
<p>
                     [out] If the <a href="https://msdn.microsoft.com/library/windows/hardware/mt761894">IDARG_IN_PARSEMONITORDESCRIPTION</a> value <b>pMonitorModes</b> was NULL, then the driver should set this to the number of monitor modes the driver would generate for the specified monitor description. f the <b>IDARG_IN_PARSEMONITORDESCRIPTION</b> value <b>pMonitorModes</b> was non-NULL then this is the count of the monitor modes that the driver copied to that buffer.</p>
</dd>

### -field <b>PreferredMonitorModeIdx</b>

<dd>
<p>
                     [out] Index into the <b>pMonitorModes</b> array of the preferred mode monitor mode, a value of <b>NO_PREFERRED_MODE</b>indicates that there is no preferred monitor mode.</p>
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