---
UID: NE.ntddrilapitypes.RILIMSSSTATUSPARAMMASK
title: RILIMSSSTATUSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssstatusparammask.htm
ms.assetid: bc31d252-eb1d-492c-ae2b-c6c7a8509685
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
req.alt-api: RILIMSSSTATUSPARAMMASK
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

# RILIMSSSTATUSPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILIMSSSTATUSPARAMMASK { 
  RIL_PARAM_IMSSTATUS_HUICCAPP,
  RIL_PARAM_IMSSTATUS_AVAILABLESERVICES,
  RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT,
  RIL_PARAM_IMSSTATUS_SERVINGDOMAIN,
  RIL_PARAM_IMSSTATUS_SYSTEMTYPE,
  RIL_PARAM_IMSSTATUS_ALL
} RILIMSSSTATUSPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_IMSSTATUS_HUICCAPP"></a><a id="ril_param_imsstatus_huiccapp"></a><b>RIL_PARAM_IMSSTATUS_HUICCAPP</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSSTATUS_AVAILABLESERVICES"></a><a id="ril_param_imsstatus_availableservices"></a><b>RIL_PARAM_IMSSTATUS_AVAILABLESERVICES</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT"></a><a id="ril_param_imsstatus_smssupportedformat"></a><b>RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSSTATUS_SERVINGDOMAIN"></a><a id="ril_param_imsstatus_servingdomain"></a><b>RIL_PARAM_IMSSTATUS_SERVINGDOMAIN</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSSTATUS_SYSTEMTYPE"></a><a id="ril_param_imsstatus_systemtype"></a><b>RIL_PARAM_IMSSTATUS_SYSTEMTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSSTATUS_ALL"></a><a id="ril_param_imsstatus_all"></a><b>RIL_PARAM_IMSSTATUS_ALL</b>

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