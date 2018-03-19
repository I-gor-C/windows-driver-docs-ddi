---
UID: NS:pepfx._PEP_REGISTER_DEBUGGER
title: "_PEP_REGISTER_DEBUGGER"
author: windows-driver-content
description: The PEP_REGISTER_DEBUGGER structure identifies a registered device that is a core system resource that provides debugger transport.
old-location: kernel\pep_register_debugger.htm
old-project: kernel
ms.assetid: 3B0240AB-4599-4F21-8CBB-14A4A60D3EFD
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PPEP_REGISTER_DEBUGGER, PEP_REGISTER_DEBUGGER, PEP_REGISTER_DEBUGGER structure [Kernel-Mode Driver Architecture], PPEP_REGISTER_DEBUGGER, PPEP_REGISTER_DEBUGGER structure pointer [Kernel-Mode Driver Architecture], _PEP_REGISTER_DEBUGGER, kernel.pep_register_debugger, pepfx/PEP_REGISTER_DEBUGGER, pepfx/PPEP_REGISTER_DEBUGGER"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: Pep_x.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
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
-	pepfx.h
api_name:
-	PEP_REGISTER_DEBUGGER
product: Windows
targetos: Windows
req.typenames: PEP_REGISTER_DEBUGGER, *PPEP_REGISTER_DEBUGGER
---

# _PEP_REGISTER_DEBUGGER structure
The <b>PEP_REGISTER_DEBUGGER</b> structure identifies a registered device that is a core system resource that provides debugger transport.

## Syntax
````
typedef struct _PEP_REGISTER_DEBUGGER {
  PEPHANDLE DeviceHandle;
} PEP_REGISTER_DEBUGGER, *PPEP_REGISTER_DEBUGGER;
````

## Members


`DeviceHandle`

[in] A <b>PEPHANDLE</b> value that identifies the device. The PEP supplied this handle in response to a previous <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186849">PEP_DPM_REGISTER_DEVICE</a> notification.

## Remarks
This structure is used by the <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186850">PEP_DPM_REGISTER_DEBUGGER</a> notification. The <b>DeviceHandle</b> member contains an input value that is supplied by the Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186849">PEP_DPM_REGISTER_DEVICE</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186850">PEP_DPM_REGISTER_DEBUGGER</a>