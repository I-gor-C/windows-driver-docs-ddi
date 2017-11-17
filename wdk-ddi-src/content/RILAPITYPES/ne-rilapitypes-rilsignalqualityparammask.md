---
UID: NE.rilapitypes.RILSIGNALQUALITYPARAMMASK
title: RILSIGNALQUALITYPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsignalqualityparammask_2.htm
ms.assetid: be6c46bb-9c14-4daf-b76a-679d71269965
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
req.alt-api: RILSIGNALQUALITYPARAMMASK
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

# RILSIGNALQUALITYPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILSIGNALQUALITYPARAMMASK { 
  RIL_PARAM_SQ_SYSTEMTYPE,
  RIL_PARAM_SQ_NUMSIGNALBARS,
  RIL_PARAM_SQ_SIGNALSTRENGTH,
  RIL_PARAM_SQ_SNR,
  RIL_PARAM_SQ_ALL
} RILSIGNALQUALITYPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_SQ_SYSTEMTYPE"></a><a id="ril_param_sq_systemtype"></a><b>RIL_PARAM_SQ_SYSTEMTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_SQ_NUMSIGNALBARS"></a><a id="ril_param_sq_numsignalbars"></a><b>RIL_PARAM_SQ_NUMSIGNALBARS</b>

<dd></dd>

### -field <a id="RIL_PARAM_SQ_SIGNALSTRENGTH"></a><a id="ril_param_sq_signalstrength"></a><b>RIL_PARAM_SQ_SIGNALSTRENGTH</b>

<dd></dd>

### -field <a id="RIL_PARAM_SQ_SNR"></a><a id="ril_param_sq_snr"></a><b>RIL_PARAM_SQ_SNR</b>

<dd></dd>

### -field <a id="RIL_PARAM_SQ_ALL"></a><a id="ril_param_sq_all"></a><b>RIL_PARAM_SQ_ALL</b>

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