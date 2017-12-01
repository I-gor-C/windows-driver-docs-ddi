---
UID: NE.rilapitypes.RILUICCFILELOCKSTATUSACCESSCONDITION
title: RILUICCFILELOCKSTATUSACCESSCONDITION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccfilelockstatusaccesscondition_2.htm
old-project: netvista
ms.assetid: f8bc0e66-1868-4e96-80d4-e541f6959eac
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
req.alt-api: RILUICCFILELOCKSTATUSACCESSCONDITION
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

# RILUICCFILELOCKSTATUSACCESSCONDITION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUICCFILELOCKSTATUSACCESSCONDITION { 
  RIL_UICCFILEACCESSCONDITION_PIN1,
  RIL_UICCFILEACCESSCONDITION_PIN2,
  RIL_UICCFILEACCESSCONDITION_RFU3,
  RIL_UICCFILEACCESSCONDITION_RFU4,
  RIL_UICCFILEACCESSCONDITION_ADM5,
  RIL_UICCFILEACCESSCONDITION_ADM6,
  RIL_UICCFILEACCESSCONDITION_NEV,
  RIL_UICCFILEACCESSCONDITION_MAX
} RILUICCFILELOCKSTATUSACCESSCONDITION;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCFILEACCESSCONDITION_PIN1"></a><a id="ril_uiccfileaccesscondition_pin1"></a><b>RIL_UICCFILEACCESSCONDITION_PIN1</b>

<dd></dd>

### -field <a id="RIL_UICCFILEACCESSCONDITION_PIN2"></a><a id="ril_uiccfileaccesscondition_pin2"></a><b>RIL_UICCFILEACCESSCONDITION_PIN2</b>

<dd></dd>

### -field <a id="RIL_UICCFILEACCESSCONDITION_RFU3"></a><a id="ril_uiccfileaccesscondition_rfu3"></a><b>RIL_UICCFILEACCESSCONDITION_RFU3</b>

<dd></dd>

### -field <a id="RIL_UICCFILEACCESSCONDITION_RFU4"></a><a id="ril_uiccfileaccesscondition_rfu4"></a><b>RIL_UICCFILEACCESSCONDITION_RFU4</b>

<dd></dd>

### -field <a id="RIL_UICCFILEACCESSCONDITION_ADM5"></a><a id="ril_uiccfileaccesscondition_adm5"></a><b>RIL_UICCFILEACCESSCONDITION_ADM5</b>

<dd></dd>

### -field <a id="RIL_UICCFILEACCESSCONDITION_ADM6"></a><a id="ril_uiccfileaccesscondition_adm6"></a><b>RIL_UICCFILEACCESSCONDITION_ADM6</b>

<dd></dd>

### -field <a id="RIL_UICCFILEACCESSCONDITION_NEV"></a><a id="ril_uiccfileaccesscondition_nev"></a><b>RIL_UICCFILEACCESSCONDITION_NEV</b>

<dd></dd>

### -field <a id="RIL_UICCFILEACCESSCONDITION_MAX"></a><a id="ril_uiccfileaccesscondition_max"></a><b>RIL_UICCFILEACCESSCONDITION_MAX</b>

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