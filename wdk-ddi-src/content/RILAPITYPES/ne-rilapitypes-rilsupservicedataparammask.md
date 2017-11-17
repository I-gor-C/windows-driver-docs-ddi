---
UID: NE.rilapitypes.RILSUPSERVICEDATAPARAMMASK
title: RILSUPSERVICEDATAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupservicedataparammask_2.htm
ms.assetid: 65901068-d45e-4c3a-b1ee-340427506c7f
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
req.alt-api: RILSUPSERVICEDATAPARAMMASK
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

# RILSUPSERVICEDATAPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>