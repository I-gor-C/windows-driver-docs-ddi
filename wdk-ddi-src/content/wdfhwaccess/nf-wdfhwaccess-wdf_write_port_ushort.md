---
UID : NF:wdfhwaccess.WDF_WRITE_PORT_USHORT
title : WDF_WRITE_PORT_USHORT function
author : windows-driver-content
description : The WDF_WRITE_PORT_USHORT function writes a USHORT value to the specified port address.
old-location : wdf\wdf_write_port_ushort.htm
old-project : wdf
ms.assetid : 310C55F8-E62C-4ABE-997E-E551CA6C4BB2
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WDF_WRITE_PORT_USHORT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfhwaccess.h
req.include-header : 
req.target-type : Universal
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 2.0
req.alt-api : WDF_WRITE_PORT_USHORT
req.alt-loc : Wdfhwaccess.h
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
req.typenames : WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS
req.product : Windows 10 or later.
---


# WDF_WRITE_PORT_USHORT function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_WRITE_PORT_USHORT</b> function writes a USHORT value to the specified port address.

## Syntax

````
void WDF_WRITE_PORT_USHORT(
  _In_ WDFDEVICE Device,
  _In_ PUSHORT   Port,
  _In_ USHORT    Value
);
````

## Parameters

`Device`

A handle to a framework device object.

`Port`

A pointer to the port, which must be a mapped memory range in I/O space.

`Value`

Specifies a USHORT value to be written to the port.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfhwaccess.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |