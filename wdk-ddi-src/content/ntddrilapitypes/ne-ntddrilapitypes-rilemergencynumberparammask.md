---
UID : NE:ntddrilapitypes.RILEMERGENCYNUMBERPARAMMASK
title : RILEMERGENCYNUMBERPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilemergencynumberparammask.htm
old-project : netvista
ms.assetid : e8365373-130b-485c-9117-89be6153be52
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_ENUM_ALL, ntddrilapitypes/RIL_PARAM_ENUM_ALL, RIL_PARAM_ENUM_NUMBER, netvista.rilemergencynumberparammask, ntddrilapitypes/RILEMERGENCYNUMBERPARAMMASK, RIL_PARAM_ENUM_UICC, RILEMERGENCYNUMBERPARAMMASK, ntddrilapitypes/RIL_PARAM_ENUM_UICC, RILEMERGENCYNUMBERPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_PARAM_ENUM_NUMBER, ntddrilapitypes/RIL_PARAM_ENUM_CATEGORY, RIL_PARAM_ENUM_CATEGORY
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
req.typenames : RILEMERGENCYNUMBERPARAMMASK
---

# RILEMERGENCYNUMBERPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILEMERGENCYNUMBERPARAMMASK { 
  RIL_PARAM_ENUM_UICC,
  RIL_PARAM_ENUM_CATEGORY,
  RIL_PARAM_ENUM_NUMBER,
  RIL_PARAM_ENUM_ALL
} RILEMERGENCYNUMBERPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_ENUM_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ENUM_CATEGORY</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ENUM_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ENUM_NUMBER</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ENUM_UICC</td>
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