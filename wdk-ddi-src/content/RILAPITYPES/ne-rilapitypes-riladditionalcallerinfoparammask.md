---
UID: NE.rilapitypes.RILADDITIONALCALLERINFOPARAMMASK
title: RILADDITIONALCALLERINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riladditionalcallerinfoparammask_2.htm
ms.assetid: 1de91e12-1f8c-48fa-85e4-c3cb061fce78
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
req.alt-api: RILADDITIONALCALLERINFOPARAMMASK
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

# RILADDITIONALCALLERINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILADDITIONALCALLERINFOPARAMMASK { 
  RIL_PARAM_ADDTLCI_CALLID,
  RIL_PARAM_ADDTLCI_CALLERINFOLENGTH,
  RIL_PARAM_ADDTLCI_CALLERINFO,
  RIL_PARAM_ADDTLCI_ALL
} RILADDITIONALCALLERINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_ADDTLCI_CALLID"></a><a id="ril_param_addtlci_callid"></a><b>RIL_PARAM_ADDTLCI_CALLID</b>

<dd></dd>

### -field <a id="RIL_PARAM_ADDTLCI_CALLERINFOLENGTH"></a><a id="ril_param_addtlci_callerinfolength"></a><b>RIL_PARAM_ADDTLCI_CALLERINFOLENGTH</b>

<dd></dd>

### -field <a id="RIL_PARAM_ADDTLCI_CALLERINFO"></a><a id="ril_param_addtlci_callerinfo"></a><b>RIL_PARAM_ADDTLCI_CALLERINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_ADDTLCI_ALL"></a><a id="ril_param_addtlci_all"></a><b>RIL_PARAM_ADDTLCI_ALL</b>

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