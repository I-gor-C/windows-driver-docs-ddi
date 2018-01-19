---
UID : NE:rilapitypes.RILGETPREFERENCEDOPERATORLISTFORMAT
title : RILGETPREFERENCEDOPERATORLISTFORMAT
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgetpreferencedoperatorlistformat_2.htm
old-project : netvista
ms.assetid : 1193174e-9247-4854-94d8-7404b2b15e5c
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILGETPREFERENCEDOPERATORLISTFORMAT, RILGETPREFERENCEDOPERATORLISTFORMAT
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
req.alt-api : RILGETPREFERENCEDOPERATORLISTFORMAT
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
req.typenames : RILGETPREFERENCEDOPERATORLISTFORMAT
req.product : Windows 10 or later.
---

# RILGETPREFERENCEDOPERATORLISTFORMAT Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILGETPREFERENCEDOPERATORLISTFORMAT { 
  RIL_OPFORMAT_SHORT,
  RIL_OPFORMAT_NUM,
  RIL_OPFORMAT_MAX
} RILGETPREFERENCEDOPERATORLISTFORMAT;
````

## Constants

<table>

<tr>
<td>RIL_OPFORMAT_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_OPFORMAT_NUM</td>
<td></td>
</tr>

<tr>
<td>RIL_OPFORMAT_SHORT</td>
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