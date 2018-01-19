---
UID : NE:rilapitypes.RILMESSAGESTATUS
title : RILMESSAGESTATUS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmessagestatus_2.htm
old-project : netvista
ms.assetid : 30ae1eff-447c-4f6f-8f6c-cd8bc657d32d
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMESSAGESTATUS, RILMESSAGESTATUS
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
req.alt-api : RILMESSAGESTATUS
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
req.typenames : RILMESSAGESTATUS
req.product : Windows 10 or later.
---

# RILMESSAGESTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMESSAGESTATUS { 
  RIL_MSGSTATUS_RECUNREAD,
  RIL_MSGSTATUS_RECREAD,
  RIL_MSGSTATUS_STOUNSENT,
  RIL_MSGSTATUS_STOSENT,
  RIL_MSGSTATUS_MAX
} RILMESSAGESTATUS;
````

## Constants

<table>

<tr>
<td>RIL_MSGSTATUS_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGSTATUS_RECREAD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGSTATUS_RECUNREAD</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGSTATUS_STOSENT</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGSTATUS_STOUNSENT</td>
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