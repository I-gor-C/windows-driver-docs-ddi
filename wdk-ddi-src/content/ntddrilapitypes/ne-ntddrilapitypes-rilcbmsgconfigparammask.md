---
UID : NE:ntddrilapitypes.RILCBMSGCONFIGPARAMMASK
title : RILCBMSGCONFIGPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcbmsgconfigparammask.htm
old-project : netvista
ms.assetid : 86bbc3ef-c76c-4abd-bfcb-56c804c12b1f
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCBMSGCONFIGPARAMMASK, RILCBMSGCONFIGPARAMMASK
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
req.alt-api : RILCBMSGCONFIGPARAMMASK
req.alt-loc : ntddrilapitypes.h
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
req.typenames : RILCBMSGCONFIGPARAMMASK
---

# RILCBMSGCONFIGPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCBMSGCONFIGPARAMMASK { 
  RIL_PARAM_CBMC_GWLINFO,
  RIL_PARAM_CBMC_CDMASIZE,
  RIL_PARAM_CBMC_CDMAINFO,
  RIL_PARAM_CBMC_ALL
} RILCBMSGCONFIGPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CBMC_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CBMC_CDMAINFO</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CBMC_CDMASIZE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CBMC_GWLINFO</td>
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