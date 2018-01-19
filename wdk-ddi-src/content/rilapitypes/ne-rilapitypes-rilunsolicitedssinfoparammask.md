---
UID : NE:rilapitypes.RILUNSOLICITEDSSINFOPARAMMASK
title : RILUNSOLICITEDSSINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilunsolicitedssinfoparammask_2.htm
old-project : netvista
ms.assetid : 772b2ab3-6ce6-4303-8b1e-145e4e28ee44
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILUNSOLICITEDSSINFOPARAMMASK, RILUNSOLICITEDSSINFOPARAMMASK
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
req.alt-api : RILUNSOLICITEDSSINFOPARAMMASK
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
req.typenames : RILUNSOLICITEDSSINFOPARAMMASK
req.product : Windows 10 or later.
---

# RILUNSOLICITEDSSINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUNSOLICITEDSSINFOPARAMMASK { 
  RIL_PARAM_UNSSS_ID,
  RIL_PARAM_UNSSS_NOTIFICATIONCODE,
  RIL_PARAM_UNSSS_ADDRESS,
  RIL_PARAM_UNSSS_SUBADDR,
  RIL_PARAM_UNSSS_CUGINDEX,
  RIL_PARAM_UNSSS_HISTLENGTH,
  RIL_PARAM_UNSSS_HISTINFO,
  RIL_PARAM_UNSSS_ALL
} RILUNSOLICITEDSSINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_UNSSS_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UNSSS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UNSSS_CUGINDEX</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UNSSS_HISTINFO</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UNSSS_HISTLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UNSSS_ID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UNSSS_NOTIFICATIONCODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UNSSS_SUBADDR</td>
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