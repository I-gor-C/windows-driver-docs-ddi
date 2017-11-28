---
UID: NE.ntddrilapitypes.RILMSGCDMALANGUAGE
title: RILMSGCDMALANGUAGE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmalanguage.htm
old-project: netvista
ms.assetid: b774fed4-533e-47ec-9e0a-da0e8fe2cfb0
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: RILMSGCDMALANGUAGE
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

# RILMSGCDMALANGUAGE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGCDMALANGUAGE { 
  RIL_MSGCDMALANG_ENGLISH,
  RIL_MSGCDMALANG_FRENCH,
  RIL_MSGCDMALANG_SPANISH,
  RIL_MSGCDMALANG_JAPANESE,
  RIL_MSGCDMALANG_KOREAN,
  RIL_MSGCDMALANG_CHINESE,
  RIL_MSGCDMALANG_HEBREW,
  RIL_MSGCDMALANG_MAX
} RILMSGCDMALANGUAGE;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGCDMALANG_ENGLISH"></a><a id="ril_msgcdmalang_english"></a><b>RIL_MSGCDMALANG_ENGLISH</b>

<dd></dd>

### -field <a id="RIL_MSGCDMALANG_FRENCH"></a><a id="ril_msgcdmalang_french"></a><b>RIL_MSGCDMALANG_FRENCH</b>

<dd></dd>

### -field <a id="RIL_MSGCDMALANG_SPANISH"></a><a id="ril_msgcdmalang_spanish"></a><b>RIL_MSGCDMALANG_SPANISH</b>

<dd></dd>

### -field <a id="RIL_MSGCDMALANG_JAPANESE"></a><a id="ril_msgcdmalang_japanese"></a><b>RIL_MSGCDMALANG_JAPANESE</b>

<dd></dd>

### -field <a id="RIL_MSGCDMALANG_KOREAN"></a><a id="ril_msgcdmalang_korean"></a><b>RIL_MSGCDMALANG_KOREAN</b>

<dd></dd>

### -field <a id="RIL_MSGCDMALANG_CHINESE"></a><a id="ril_msgcdmalang_chinese"></a><b>RIL_MSGCDMALANG_CHINESE</b>

<dd></dd>

### -field <a id="RIL_MSGCDMALANG_HEBREW"></a><a id="ril_msgcdmalang_hebrew"></a><b>RIL_MSGCDMALANG_HEBREW</b>

<dd></dd>

### -field <a id="RIL_MSGCDMALANG_MAX"></a><a id="ril_msgcdmalang_max"></a><b>RIL_MSGCDMALANG_MAX</b>

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