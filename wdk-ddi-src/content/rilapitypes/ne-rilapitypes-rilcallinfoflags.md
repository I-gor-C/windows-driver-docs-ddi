---
UID : NE:rilapitypes.RILCALLINFOFLAGS
title : RILCALLINFOFLAGS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallinfoflags_2.htm
old-project : netvista
ms.assetid : 7b701e86-ee0b-4a46-a6bf-4a4fe18c371f
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLINFOFLAGS, RILCALLINFOFLAGS
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
req.alt-api : RILCALLINFOFLAGS
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
req.typenames : RILCALLINFOFLAGS
req.product : Windows 10 or later.
---

# RILCALLINFOFLAGS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLINFOFLAGS { 
  RILCALLINFO_FLAG_ALIENCALL,
  RILCALLINFO_FLAG_EMERGENCYCALL
} RILCALLINFOFLAGS;
````

## Constants

<table>

<tr>
<td>RILCALLINFO_FLAG_ALIENCALL</td>
<td></td>
</tr>

<tr>
<td>RILCALLINFO_FLAG_EMERGENCYCALL</td>
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