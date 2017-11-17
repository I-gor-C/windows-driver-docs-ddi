---
UID: NE.rilapitypes.RILOPERATORNAMESPARAMMASK
title: RILOPERATORNAMESPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riloperatornamesparammask_2.htm
ms.assetid: d91e6e66-ff0f-4e36-ba1b-bd7f502739d9
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
req.alt-api: RILOPERATORNAMESPARAMMASK
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

# RILOPERATORNAMESPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILOPERATORNAMESPARAMMASK { 
  RIL_PARAM_ON_SHORTNAME,
  RIL_PARAM_ON_NUMNAME,
  RIL_PARAM_ON_COUNTRY_CODE,
  RIL_PARAM_ON_SYSTEMTYPE,
  RIL_PARAM_ON_ALL
} RILOPERATORNAMESPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_ON_SHORTNAME"></a><a id="ril_param_on_shortname"></a><b>RIL_PARAM_ON_SHORTNAME</b>

<dd></dd>

### -field <a id="RIL_PARAM_ON_NUMNAME"></a><a id="ril_param_on_numname"></a><b>RIL_PARAM_ON_NUMNAME</b>

<dd></dd>

### -field <a id="RIL_PARAM_ON_COUNTRY_CODE"></a><a id="ril_param_on_country_code"></a><b>RIL_PARAM_ON_COUNTRY_CODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_ON_SYSTEMTYPE"></a><a id="ril_param_on_systemtype"></a><b>RIL_PARAM_ON_SYSTEMTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_ON_ALL"></a><a id="ril_param_on_all"></a><b>RIL_PARAM_ON_ALL</b>

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