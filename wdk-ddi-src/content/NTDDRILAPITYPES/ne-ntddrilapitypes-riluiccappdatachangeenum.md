---
UID: NE.ntddrilapitypes.RILUICCAPPDATACHANGEENUM
title: RILUICCAPPDATACHANGEENUM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccappdatachangeenum.htm
ms.assetid: 6960080f-03dc-4c5f-8cd8-b96d030f2bd3
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
req.alt-api: RILUICCAPPDATACHANGEENUM
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

# RILUICCAPPDATACHANGEENUM enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILUICCAPPDATACHANGEENUM { 
  RIL_UICCAPP_DATACHANGE_MBDN,
  RIL_UICCAPP_DATACHANGE_EF_CSP_PLMN_UNSET,
  RIL_UICCAPP_DATACHANGE_EF_CSP_PLMN_SET,
  RIL_UICCAPP_DATACHANGE_ESNME,
  RIL_UICCAPP_DATACHANGE_MAX
} RILUICCAPPDATACHANGEENUM;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCAPP_DATACHANGE_MBDN"></a><a id="ril_uiccapp_datachange_mbdn"></a><b>RIL_UICCAPP_DATACHANGE_MBDN</b>

<dd></dd>

### -field <a id="RIL_UICCAPP_DATACHANGE_EF_CSP_PLMN_UNSET"></a><a id="ril_uiccapp_datachange_ef_csp_plmn_unset"></a><b>RIL_UICCAPP_DATACHANGE_EF_CSP_PLMN_UNSET</b>

<dd></dd>

### -field <a id="RIL_UICCAPP_DATACHANGE_EF_CSP_PLMN_SET"></a><a id="ril_uiccapp_datachange_ef_csp_plmn_set"></a><b>RIL_UICCAPP_DATACHANGE_EF_CSP_PLMN_SET</b>

<dd></dd>

### -field <a id="RIL_UICCAPP_DATACHANGE_ESNME"></a><a id="ril_uiccapp_datachange_esnme"></a><b>RIL_UICCAPP_DATACHANGE_ESNME</b>

<dd></dd>

### -field <a id="RIL_UICCAPP_DATACHANGE_MAX"></a><a id="ril_uiccapp_datachange_max"></a><b>RIL_UICCAPP_DATACHANGE_MAX</b>

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