---
UID: NE.rilapitypes.RILUICCCARDINFOPARAMMASK
title: RILUICCCARDINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicccardinfoparammask_2.htm
ms.assetid: f27c7f54-f939-4e9b-a27c-b0137fbb7cec
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
req.alt-api: RILUICCCARDINFOPARAMMASK
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

# RILUICCCARDINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUICCCARDINFOPARAMMASK { 
  RIL_PARAM_CARDINFO_ICCID,
  RIL_PARAM_CARDINFO_NUMAPPS,
  RIL_PARAM_CARDINFO_APPINFO,
  RIL_PARAM_CARDINFO_ALL
} RILUICCCARDINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_CARDINFO_ICCID"></a><a id="ril_param_cardinfo_iccid"></a><b>RIL_PARAM_CARDINFO_ICCID</b>

<dd></dd>

### -field <a id="RIL_PARAM_CARDINFO_NUMAPPS"></a><a id="ril_param_cardinfo_numapps"></a><b>RIL_PARAM_CARDINFO_NUMAPPS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CARDINFO_APPINFO"></a><a id="ril_param_cardinfo_appinfo"></a><b>RIL_PARAM_CARDINFO_APPINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_CARDINFO_ALL"></a><a id="ril_param_cardinfo_all"></a><b>RIL_PARAM_CARDINFO_ALL</b>

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