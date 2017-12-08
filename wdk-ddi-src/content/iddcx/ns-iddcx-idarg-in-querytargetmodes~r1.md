---
UID: NS.iddcx.IDARG_IN_QUERYTARGETMODES~r1
title: IDARG_IN_QUERYTARGETMODES
author: windows-driver-content
description: Gives information about the target modes associated with a monitor.
old-location: display\idarg_in_querytargetmodes.htm
old-project: display
ms.assetid: 4eeadee1-ac2a-46f5-88e0-fe8d3db3dcf1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_QUERYTARGETMODES,
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
req.alt-api: IDARG_IN_QUERYTARGETMODES
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

# IDARG_IN_QUERYTARGETMODES structure



## -description
<p>Gives information about the target modes associated with a monitor.</p>


## -syntax

````
typedef struct IDARG_IN_QUERYTARGETMODES {
  IDDCX_MONITOR_DESCRIPTION                                   MonitorDescription;
  UINT                                                        TargetModeBufferInputCount;
  _Field_size_(TargetModeBufferInputCount) IDDCX_TARGET_MODE* pTargetModes;
} IDARG_IN_QUERYTARGETMODES, *IDARG_IN_QUERYTARGETMODES;
````


## -struct-fields
<dl>

### -field MonitorDescription

<dd>
<p>
                     [in] The monitor description. </p>
<div class="alert"><b>Note</b>  This may not be the monitor description the driver originally provided in the monitor arrival call, which allows for the monitor description to be updated by the OS.</div>
<div> </div>
</dd>

### -field TargetModeBufferInputCount

<dd>
<p>
                     [in] The number of target modes the <b>pTargetModes</b> buffer passed to the driver can hold. If the value is zero, then the driver should not copy the target mode list to <b>pTargetModes.</b></p>
</dd>

### -field pTargetModes

<dd>
<p>
                     [out] Pointer to the buffer that the driver should copy the target modes it supports for this monitor
                 to.</p>
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