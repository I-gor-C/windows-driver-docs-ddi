---
UID : NF:wdfhwaccess.WDF_WRITE_PORT_BUFFER_ULONG
title : WDF_WRITE_PORT_BUFFER_ULONG function
author : windows-driver-content
description : The WDF_WRITE_PORT_BUFFER_ULONG function writes a number of ULONG values from a buffer to the specified port address.
old-location : wdf\wdf_write_port_buffer_ulong.htm
old-project : wdf
ms.assetid : 4FBBC349-B6D0-4F99-AF34-FA237199431E
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WDF_WRITE_PORT_BUFFER_ULONG
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
req.alt-api : WDF_WRITE_PORT_BUFFER_ULONG
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


# WDF_WRITE_PORT_BUFFER_ULONG function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_WRITE_PORT_BUFFER_ULONG</b> function writes a number of ULONG values from a buffer to the specified port address.

## Syntax

````
void WDF_WRITE_PORT_BUFFER_ULONG(
  _In_ WDFDEVICE Device,
  _In_ PULONG    Port,
  _In_ PULONG    Buffer,
  _In_ ULONG     Count 
);
````

## Parameters

`Device`

A handle to a framework device object.

`Port`

A pointer to the port, which must be a mapped memory range in I/O space.

`Buffer`

A pointer to a buffer from which an array of ULONG values is to be written.

`Count`

Specifies the number of ULONG values to be written to the buffer.


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