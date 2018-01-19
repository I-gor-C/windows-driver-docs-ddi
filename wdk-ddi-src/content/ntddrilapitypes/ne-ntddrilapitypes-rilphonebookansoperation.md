---
UID : NE:ntddrilapitypes.RILPHONEBOOKANSOPERATION
title : RILPHONEBOOKANSOPERATION
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilphonebookansoperation.htm
old-project : netvista
ms.assetid : 29dcc5c0-0b07-49d7-b2ab-bdac7333baf7
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILPHONEBOOKANSOPERATION, RILPHONEBOOKANSOPERATION
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
req.alt-api : RILPHONEBOOKANSOPERATION
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
req.typenames : RILPHONEBOOKANSOPERATION
---

# RILPHONEBOOKANSOPERATION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPHONEBOOKANSOPERATION { 
  RIL_PHONEBOOK_ANSMODIFIED,
  RIL_PHONEBOOK_ANSDELETED,
  RIL_PHONEBOOK_MAX
} RILPHONEBOOKANSOPERATION;
````

## Constants

<table>

<tr>
<td>RIL_PHONEBOOK_ANSDELETED</td>
<td></td>
</tr>

<tr>
<td>RIL_PHONEBOOK_ANSMODIFIED</td>
<td></td>
</tr>

<tr>
<td>RIL_PHONEBOOK_MAX</td>
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