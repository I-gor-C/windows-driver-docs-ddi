---
UID : NE:ksproxy.KSALLOCATORMODE
title : KSALLOCATORMODE
author : windows-driver-content
description : .
old-location : stream\ksallocatormode.htm
old-project : stream
ms.assetid : 2D02D43F-495E-45EE-B932-C8924ADF05DC
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSALLOCATORMODE, KSALLOCATORMODE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ksproxy.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSALLOCATORMODE
req.alt-loc : Ksproxy.h
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
req.typenames : KSALLOCATORMODE
---

# KSALLOCATORMODE Enumeration


## Syntax
````
typedef enum  { 
  KsAllocatorMode_User,
  KsAllocatorMode_Kernel
} KSALLOCATORMODE;
````

## Constants

<table>

<tr>
<td>KsAllocatorMode_Kernel</td>
<td></td>
</tr>

<tr>
<td>KsAllocatorMode_User</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |