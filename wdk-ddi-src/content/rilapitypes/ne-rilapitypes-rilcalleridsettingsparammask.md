---
UID : NE:rilapitypes.RILCALLERIDSETTINGSPARAMMASK
title : RILCALLERIDSETTINGSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcalleridsettingsparammask_2.htm
old-project : netvista
ms.assetid : 579165ca-94e7-433c-91c6-3112c4b75f64
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLERIDSETTINGSPARAMMASK, RILCALLERIDSETTINGSPARAMMASK
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILCALLERIDSETTINGSPARAMMASK
req.alt-loc : rilapitypes.h
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
req.typenames : RILCALLERIDSETTINGSPARAMMASK
req.product : Windows 10 or later.
---

# RILCALLERIDSETTINGSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLERIDSETTINGSPARAMMASK { 
  RIL_PARAM_CIDS_PROVISIONING,
  RIL_PARAM_CIDS_STATUS,
  RIL_PARAM_CIDS_ALL
} RILCALLERIDSETTINGSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CIDS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CIDS_PROVISIONING</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CIDS_STATUS</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |