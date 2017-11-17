---
UID: NE.rilapitypes.RILUICCRECORDTYPE
title: RILUICCRECORDTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccrecordtype_2.htm
ms.assetid: 2eb26355-25e9-4edf-9695-08b172593712
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILUICCRECORDTYPE
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILUICCRECORDTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUICCRECORDTYPE { 
  RIL_UICCRECORDTYPE_TRANSPARENT,
  RIL_UICCRECORDTYPE_CYCLIC,
  RIL_UICCRECORDTYPE_LINEAR,
  RIL_UICCRECORDTYPE_BERTLV,
  RIL_UICCRECORDTYPE_MASTER,
  RIL_UICCRECORDTYPE_DEDICATED,
  RIL_UICCRECORDTYPE_MAX
} RILUICCRECORDTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCRECORDTYPE_TRANSPARENT"></a><a id="ril_uiccrecordtype_transparent"></a><b>RIL_UICCRECORDTYPE_TRANSPARENT</b>

<dd></dd>

### -field <a id="RIL_UICCRECORDTYPE_CYCLIC"></a><a id="ril_uiccrecordtype_cyclic"></a><b>RIL_UICCRECORDTYPE_CYCLIC</b>

<dd></dd>

### -field <a id="RIL_UICCRECORDTYPE_LINEAR"></a><a id="ril_uiccrecordtype_linear"></a><b>RIL_UICCRECORDTYPE_LINEAR</b>

<dd></dd>

### -field <a id="RIL_UICCRECORDTYPE_BERTLV"></a><a id="ril_uiccrecordtype_bertlv"></a><b>RIL_UICCRECORDTYPE_BERTLV</b>

<dd></dd>

### -field <a id="RIL_UICCRECORDTYPE_MASTER"></a><a id="ril_uiccrecordtype_master"></a><b>RIL_UICCRECORDTYPE_MASTER</b>

<dd></dd>

### -field <a id="RIL_UICCRECORDTYPE_DEDICATED"></a><a id="ril_uiccrecordtype_dedicated"></a><b>RIL_UICCRECORDTYPE_DEDICATED</b>

<dd></dd>

### -field <a id="RIL_UICCRECORDTYPE_MAX"></a><a id="ril_uiccrecordtype_max"></a><b>RIL_UICCRECORDTYPE_MAX</b>

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