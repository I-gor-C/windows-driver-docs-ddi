---
UID : NE:ksproxy.KSIOOPERATION
title : KSIOOPERATION
author : windows-driver-content
description : .
old-location : stream\ksiooperation.htm
old-project : stream
ms.assetid : 993909CB-B00C-40C0-ADDA-DB4389D9812E
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSIOOPERATION, KSIOOPERATION
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
req.alt-api : KSIOOPERATION
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
req.typenames : KSIOOPERATION
---

# KSIOOPERATION Enumeration


## Syntax
````
typedef enum  { 
  KsIoOperation_Write,
  KsIoOperation_Read
} KSIOOPERATION;
````

## Constants

<table>

<tr>
<td>KsIoOperation_Read</td>
<td></td>
</tr>

<tr>
<td>KsIoOperation_Write</td>
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