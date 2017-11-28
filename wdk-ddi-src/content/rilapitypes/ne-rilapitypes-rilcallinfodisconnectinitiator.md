---
UID: NE.rilapitypes.RILCALLINFODISCONNECTINITIATOR
title: RILCALLINFODISCONNECTINITIATOR
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfodisconnectinitiator_2.htm
old-project: netvista
ms.assetid: 4ea730ab-0ba0-46cd-b156-0b2f32b2eafe
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLINFODISCONNECTINITIATOR
req.alt-loc: rilapitypes.h
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

# RILCALLINFODISCONNECTINITIATOR enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLINFODISCONNECTINITIATOR { 
  RIL_DISCINIT_LOCAL,
  RIL_DISCINIT_REMOTE,
  RIL_DISCINIT_MAX
} RILCALLINFODISCONNECTINITIATOR;
````


## -enum-fields
<dl>

### -field <a id="RIL_DISCINIT_LOCAL"></a><a id="ril_discinit_local"></a><b>RIL_DISCINIT_LOCAL</b>

<dd></dd>

### -field <a id="RIL_DISCINIT_REMOTE"></a><a id="ril_discinit_remote"></a><b>RIL_DISCINIT_REMOTE</b>

<dd></dd>

### -field <a id="RIL_DISCINIT_MAX"></a><a id="ril_discinit_max"></a><b>RIL_DISCINIT_MAX</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>