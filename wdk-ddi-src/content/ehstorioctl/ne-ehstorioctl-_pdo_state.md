---
UID : NE:ehstorioctl._PDO_STATE
title : _PDO_STATE
author : windows-driver-content
description : This enumeration describes the states of Physical Device Objects (PDOs).
old-location : storage\pdo_state.htm
old-project : storage
ms.assetid : 006e2cef-4e49-4819-bfce-d9bf5983643e
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _PDO_STATE, PDO_STATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ehstorioctl.h
req.include-header : EhStorIoctl.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PDO_STATE
req.alt-loc : EhStorIoctl.h
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
req.typenames : PDO_STATE
---

# _PDO_STATE Enumeration
This enumeration describes the states of Physical Device Objects (PDOs).

## Syntax
````
typedef enum _PDO_STATE { 
  PDO_STATE_UNDEFINED    = 0,
  PDO_STATE_STARTED      = 1,
  PDO_STATE_NOT_STARTED  = 2
} PDO_STATE;
````

## Constants

<table>

<tr>
<td>PDO_STATE_NOT_STARTED</td>
<td>This value indicates that the PDO is not started.</td>
</tr>

<tr>
<td>PDO_STATE_STARTED</td>
<td>This value indicates that the PDO is started.</td>
</tr>

<tr>
<td>PDO_STATE_UNDEFINED</td>
<td>This value indicates that the PDO state is undefined.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ehstorioctl.h (include EhStorIoctl.h) |