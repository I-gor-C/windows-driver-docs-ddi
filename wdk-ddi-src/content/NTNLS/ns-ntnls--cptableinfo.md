---
UID: NS.ntnls._CPTABLEINFO
title: CPTABLEINFO
author: windows-driver-content
description: Stores the NLS file formats.
old-location: kernel\cptableinfo.htm
ms.assetid: 20EE0017-760E-48A1-8658-2A0278843074
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntnls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CPTABLEINFO
req.alt-loc: Ntnls.h
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
ms.keywords: CPTABLEINFO, CPTABLEINFO, *PCPTABLEINFO
req.iface: 
---

# CPTABLEINFO structure



## -description
<p>Stores the NLS file formats.</p>


## -syntax

````
typedef struct _CPTABLEINFO {
  USHORT  CodePage;
  USHORT  MaximumCharacterSize;
  USHORT  DefaultChar;
  USHORT  UniDefaultChar;
  USHORT  TransDefaultChar;
  USHORT  TransUniDefaultChar;
  USHORT  DBCSCodePage;
  UCHAR   LeadByte[MAXIMUM_LEADBYTES];
  PUSHORT MultiByteTable;
  PVOID   WideCharTable;
  PUSHORT DBCSRanges;
  PUSHORT DBCSOffsets;
} CPTABLEINFO, *PCPTABLEINFO;
````


## -struct-fields
<dl>

### -field <b>CodePage</b>

<dd>
<p>Specifies the code page number.</p>
</dd>

### -field <b>MaximumCharacterSize</b>

<dd>
<p>Specifies the maximum length in bytes of a character.</p>
</dd>

### -field <b>DefaultChar</b>

<dd>
<p>Specifies the default character (MB).</p>
</dd>

### -field <b>UniDefaultChar</b>

<dd>
<p>Specifies the default character (Unicode).</p>
</dd>

### -field <b>TransDefaultChar</b>

<dd>
<p>Specifies the translation of the default character (Unicode).</p>
</dd>

### -field <b>TransUniDefaultChar</b>

<dd>
<p>Specifies the translation of the Unicode default character (MB).</p>
</dd>

### -field <b>DBCSCodePage</b>

<dd>
<p>Specifies non-zero for DBCS code pages.</p>
</dd>

### -field <b>LeadByte</b>

<dd>
<p>Specifies the lead byte ranges.</p>
</dd>

### -field <b>MultiByteTable</b>

<dd>
<p>Specifies a pointer to a MB translation table.</p>
</dd>

### -field <b>WideCharTable</b>

<dd>
<p>Specifies a pointer to a WC translation table.</p>
</dd>

### -field <b>DBCSRanges</b>

<dd>
<p>Specifies a pointer to DBCS ranges.</p>
</dd>

### -field <b>DBCSOffsets</b>

<dd>
<p>Specifies a pointer to DBCS offsets.</p>
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
<dt>Ntnls.h</dt>
</dl>
</td>
</tr>
</table>