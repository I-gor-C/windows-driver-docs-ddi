---
UID: NE.rilapitypes.RILMSGMWISUMMARYLISTPARAMMASK
title: RILMSGMWISUMMARYLISTPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgmwisummarylistparammask_2.htm
old-project: netvista
ms.assetid: cc4253ab-d0f8-4c73-a538-29cac8c0df31
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
req.alt-api: RILMSGMWISUMMARYLISTPARAMMASK
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

# RILMSGMWISUMMARYLISTPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGMWISUMMARYLISTPARAMMASK { 
  RIL_PARAM_MWISUMMARY_REFNUM,
  RIL_PARAM_MWISUMMARY_ACCTADDR,
  RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS,
  RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS,
  RIL_PARAM_MWISUMMARY_SUMMARYITEMS,
  RIL_PARAM_MWISUMMARY_ALL
} RILMSGMWISUMMARYLISTPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_MWISUMMARY_REFNUM"></a><a id="ril_param_mwisummary_refnum"></a><b>RIL_PARAM_MWISUMMARY_REFNUM</b>

<dd></dd>

### -field <a id="RIL_PARAM_MWISUMMARY_ACCTADDR"></a><a id="ril_param_mwisummary_acctaddr"></a><b>RIL_PARAM_MWISUMMARY_ACCTADDR</b>

<dd></dd>

### -field <a id="RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS"></a><a id="ril_param_mwisummary_totalnumdetailitems"></a><b>RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS</b>

<dd></dd>

### -field <a id="RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS"></a><a id="ril_param_mwisummary_numsummaryitems"></a><b>RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS</b>

<dd></dd>

### -field <a id="RIL_PARAM_MWISUMMARY_SUMMARYITEMS"></a><a id="ril_param_mwisummary_summaryitems"></a><b>RIL_PARAM_MWISUMMARY_SUMMARYITEMS</b>

<dd></dd>

### -field <a id="RIL_PARAM_MWISUMMARY_ALL"></a><a id="ril_param_mwisummary_all"></a><b>RIL_PARAM_MWISUMMARY_ALL</b>

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