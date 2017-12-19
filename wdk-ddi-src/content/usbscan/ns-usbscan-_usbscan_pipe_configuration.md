---
UID: NS.USBSCAN._USBSCAN_PIPE_CONFIGURATION
title: _USBSCAN_PIPE_CONFIGURATION
author: windows-driver-content
description: The USBSCAN_PIPE_CONFIGURATION structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_PIPE_CONFIGURATION.
old-location: image\usbscan_pipe_configuration.htm
old-project: Image
ms.assetid: c9b0247b-1444-46c9-a430-897594f8d223
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _USBSCAN_PIPE_CONFIGURATION, PUSBSCAN_PIPE_CONFIGURATION, *PUSBSCAN_PIPE_CONFIGURATION, USBSCAN_PIPE_CONFIGURATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbscan.h
req.include-header: Usbscan.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBSCAN_PIPE_CONFIGURATION
req.alt-loc: usbscan.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# _USBSCAN_PIPE_CONFIGURATION structure



## -description
The USBSCAN_PIPE_CONFIGURATION structure is used as a parameter to <a href="base.deviceiocontrol">DeviceIoControl</a>, when the specified I/O control code is <a href="..\usbscan\ni-usbscan-ioctl_get_pipe_configuration.md">IOCTL_GET_PIPE_CONFIGURATION</a>.



## -syntax

````
typedef struct _USBSCAN_PIPE_CONFIGURATION {
  ULONG                    NumberOfPipes;
  USBSCAN_PIPE_INFORMATION PipeInfo[MAX_NUM_PIPES];
} USBSCAN_PIPE_CONFIGURATION, *PUSBSCAN_PIPE_CONFIGURATION;
````


## -struct-fields

### -field NumberOfPipes

The number of transfer pipes supported for the device.


### -field PipeInfo

Pointer to a <b>NumberOfPipes</b>-sized array of <a href="image.usbscan_pipe_information">USBSCAN_PIPE_INFORMATION</a> structures.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Usbscan.h (include Usbscan.h)</dt>
</dl>
</td>
</tr>
</table>