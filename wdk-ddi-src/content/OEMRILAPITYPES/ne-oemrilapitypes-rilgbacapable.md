---
UID: NE.oemrilapitypes.RILGBACAPABLE
title: RILGBACAPABLE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgbacapable.htm
ms.assetid: c1acc574-6e9e-40a1-8892-00572fcc545c
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: oemrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILGBACAPABLE
req.alt-loc: oemrilapitypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntstrsafe.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: RtlUnicodeStringVPrintfEx
req.iface: 
---

# RILGBACAPABLE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILGBACAPABLE { 
  RIL_GBA_UNKNOWN,
  RIL_GBA_NOT_SUPPORTED,
  RIL_GBA_ME_SUPPORTED,
  RIL_GBA_U_SUPPORTED
} RILGBACAPABLE;
````


## -enum-fields
<dl>

### -field <a id="RIL_GBA_UNKNOWN"></a><a id="ril_gba_unknown"></a><b>RIL_GBA_UNKNOWN</b>

<dd></dd>

### -field <a id="RIL_GBA_NOT_SUPPORTED"></a><a id="ril_gba_not_supported"></a><b>RIL_GBA_NOT_SUPPORTED</b>

<dd></dd>

### -field <a id="RIL_GBA_ME_SUPPORTED"></a><a id="ril_gba_me_supported"></a><b>RIL_GBA_ME_SUPPORTED</b>

<dd></dd>

### -field <a id="RIL_GBA_U_SUPPORTED"></a><a id="ril_gba_u_supported"></a><b>RIL_GBA_U_SUPPORTED</b>

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
<dt>Oemrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>