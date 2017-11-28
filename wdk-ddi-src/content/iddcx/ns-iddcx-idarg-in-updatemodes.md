---
UID: NS.iddcx.IDARG_IN_UPDATEMODES
title: IDARG_IN_UPDATEMODES
author: windows-driver-content
description: Gives information about the target modes that will be updated by the driver.
old-location: display\idarg_in_updatemodes.htm
old-project: display
ms.assetid: d18f1da0-0cd0-48bf-bf01-a80887b6b2ac
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_UPDATEMODES,
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
req.alt-api: IDARG_IN_UPDATEMODES
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

# IDARG_IN_UPDATEMODES structure



## -description
<p>
                 Gives information about the target modes that will be updated by the driver.</p>


## -syntax

````
typedef struct IDARG_IN_UPDATEMODES {
  IDDCX_UPDATE_REASON                              Reason;
  UINT                                             TargetModeCount;
  _Field_size_(TargetModeCount) IDDCX_TARGET_MODE* pTargetModes;
} IDARG_IN_UPDATEMODES, *IDARG_IN_UPDATEMODES;
````


## -struct-fields
<dl>

### -field <b>Reason</b>

<dd>
<p>
                     Indicates the reason why the driver is updating the modes.
                 </p>
</dd>

### -field <b>TargetModeCount</b>

<dd>
<p>
                     [in] Number of target modes in the <b>pTargetModes</b> buffer.  This cannot be zero.</p>
</dd>

### -field <b>pTargetModes</b>

<dd>
<p>
                     [in] Pointer to the buffer that the driver should copy the target modes it supports for this monitor into.
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