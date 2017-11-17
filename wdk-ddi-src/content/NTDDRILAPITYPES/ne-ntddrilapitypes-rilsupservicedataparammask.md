---
UID: NE.ntddrilapitypes.RILSUPSERVICEDATAPARAMMASK
title: RILSUPSERVICEDATAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupservicedataparammask.htm
ms.assetid: 2b0ff5a7-02b3-4a22-98da-d13825bc2f45
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
req.alt-api: RILSUPSERVICEDATAPARAMMASK
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

# RILSUPSERVICEDATAPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSUPSERVICEDATAPARAMMASK { 
  RIL_PARAM_SSDI_STATUS,
  RIL_PARAM_SSDI_SS_ERROR,
  RIL_PARAM_SSDI_CC_ERROR,
  RIL_PARAM_SSDI_VENDOR_ERROR,
  RIL_PARAM_SSDI_DATASIZE,
  RIL_PARAM_SSDI_DATA,
  RIL_PARAM_SSDI_ALL
} RILSUPSERVICEDATAPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_SSDI_STATUS"></a><a id="ril_param_ssdi_status"></a><b>RIL_PARAM_SSDI_STATUS</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSDI_SS_ERROR"></a><a id="ril_param_ssdi_ss_error"></a><b>RIL_PARAM_SSDI_SS_ERROR</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSDI_CC_ERROR"></a><a id="ril_param_ssdi_cc_error"></a><b>RIL_PARAM_SSDI_CC_ERROR</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSDI_VENDOR_ERROR"></a><a id="ril_param_ssdi_vendor_error"></a><b>RIL_PARAM_SSDI_VENDOR_ERROR</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSDI_DATASIZE"></a><a id="ril_param_ssdi_datasize"></a><b>RIL_PARAM_SSDI_DATASIZE</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSDI_DATA"></a><a id="ril_param_ssdi_data"></a><b>RIL_PARAM_SSDI_DATA</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSDI_ALL"></a><a id="ril_param_ssdi_all"></a><b>RIL_PARAM_SSDI_ALL</b>

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