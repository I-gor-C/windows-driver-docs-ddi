---
UID : NE:ntddrilapitypes.RILUICCAPPPERSOCHECKSTATUSPARAMMASK
title : RILUICCAPPPERSOCHECKSTATUSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluiccapppersocheckstatusparammask.htm
old-project : netvista
ms.assetid : 552c6ee9-47e7-4863-95bb-256057a99649
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_UAPCS_PERSOCHECKSTATE, netvista.riluiccapppersocheckstatusparammask, ntddrilapitypes/RIL_PARAM_UAPCS_PERSOFEATURE, ntddrilapitypes/RIL_PARAM_UAPCS_PERSOCHECKSTATE, RIL_PARAM_UAPCS_PERSOFEATURE, RILUICCAPPPERSOCHECKSTATUSPARAMMASK, ntddrilapitypes/RILUICCAPPPERSOCHECKSTATUSPARAMMASK, RILUICCAPPPERSOCHECKSTATUSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_UAPCS_ALL, ntddrilapitypes/RIL_PARAM_UAPCS_ALL
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddrilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILUICCAPPPERSOCHECKSTATUSPARAMMASK
---

# RILUICCAPPPERSOCHECKSTATUSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUICCAPPPERSOCHECKSTATUSPARAMMASK { 
  RIL_PARAM_UAPCS_PERSOFEATURE,
  RIL_PARAM_UAPCS_PERSOCHECKSTATE,
  RIL_PARAM_UAPCS_ALL
} RILUICCAPPPERSOCHECKSTATUSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_UAPCS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UAPCS_HUICCAPP</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UAPCS_PERSOCHECKSTATE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UAPCS_PERSOFEATURE</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |