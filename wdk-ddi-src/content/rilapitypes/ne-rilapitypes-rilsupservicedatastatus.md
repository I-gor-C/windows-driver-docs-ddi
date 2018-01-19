---
UID : NE:rilapitypes.RILSUPSERVICEDATASTATUS
title : RILSUPSERVICEDATASTATUS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsupservicedatastatus_2.htm
old-project : netvista
ms.assetid : 9879db5b-25c1-451c-bb50-37e85cf1f5e5
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILSUPSERVICEDATASTATUS, RILSUPSERVICEDATASTATUS
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
req.alt-api : RILSUPSERVICEDATASTATUS
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
req.typenames : RILSUPSERVICEDATASTATUS
req.product : Windows 10 or later.
---

# RILSUPSERVICEDATASTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSUPSERVICEDATASTATUS { 
  RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED,
  RIL_SUPSVCDATASTATUS_TIMEOUT,
  RIL_SUPSVCDATASTATUS_ERROR,
  RIL_SUPSVCDATASTATUS_MAX
} RILSUPSERVICEDATASTATUS;
````

## Constants

<table>

<tr>
<td>RIL_SUPSVCDATASTATUS_ERROR</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCDATASTATUS_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCDATASTATUS_TIMEOUT</td>
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