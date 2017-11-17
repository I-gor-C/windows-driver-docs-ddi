---
UID: NE.ntddrilapitypes.RILMSGCDMAMSGENCODING
title: RILMSGCDMAMSGENCODING
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmamsgencoding.htm
ms.assetid: d0bc5fa4-d08d-484c-b6e0-35c7f1d144c3
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGCDMAMSGENCODING
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
req.iface: 
---

# RILMSGCDMAMSGENCODING enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGCDMAMSGENCODING { 
  RIL_MSGCODING_7BITASCII,
  RIL_MSGCODING_UNICODE,
  RIL_MSGCODING_7BITGSM,
  RIL_MSGCODING_8BITGSM,
  RIL_MSGCODING_OCTET,
  RIL_MSGCODING_IA5,
  RIL_MSGCODING_JIS,
  RIL_MSGCODING_KOREAN,
  RIL_MSGCODING_LATIN_HEBREW,
  RIL_MSGCODING_LATIN,
  RIL_MSGCODING_MAX
} RILMSGCDMAMSGENCODING;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGCODING_7BITASCII"></a><a id="ril_msgcoding_7bitascii"></a><b>RIL_MSGCODING_7BITASCII</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_UNICODE"></a><a id="ril_msgcoding_unicode"></a><b>RIL_MSGCODING_UNICODE</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_7BITGSM"></a><a id="ril_msgcoding_7bitgsm"></a><b>RIL_MSGCODING_7BITGSM</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_8BITGSM"></a><a id="ril_msgcoding_8bitgsm"></a><b>RIL_MSGCODING_8BITGSM</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_OCTET"></a><a id="ril_msgcoding_octet"></a><b>RIL_MSGCODING_OCTET</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_IA5"></a><a id="ril_msgcoding_ia5"></a><b>RIL_MSGCODING_IA5</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_JIS"></a><a id="ril_msgcoding_jis"></a><b>RIL_MSGCODING_JIS</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_KOREAN"></a><a id="ril_msgcoding_korean"></a><b>RIL_MSGCODING_KOREAN</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_LATIN_HEBREW"></a><a id="ril_msgcoding_latin_hebrew"></a><b>RIL_MSGCODING_LATIN_HEBREW</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_LATIN"></a><a id="ril_msgcoding_latin"></a><b>RIL_MSGCODING_LATIN</b>

<dd></dd>

### -field <a id="RIL_MSGCODING_MAX"></a><a id="ril_msgcoding_max"></a><b>RIL_MSGCODING_MAX</b>

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