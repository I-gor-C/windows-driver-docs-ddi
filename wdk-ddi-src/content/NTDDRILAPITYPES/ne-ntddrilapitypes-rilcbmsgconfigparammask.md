---
UID: NE.ntddrilapitypes.RILCBMSGCONFIGPARAMMASK
title: RILCBMSGCONFIGPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcbmsgconfigparammask.htm
ms.assetid: 86bbc3ef-c76c-4abd-bfcb-56c804c12b1f
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
req.alt-api: RILCBMSGCONFIGPARAMMASK
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

# RILCBMSGCONFIGPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCBMSGCONFIGPARAMMASK { 
  RIL_PARAM_CBMC_GWLINFO,
  RIL_PARAM_CBMC_CDMASIZE,
  RIL_PARAM_CBMC_CDMAINFO,
  RIL_PARAM_CBMC_ALL
} RILCBMSGCONFIGPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_CBMC_GWLINFO"></a><a id="ril_param_cbmc_gwlinfo"></a><b>RIL_PARAM_CBMC_GWLINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_CBMC_CDMASIZE"></a><a id="ril_param_cbmc_cdmasize"></a><b>RIL_PARAM_CBMC_CDMASIZE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CBMC_CDMAINFO"></a><a id="ril_param_cbmc_cdmainfo"></a><b>RIL_PARAM_CBMC_CDMAINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_CBMC_ALL"></a><a id="ril_param_cbmc_all"></a><b>RIL_PARAM_CBMC_ALL</b>

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