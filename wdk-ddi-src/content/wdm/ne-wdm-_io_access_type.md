---
UID : NE:wdm._IO_ACCESS_TYPE
title : "_IO_ACCESS_TYPE"
author : windows-driver-content
description : Defines the access rights for Scheduled File I/O (SFIO).
old-location : kernel\io_access_type.htm
old-project : kernel
ms.assetid : 9ABFF1E8-50B8-4B59-964D-BA79AB63BFCE
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : wdm/IO_ACCESS_TYPE, _IO_ACCESS_TYPE, IO_ACCESS_TYPE, ReadAccess, WriteAccess, wdm/WriteAccess, wdm/ReadAccess, ModifyAccess, wdm/ModifyAccess, kernel.io_access_type, IO_ACCESS_TYPE enumeration [Kernel-Mode Driver Architecture]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wdm.h
req.include-header : Wdm.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : IO_ACCESS_TYPE
req.product : Windows 10 or later.
---

# _IO_ACCESS_TYPE Enumeration
Defines the access rights for Scheduled File I/O (SFIO).

## Syntax
````
typedef enum _IO_ACCESS_TYPE { 
  ReadAccess,
  WriteAccess,
  ModifyAccess
} IO_ACCESS_TYPE;
````

## Constants

<table>

<tr>
<td>ModifyAccess</td>
<td>Indicates that the input/output will be comprised of reads and writes.</td>
</tr>

<tr>
<td>ReadAccess</td>
<td>Indicates that the input/output will be comprised solely of reads.</td>
</tr>

<tr>
<td>WriteAccess</td>
<td>Indicates that the input/output will be comprised solely of writes.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h) |