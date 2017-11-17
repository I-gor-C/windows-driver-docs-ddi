---
UID: NE.ntddrilapitypes.RILMSGBCGENERALWARNINGTYPE
title: RILMSGBCGENERALWARNINGTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgbcgeneralwarningtype.htm
ms.assetid: c9d1a52e-e133-4fb5-a7a1-75699fe35cac
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
req.alt-api: RILMSGBCGENERALWARNINGTYPE
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

# RILMSGBCGENERALWARNINGTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGBCGENERALWARNINGTYPE { 
  RIL_WARNINGTYPE_TSUNAMI,
  RIL_WARNINGTYPE_EARTHQUAKETSUNAMI,
  RIL_WARNINGTYPE_TEST,
  RIL_WARNINGTYPE_OTHER,
  RIL_WARNINGTYPE_RESERVED,
  RIL_WARNINGTYPE_MAX
} RILMSGBCGENERALWARNINGTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_WARNINGTYPE_TSUNAMI"></a><a id="ril_warningtype_tsunami"></a><b>RIL_WARNINGTYPE_TSUNAMI</b>

<dd></dd>

### -field <a id="RIL_WARNINGTYPE_EARTHQUAKETSUNAMI"></a><a id="ril_warningtype_earthquaketsunami"></a><b>RIL_WARNINGTYPE_EARTHQUAKETSUNAMI</b>

<dd></dd>

### -field <a id="RIL_WARNINGTYPE_TEST"></a><a id="ril_warningtype_test"></a><b>RIL_WARNINGTYPE_TEST</b>

<dd></dd>

### -field <a id="RIL_WARNINGTYPE_OTHER"></a><a id="ril_warningtype_other"></a><b>RIL_WARNINGTYPE_OTHER</b>

<dd></dd>

### -field <a id="RIL_WARNINGTYPE_RESERVED"></a><a id="ril_warningtype_reserved"></a><b>RIL_WARNINGTYPE_RESERVED</b>

<dd></dd>

### -field <a id="RIL_WARNINGTYPE_MAX"></a><a id="ril_warningtype_max"></a><b>RIL_WARNINGTYPE_MAX</b>

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