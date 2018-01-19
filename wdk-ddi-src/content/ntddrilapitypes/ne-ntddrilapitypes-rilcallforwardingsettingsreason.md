---
UID : NE:ntddrilapitypes.RILCALLFORWARDINGSETTINGSREASON
title : RILCALLFORWARDINGSETTINGSREASON
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallforwardingsettingsreason.htm
old-project : netvista
ms.assetid : d1c39f60-15fb-450d-b879-fb5d236fcf45
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLFORWARDINGSETTINGSREASON, RILCALLFORWARDINGSETTINGSREASON
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
req.alt-api : RILCALLFORWARDINGSETTINGSREASON
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
req.typenames : RILCALLFORWARDINGSETTINGSREASON
---

# RILCALLFORWARDINGSETTINGSREASON Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLFORWARDINGSETTINGSREASON { 
  RIL_FWDREASON_MOBILEBUSY,
  RIL_FWDREASON_NOREPLY,
  RIL_FWDREASON_UNREACHABLE,
  RIL_FWDREASON_ALLFORWARDING,
  RIL_FWDREASON_ALLCONDITIONAL,
  RIL_FWDREASON_MAX
} RILCALLFORWARDINGSETTINGSREASON;
````

## Constants

<table>

<tr>
<td>RIL_FWDREASON_ALLCONDITIONAL</td>
<td></td>
</tr>

<tr>
<td>RIL_FWDREASON_ALLFORWARDING</td>
<td></td>
</tr>

<tr>
<td>RIL_FWDREASON_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_FWDREASON_MOBILEBUSY</td>
<td></td>
</tr>

<tr>
<td>RIL_FWDREASON_NOREPLY</td>
<td></td>
</tr>

<tr>
<td>RIL_FWDREASON_UNREACHABLE</td>
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