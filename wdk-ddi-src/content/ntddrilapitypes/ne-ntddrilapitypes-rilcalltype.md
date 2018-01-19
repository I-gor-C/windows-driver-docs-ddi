---
UID : NE:ntddrilapitypes.RILCALLTYPE
title : RILCALLTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcalltype.htm
old-project : netvista
ms.assetid : bd6b9e57-f50b-4743-9c51-066940aad200
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLTYPE, RILCALLTYPE
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
req.alt-api : RILCALLTYPE
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
req.typenames : RILCALLTYPE
---

# RILCALLTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLTYPE { 
  RIL_CALLTYPE_VOICE,
  RIL_CALLTYPE_DATA,
  RIL_CALLTYPE_FAX,
  RIL_CALLTYPE_PTT,
  RIL_CALLTYPE_VT,
  RIL_CALLTYPE_USSD,
  RIL_CALLTYPE_SUPSVC,
  RIL_CALLTYPE_IMS,
  RIL_CALLTYPE_MAX
} RILCALLTYPE;
````

## Constants

<table>

<tr>
<td>RIL_CALLTYPE_DATA</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_FAX</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_IMS</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_PTT</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_SUPSVC</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_USSD</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_VOICE</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLTYPE_VT</td>
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