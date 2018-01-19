---
UID : NE:irb.IDE_DEVICE_TYPE
title : IDE_DEVICE_TYPE
author : windows-driver-content
description : The IDE_DEVICE_TYPE enumeration type indicates the device type.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location : storage\ide_device_type.htm
old-project : storage
ms.assetid : 6d94189f-d6ab-40ad-85e5-f4efe8c30ed8
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDE_DEVICE_TYPE, IDE_DEVICE_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : irb.h
req.include-header : Irb.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IDE_DEVICE_TYPE
req.alt-loc : irb.h
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
req.typenames : IDE_DEVICE_TYPE
---

# IDE_DEVICE_TYPE Enumeration
The IDE_DEVICE_TYPE enumeration type indicates the device type.

## Syntax
````
typedef enum  { 
  DeviceUnknown   = 0,
  DeviceIsAta     = 1,
  DeviceIsAtapi   = 2,
  DeviceNotExist  = 3
} IDE_DEVICE_TYPE;
````

## Constants

<table>

<tr>
<td>DeviceIsAta</td>
<td>Indicates an ATA device.</td>
</tr>

<tr>
<td>DeviceIsAtapi</td>
<td>Indicates an ATAPI device.</td>
</tr>

<tr>
<td>DeviceNotExist</td>
<td>Indicates that the device does not exist.</td>
</tr>

<tr>
<td>DeviceUnknown</td>
<td>Indicates that the device does not communicate by means of a known protocol.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | irb.h (include Irb.h) |