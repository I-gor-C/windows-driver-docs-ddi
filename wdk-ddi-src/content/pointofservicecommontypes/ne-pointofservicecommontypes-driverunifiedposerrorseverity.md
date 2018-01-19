---
UID : NE:pointofservicecommontypes.DriverUnifiedPosErrorSeverity
title : DriverUnifiedPosErrorSeverity
author : windows-driver-content
description : This enumeration indicates the severity of the error.
old-location : pos\unifiedposerrorseverity.htm
old-project : pos
ms.assetid : a8c592fa-2736-49e4-8d4d-8729baef9c49
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : DriverUnifiedPosErrorSeverity, DriverUnifiedPosErrorSeverity
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : pointofservicecommontypes.h
req.include-header : Pointofservicecommontypes.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DriverUnifiedPosErrorSeverity
req.alt-loc : pointofservicecommontypes.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Called at PASSIVE_LEVEL.
req.typenames : DriverUnifiedPosErrorSeverity
---

# DriverUnifiedPosErrorSeverity Enumeration
This enumeration indicates the severity of the error.

## Syntax
````
typedef enum _DriverUnifiedPosErrorSeverity { 
  UnknownErrorSeverity  = 0,
  Warning               = 1,
  Recoverable           = 2,
  Unrecoverable         = 3,
   AssistanceRequired   = 4,
  Fatal                 = 5
} DriverUnifiedPosErrorSeverity;
````

## Constants

<table>

<tr>
<td>Fatal</td>
<td>The error requires that the device be rebooted.</td>
</tr>

<tr>
<td>Recoverable</td>
<td>The device can recover from the error without closing the application or rebooting.</td>
</tr>

<tr>
<td>UnknownErrorSeverity</td>
<td>The severity of the error is not known.</td>
</tr>

<tr>
<td>Unrecoverable</td>
<td>The device is still working, but it must close the application to recover from the error.</td>
</tr>

<tr>
<td>Warning</td>
<td>The error or warning is informational.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pointofservicecommontypes.h (include Pointofservicecommontypes.h) |