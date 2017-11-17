---
UID: NE.rilapitypes.RILCBMSGCONFIGPARAMMASK
title: RILCBMSGCONFIGPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcbmsgconfigparammask_2.htm
ms.assetid: ec2a26a0-4325-41d9-a6b4-5b9c2f22dd4e
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
req.alt-api: RILCBMSGCONFIGPARAMMASK
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

# RILCBMSGCONFIGPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>