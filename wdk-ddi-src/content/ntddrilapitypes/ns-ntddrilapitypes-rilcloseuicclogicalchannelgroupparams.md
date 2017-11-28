---
UID: NS.ntddrilapitypes.RILCLOSEUICCLOGICALCHANNELGROUPPARAMS
title: RILCLOSEUICCLOGICALCHANNELGROUPPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcloseuicclogicalchannelgroupparams.htm
old-project: netvista
ms.assetid: 9442df60-7280-4c09-bea0-45ed2ac70694
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILCLOSEUICCLOGICALCHANNELGROUPPARAMS, RILCLOSEUICCLOGICALCHANNELGROUPPARAMS, *LPRILCLOSEUICCLOGICALCHANNELGROUPPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCLOSEUICCLOGICALCHANNELGROUPPARAMS
req.alt-loc: ntddrilapitypes.h
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
---

# RILCLOSEUICCLOGICALCHANNELGROUPPARAMS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILCLOSEUICCLOGICALCHANNELGROUPPARAMS {
  DWORD  dwSlotIndex;
  DWORD  dwChannelGroup;
} RILCLOSEUICCLOGICALCHANNELGROUPPARAMS, RILCLOSEUICCLOGICALCHANNELGROUPPARAMS;
````


## -struct-fields
<dl>

### -field <b>dwSlotIndex</b>

<dd></dd>

### -field <b>dwChannelGroup</b>

<dd></dd>
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>