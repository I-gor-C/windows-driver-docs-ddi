---
UID : NE:usbscan._RAW_PIPE_TYPE
title : _RAW_PIPE_TYPE
author : windows-driver-content
description : The RAW_PIPE_TYPE data type is used to specify the type of a USB pipe.
old-location : image\raw_pipe_type.htm
old-project : image
ms.assetid : 6af4161c-7caa-4d80-8938-303380ee3058
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : _RAW_PIPE_TYPE, RAW_PIPE_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : usbscan.h
req.include-header : Usbscan.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RAW_PIPE_TYPE
req.alt-loc : usbscan.h
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
req.typenames : RAW_PIPE_TYPE
req.product : Windows 10 or later.
---

# _RAW_PIPE_TYPE Enumeration
The RAW_PIPE_TYPE data type is used to specify the type of a USB pipe. The values are defined as follows:

## Syntax
````
typedef enum _RAW_PIPE_TYPE { 
  USBSCAN_PIPE_CONTROL      = 0,
  USBSCAN_PIPE_ISOCHRONOUS  = 1,
  USBSCAN_PIPE_BULK         = 2,
  USBSCAN_PIPE_INTERRUPT    = 3
} RAW_PIPE_TYPE;
````

## Constants

<table>

<tr>
<td>USBSCAN_PIPE_BULK</td>
<td>Identifies a bulk IN or bulk OUT pipe.</td>
</tr>

<tr>
<td>USBSCAN_PIPE_CONTROL</td>
<td>Identifies the control pipe.</td>
</tr>

<tr>
<td>USBSCAN_PIPE_INTERRUPT</td>
<td>Identifies an interrupt pipe.</td>
</tr>

<tr>
<td>USBSCAN_PIPE_ISOCHRONOUS</td>
<td>Identifies an isochronous pipe.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | usbscan.h (include Usbscan.h) |