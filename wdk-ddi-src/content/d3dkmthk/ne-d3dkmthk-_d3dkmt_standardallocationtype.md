---
UID : NE:d3dkmthk._D3DKMT_STANDARDALLOCATIONTYPE
title : _D3DKMT_STANDARDALLOCATIONTYPE
author : windows-driver-content
description : Used to give information on the allocation type.
old-location : display\d3dkmt-standardallocationtype.htm
old-project : display
ms.assetid : 7ce6d148-bfe8-4040-a4c1-ccd22fd07307
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DKMT_STANDARDALLOCATIONTYPE, D3DKMT_STANDARDALLOCATIONTYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMT_STANDARDALLOCATIONTYPE
req.alt-loc : d3dkmthk.h
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
req.typenames : D3DKMT_STANDARDALLOCATIONTYPE
---

# _D3DKMT_STANDARDALLOCATIONTYPE Enumeration
Used to give information on the allocation type.

## Syntax
````
typedef enum _D3DKMT_STANDARDALLOCATIONTYPE { 
  D3DKMT_STANDARDALLOCATIONTYPE_EXISTINGHEAP  = 1
} D3DKMT_STANDARDALLOCATIONTYPE;
````

## Constants

<table>

<tr>
<td>D3DKMT_STANDARDALLOCATIONTYPE_EXISTINGHEAP</td>
<td>Indicates that the allocation type is an existing heap.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |