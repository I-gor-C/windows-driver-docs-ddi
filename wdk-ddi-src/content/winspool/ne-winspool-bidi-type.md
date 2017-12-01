---
UID: NE.winspool.BIDI_TYPE
title: BIDI_TYPE
author: windows-driver-content
description: The BIDI_TYPE enumeration lists the possible values of data transferred in a bidi operation.
old-location: print\bidi_type.htm
old-project: print
ms.assetid: ebb79ad6-91a1-4bdf-a6f6-7e04ed2358d9
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PSHOWUIPARAMS, SHOWUIPARAMS, *PSHOWUIPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: winspool.h
req.include-header: Winspool.h
req.target-type: Windows
req.target-min-winverclnt: This enumeration is available in Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BIDI_TYPE
req.alt-loc: winspool.h
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

# BIDI_TYPE enumeration



## -description
<p>The BIDI_TYPE enumeration lists the possible values of data transferred in a bidi operation.</p>


## -syntax

````
typedef enum  { 
  BIDI_NULL    = 0,
  BIDI_INT     = 1,
  BIDI_FLOAT   = 2,
  BIDI_BOOL    = 3,
  BIDI_STRING  = 4,
  BIDI_TEXT    = 5,
  BIDI_ENUM    = 6,
  BIDI_BLOB    = 7
} BIDI_TYPE;
````


## -enum-fields
<dl>

### -field <a id="BIDI_NULL"></a><a id="bidi_null"></a><b>BIDI_NULL</b>

<dd>
<p>Indicates that there is no data.</p>
</dd>

### -field <a id="BIDI_INT"></a><a id="bidi_int"></a><b>BIDI_INT</b>

<dd>
<p>Indicates that the bidi data is an integer.</p>
</dd>

### -field <a id="BIDI_FLOAT"></a><a id="bidi_float"></a><b>BIDI_FLOAT</b>

<dd>
<p>Indicates that the bidi data is a floating-point number.</p>
</dd>

### -field <a id="BIDI_BOOL"></a><a id="bidi_bool"></a><b>BIDI_BOOL</b>

<dd>
<p>Indicates that the bidi data is either <b>TRUE</b> or <b>FALSE</b>.</p>
</dd>

### -field <a id="BIDI_STRING"></a><a id="bidi_string"></a><b>BIDI_STRING</b>

<dd>
<p>Indicates that the bidi data is a Unicode character string.</p>
</dd>

### -field <a id="BIDI_TEXT"></a><a id="bidi_text"></a><b>BIDI_TEXT</b>

<dd>
<p>Indicates that the bidi data is a nonlocalizable Unicode string.</p>
</dd>

### -field <a id="BIDI_ENUM"></a><a id="bidi_enum"></a><b>BIDI_ENUM</b>

<dd>
<p>Indicates that the bidi data value is a Unicode string.</p>
</dd>

### -field <a id="BIDI_BLOB"></a><a id="bidi_blob"></a><b>BIDI_BLOB</b>

<dd>
<p>Indicates that the bidi data is binary data.</p>
</dd>
</dl>

## -remarks
<p>The following correspondence applies between Simple Network Management Protocol (SNMP) types and bidi types defined in the BIDI_TYPE enumeration.</p>

<p>SNMP_SYNTAX_CNTR32</p>

<p>SNMP_SYNTAX_GAUGE32</p>

<p>SNMP_SYNTAX_INT</p>

<p>SNMP_SYNTAX_TIMETICKS</p>

<p>SNMP_SYNTAX_UINT32</p>

<p>BIDI_BOOL</p>

<p>BIDI_INT</p>

<p>SNMP_SYNTAX_IPADDR</p>

<p>SNMP_SYNTAX_OCTETS</p>

<p>SNMP_SYNTAX_OID</p>

<p>BIDI_ENUM</p>

<p>BIDI_STRING</p>

<p>BIDI_TEXT</p>

<p>SNMP_SYNTAX_CNTR64</p>

<p>SNMP_SYNTAX_OPAQUE</p>

<p>BIDI_BLOB</p>

<p>(none)</p>

<p>BIDI_FLOAT</p>

<p>See the smiValue structure in the Microsoft Windows SDK documentation for descriptions of the WinSNMP data types.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This enumeration is available in Windows XP and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winspool.h (include Winspool.h)</dt>
</dl>
</td>
</tr>
</table>