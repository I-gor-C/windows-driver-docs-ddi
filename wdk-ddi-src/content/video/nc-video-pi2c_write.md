---
UID: NC:video.PI2C_WRITE
title: PI2C_WRITE
author: windows-driver-content
description: The I2CWrite function writes data over the I2C channel.
old-location: display\i2cwrite.htm
old-project: display
ms.assetid: 5aaebf38-bc09-4fb5-969e-7b456773d5ac
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: I2CWrite, I2CWrite callback function [Display Devices], PI2C_WRITE, VideoPort_Functions_3e35f4d8-7c13-4c2c-b0e4-c518bc63e6f6.xml, display.i2cwrite, video/I2CWrite
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	video.h
api_name:
-	I2CWrite
product: Windows
targetos: Windows
req.typenames: VHF_CONFIG, *PVHF_CONFIG
req.product: Windows 10 or later.
---


# PI2C_WRITE callback function
The <i>I2CWrite</i> function writes data over the <a href="https://msdn.microsoft.com/5a140cc0-ecc5-46ff-be3f-3c92f0f67dca">I2C</a> channel.

## Syntax

```
PI2C_WRITE Pi2cWrite;

BOOLEAN Pi2cWrite(
  IN PVOID HwDeviceExtension,
  IN PI2C_CALLBACKS I2CCallbacks,
  IN PUCHAR Buffer,
  IN ULONG Length
)
{...}
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's per-adapter device extension.

`I2CCallbacks`

Pointer to an <a href="..\video\ns-video-_i2c_callbacks.md">I2C_CALLBACKS</a> structure, containing pointers to miniport driver-defined functions that read and write data and clock lines.

`Buffer`

Pointer to the data to be written.

`Length`

Specifies the number of bytes to be written.


## Return Value

<i>I2CWrite</i> returns <b>TRUE</b> if the data was successfully written, and <b>FALSE</b> otherwise.

## Remarks

The video port implements this function, which can be accessed through a pointer in the <a href="..\video\ns-video-_video_port_i2c_interface.md">VIDEO_PORT_I2C_INTERFACE</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 2000 and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | video.h (include Video.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\video\ns-video-_video_port_i2c_interface.md">VIDEO_PORT_I2C_INTERFACE</a>