---
UID: NE.rilapitypes.RILUICCAPPDATACHANGEENUM
title: RILUICCAPPDATACHANGEENUM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccappdatachangeenum_2.htm
old-project: netvista
ms.assetid: 66d5596b-5f5b-46a6-9151-074c4713940f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILUICCAPPDATACHANGEENUM
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
req.iface: 
req.product: Windows 10 or later.
---

# RILUICCAPPDATACHANGEENUM enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>