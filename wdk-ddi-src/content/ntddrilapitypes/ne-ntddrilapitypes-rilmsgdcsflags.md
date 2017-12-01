---
UID: NE.ntddrilapitypes.RILMSGDCSFLAGS
title: RILMSGDCSFLAGS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcsflags.htm
old-project: netvista
ms.assetid: 9c69d290-0cc6-4444-b9cb-a9555526e9ed
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
req.alt-api: RILMSGDCSFLAGS
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

# RILMSGDCSFLAGS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGDCSFLAGS { 
  RIL_DCSFLAG_COMPRESSED,
  RIL_DCSFLAG_INDICATIONACTIVE,
  RIL_DCSFLAG_DISCARD,
  RIL_DCSFLAG_ALL
} RILMSGDCSFLAGS;
````


## -enum-fields
<dl>

### -field <a id="RIL_DCSFLAG_COMPRESSED"></a><a id="ril_dcsflag_compressed"></a><b>RIL_DCSFLAG_COMPRESSED</b>

<dd></dd>

### -field <a id="RIL_DCSFLAG_INDICATIONACTIVE"></a><a id="ril_dcsflag_indicationactive"></a><b>RIL_DCSFLAG_INDICATIONACTIVE</b>

<dd></dd>

### -field <a id="RIL_DCSFLAG_DISCARD"></a><a id="ril_dcsflag_discard"></a><b>RIL_DCSFLAG_DISCARD</b>

<dd></dd>

### -field <a id="RIL_DCSFLAG_ALL"></a><a id="ril_dcsflag_all"></a><b>RIL_DCSFLAG_ALL</b>

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