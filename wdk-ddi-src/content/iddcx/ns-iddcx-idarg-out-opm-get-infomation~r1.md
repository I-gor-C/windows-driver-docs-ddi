---
UID: NS.iddcx.IDARG_OUT_OPM_GET_INFOMATION~r1
title: IDARG_OUT_OPM_GET_INFOMATION
author: windows-driver-content
description: Gives the OPM information that was requested.
old-location: display\idarg_out_opm_get_infomation.htm
old-project: display
ms.assetid: 7c51b228-480d-4e19-aa70-4fcc44ffae16
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_OUT_OPM_GET_INFOMATION,
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
req.alt-api: IDARG_OUT_OPM_GET_INFOMATION
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

# IDARG_OUT_OPM_GET_INFOMATION structure



## -description
<p>
                 Gives the OPM information that was requested.
             </p>


## -syntax

````
typedef struct IDARG_OUT_OPM_GET_INFOMATION {
  IDDCX_OPM_REQUESTED_INFORMATION RequestedInformation;
} IDARG_OUT_OPM_GET_INFOMATION, *IDARG_OUT_OPM_GET_INFOMATION;
````


## -struct-fields
<dl>

### -field <b>RequestedInformation</b>

<dd>
<p>
                      [out] The OPM information that was requested.
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