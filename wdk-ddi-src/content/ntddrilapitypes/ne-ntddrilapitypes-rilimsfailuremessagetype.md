---
UID: NE.ntddrilapitypes.RILIMSFAILUREMESSAGETYPE
title: RILIMSFAILUREMESSAGETYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsfailuremessagetype.htm
old-project: netvista
ms.assetid: e40241e6-90ee-4bbb-8fde-f52ffd838c1f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILIMSFAILUREMESSAGETYPE
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

# RILIMSFAILUREMESSAGETYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILIMSFAILUREMESSAGETYPE { 
  RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE,
  RIL_IMSFAILUREMESSAGETYPE_INCALL,
  RIL_IMSFAILUREMESSAGETYPE_MAX
} RILIMSFAILUREMESSAGETYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE"></a><a id="ril_imsfailuremessagetype_subscribe"></a><b>RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE</b>

<dd></dd>

### -field <a id="RIL_IMSFAILUREMESSAGETYPE_INCALL"></a><a id="ril_imsfailuremessagetype_incall"></a><b>RIL_IMSFAILUREMESSAGETYPE_INCALL</b>

<dd></dd>

### -field <a id="RIL_IMSFAILUREMESSAGETYPE_MAX"></a><a id="ril_imsfailuremessagetype_max"></a><b>RIL_IMSFAILUREMESSAGETYPE_MAX</b>

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