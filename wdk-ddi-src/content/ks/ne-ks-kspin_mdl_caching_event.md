---
UID : NE:ks.KSPIN_MDL_CACHING_EVENT
title : KSPIN_MDL_CACHING_EVENT
author : windows-driver-content
description : This enumeration is used internally by the operating system.
old-location : stream\kspin_mdl_caching_event.htm
old-project : stream
ms.assetid : 74A7C2C8-F12B-4753-8E1F-C425B0B56788
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSPIN_MDL_CACHING_EVENT, KSPIN_MDL_CACHING_EVENT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ks.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSPIN_MDL_CACHING_EVENT
req.alt-loc : ks.h
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
req.typenames : KSPIN_MDL_CACHING_EVENT
---

# KSPIN_MDL_CACHING_EVENT Enumeration
This enumeration is used internally by the operating system.

## Syntax
````
typedef enum  { 
  KSPIN_MDL_CACHING_NOTIFY_CLEANUP,
  KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT,
  KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT,
  KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE
} KSPIN_MDL_CACHING_EVENT;
````

## Constants

<table>

<tr>
<td>KSPIN_MDL_CACHING_NOTIFY_ADDSAMPLE</td>
<td>This value is used internally by the operating system.</td>
</tr>

<tr>
<td>KSPIN_MDL_CACHING_NOTIFY_CLEANALL_NOWAIT</td>
<td>This value is used internally by the operating system.</td>
</tr>

<tr>
<td>KSPIN_MDL_CACHING_NOTIFY_CLEANALL_WAIT</td>
<td>This value is used internally by the operating system.</td>
</tr>

<tr>
<td>KSPIN_MDL_CACHING_NOTIFY_CLEANUP</td>
<td>This value is used internally by the operating system.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h |