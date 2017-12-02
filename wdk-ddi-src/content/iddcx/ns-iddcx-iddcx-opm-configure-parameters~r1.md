---
UID: NS.iddcx.IDDCX_OPM_CONFIGURE_PARAMETERS~r1
title: IDDCX_OPM_CONFIGURE_PARAMETERS
author: windows-driver-content
description: Gives information about the OPM configure parameters.
old-location: display\iddcx_opm_configure_parameters.htm
old-project: display
ms.assetid: 88d8171f-8ed4-40af-8c05-7421895dca26
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_OPM_CONFIGURE_PARAMETERS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_OPM_CONFIGURE_PARAMETERS
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_OPM_CONFIGURE_PARAMETERS structure



## -description
<p>Gives information about the OPM configure parameters.</p>


## -syntax

````
typedef struct IDDCX_OPM_CONFIGURE_PARAMETERS {
  UINT                     Size;
  OPM_CONFIGURE_PARAMETERS ConfigParameters;
} IDDCX_OPM_CONFIGURE_PARAMETERS, *IDDCX_OPM_CONFIGURE_PARAMETERS;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>
                     Total size of the structure.
                 </p>
</dd>

### -field ConfigParameters

<dd>
<p>
                     Configuration parameters.
                 </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>