---
UID: NS:d3dkmddi._DXGKARG_CREATEDEVICE
title: "_DXGKARG_CREATEDEVICE"
author: windows-driver-content
description: The DXGKARG_CREATEDEVICE structure describes a graphics context device.
old-location: display\dxgkarg_createdevice.htm
old-project: display
ms.assetid: 88d20349-4039-4a5d-a1fd-0488148c623d
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*INOUT_PDXGKARG_CREATEDEVICE, DXGKARG_CREATEDEVICE, DXGKARG_CREATEDEVICE structure [Display Devices], DmStructs_76bb50f9-b0d8-415c-b183-ad780ebcabc6.xml, _DXGKARG_CREATEDEVICE, d3dkmddi/DXGKARG_CREATEDEVICE, display.dxgkarg_createdevice"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGKARG_CREATEDEVICE
product:
- Windows
targetos: Windows
req.typenames: DXGKARG_CREATEDEVICE
---

# _DXGKARG_CREATEDEVICE structure
The DXGKARG_CREATEDEVICE structure describes a graphics context device.

## Syntax
```
typedef struct _DXGKARG_CREATEDEVICE {
  HANDLE hDevice;
  union {
    DXGK_CREATEDEVICEFLAGS Flags;
    DXGK_DEVICEINFO        *pInfo;
  };
  ULONG  Pasid;
  HANDLE hKmdProcess;
} DXGKARG_CREATEDEVICE;
```

## Members


`hDevice`

A handle to the graphics context device. On input to the <a href="https://msdn.microsoft.com/a7027735-0ec4-4fad-81fb-1c3aca4ebf2d">DxgkDdiCreateDevice</a> function, <b>hDevice</b> specifies the handle that the driver should use when it calls back into the Microsoft DirectX graphics kernel subsystem. 

The driver generates a unique handle and passes it back to the DirectX graphics subsystem. On output from the <a href="https://msdn.microsoft.com/a7027735-0ec4-4fad-81fb-1c3aca4ebf2d">DxgkDdiCreateDevice</a> function, <b>hDevice</b> specifies the handle that the DirectX graphics subsystem should use in subsequent driver calls to identify the device.

`Pasid`

The owner process PASID for a support vector machine GPU.

Supported starting with Windows 10.

`hKmdProcess`

A handle to the corresponding kernel mode driver process object.

Supported starting with Windows 10.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561039">DXGK_CREATEDEVICEFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561047">DXGK_DEVICEINFO</a>



<a href="https://msdn.microsoft.com/a7027735-0ec4-4fad-81fb-1c3aca4ebf2d">DxgkDdiCreateDevice</a>