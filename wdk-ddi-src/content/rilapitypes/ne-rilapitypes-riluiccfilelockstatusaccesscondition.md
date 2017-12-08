---
UID: NE.rilapitypes.RILUICCFILELOCKSTATUSACCESSCONDITION
title: RILUICCFILELOCKSTATUSACCESSCONDITION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccfilelockstatusaccesscondition_2.htm
old-project: netvista
ms.assetid: f8bc0e66-1868-4e96-80d4-e541f6959eac
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILUICCFILELOCKSTATUSACCESSCONDITION, RILUICCFILELOCKSTATUSACCESSCONDITION
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
req.product: Windows 10 or later.
---

# RILUICCFILELOCKSTATUSACCESSCONDITION enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 


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

### -field RIL_UICCFILEACCESSCONDITION_PIN1


### -field RIL_UICCFILEACCESSCONDITION_PIN2


### -field RIL_UICCFILEACCESSCONDITION_RFU3


### -field RIL_UICCFILEACCESSCONDITION_RFU4


### -field RIL_UICCFILEACCESSCONDITION_ADM5


### -field RIL_UICCFILEACCESSCONDITION_ADM6


### -field RIL_UICCFILEACCESSCONDITION_NEV


### -field RIL_UICCFILEACCESSCONDITION_MAX


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>