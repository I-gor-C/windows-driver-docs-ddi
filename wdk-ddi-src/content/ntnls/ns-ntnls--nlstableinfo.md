---
UID: NS.ntnls._NLSTABLEINFO
title: NLSTABLEINFO
author: windows-driver-content
description: Stores the NLS file formats .
old-location: kernel\nlstableinfo.htm
old-project: kernel
ms.assetid: B9E64163-B338-49C9-8167-C36B110AB710
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NLSTABLEINFO, NLSTABLEINFO, *PNLSTABLEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntnls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NLSTABLEINFO
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
req.iface: 
---

# NLSTABLEINFO structure



## -description
<p>Stores the NLS file formats .</p>


## -syntax

````
typedef struct _NLSTABLEINFO {
  CPTABLEINFO    OemTableInfo;
  CPTABLEINFO    AnsiTableInfo;
  PUSHORT        UpperCaseTable;
  LowerCaseTable PUSHORT;
} NLSTABLEINFO, *PNLSTABLEINFO;
````


## -struct-fields
<dl>

### -field <b>OemTableInfo</b>

<dd>
<p>Specifies OEM table.</p>
</dd>

### -field <b>AnsiTableInfo</b>

<dd>
<p>Specifies an ANSI table. </p>
</dd>

### -field <b>UpperCaseTable</b>

<dd>
<p>Specifies an 844 format uppercase table.</p>
</dd>

### -field <b>PUSHORT</b>

<dd>
<p>Specifies an 844 format lowercase table.</p>
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