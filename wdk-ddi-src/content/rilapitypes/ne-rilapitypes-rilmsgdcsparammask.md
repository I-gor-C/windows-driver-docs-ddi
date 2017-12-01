---
UID: NE.rilapitypes.RILMSGDCSPARAMMASK
title: RILMSGDCSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcsparammask_2.htm
old-project: netvista
ms.assetid: 58ec244c-ccd5-480d-8185-2c62273aeb1f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGDCSPARAMMASK
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
req.iface: 
req.product: Windows 10 or later.
---

# RILMSGDCSPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGDCSPARAMMASK { 
  RIL_PARAM_MDCS_FLAGS,
  RIL_PARAM_MDCS_MSGCLASS,
  RIL_PARAM_MDCS_ALPHABET,
  RIL_PARAM_MDCS_INDICATION,
  RIL_PARAM_MDCS_LANGUAGE,
  RIL_PARAM_MDCS_ALL
} RILMSGDCSPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_MDCS_FLAGS"></a><a id="ril_param_mdcs_flags"></a><b>RIL_PARAM_MDCS_FLAGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_MDCS_MSGCLASS"></a><a id="ril_param_mdcs_msgclass"></a><b>RIL_PARAM_MDCS_MSGCLASS</b>

<dd></dd>

### -field <a id="RIL_PARAM_MDCS_ALPHABET"></a><a id="ril_param_mdcs_alphabet"></a><b>RIL_PARAM_MDCS_ALPHABET</b>

<dd></dd>

### -field <a id="RIL_PARAM_MDCS_INDICATION"></a><a id="ril_param_mdcs_indication"></a><b>RIL_PARAM_MDCS_INDICATION</b>

<dd></dd>

### -field <a id="RIL_PARAM_MDCS_LANGUAGE"></a><a id="ril_param_mdcs_language"></a><b>RIL_PARAM_MDCS_LANGUAGE</b>

<dd></dd>

### -field <a id="RIL_PARAM_MDCS_ALL"></a><a id="ril_param_mdcs_all"></a><b>RIL_PARAM_MDCS_ALL</b>

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