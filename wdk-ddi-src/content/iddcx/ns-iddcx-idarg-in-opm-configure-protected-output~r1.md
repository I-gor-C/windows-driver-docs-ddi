---
UID: NS.iddcx.IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT~r1
title: IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT
author: windows-driver-content
description: Gives information about the buffer that the driver will copy configuration parameters to.
old-location: display\idarg_in_opm_configure_protected_output.htm
old-project: display
ms.assetid: 523b904c-c833-40f2-8173-7ec1c6687b26
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT,
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
req.alt-api: IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT
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

# IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT structure



## -description
<p>
                 Gives information about the buffer that the driver will copy configuration parameters to.
             </p>


## -syntax

````
typedef struct IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT {
  IDDCX_OPM_CONFIGURE_PARAMETERS                           ConfigParameters;
  UINT                                                     AdditionalParametersSizeInBytes;
  _Field_size_full_(AdditionalParametersSizeInBytes) PVOID pAdditionalParameters;
} IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT, *IDARG_IN_OPM_CONFIGURE_PROTECTED_OUTPUT;
````


## -struct-fields
<dl>

### -field <b>ConfigParameters</b>

<dd>
<p>
                     [in] Configuration parameters
                 </p>
</dd>

### -field <b>AdditionalParametersSizeInBytes</b>

<dd>
<p>
                     [in] Size of additional parameter buffer
                 </p>
</dd>

### -field <b>pAdditionalParameters</b>

<dd>
<p>
                     [in] A pointer to a buffer that the driver copies the configuration info to.
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