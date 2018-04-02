---
UID: NE:pepfx._PEP_DEVICE_ACCEPTANCE_TYPE
title: "_PEP_DEVICE_ACCEPTANCE_TYPE"
author: windows-driver-content
description: The PEP_DEVICE_ACCEPTANCE_TYPE enumeration indicates whether a PEP accepts ownership of a device.
old-location: kernel\pep_device_acceptance_type.htm
old-project: kernel
ms.assetid: 72D0BEC2-F5D5-4045-AD63-F263993817B0
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_DEVICE_ACCEPTANCE_TYPE, PEP_DEVICE_ACCEPTANCE_TYPE, PEP_DEVICE_ACCEPTANCE_TYPE enumeration [Kernel-Mode Driver Architecture], PepDeviceAccepted, PepDeviceAcceptedMax, PepDeviceAcceptedReserved, PepDeviceNotAccepted, _PEP_DEVICE_ACCEPTANCE_TYPE, kernel.pep_device_acceptance_type, pepfx/PEP_DEVICE_ACCEPTANCE_TYPE, pepfx/PepDeviceAccepted, pepfx/PepDeviceAcceptedMax, pepfx/PepDeviceAcceptedReserved, pepfx/PepDeviceNotAccepted"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
-	PEP_DEVICE_ACCEPTANCE_TYPE
product:
- Windows
targetos: Windows
req.typenames: PEP_DEVICE_ACCEPTANCE_TYPE, *PPEP_DEVICE_ACCEPTANCE_TYPE
---

# _PEP_DEVICE_ACCEPTANCE_TYPE Enumeration
The <b>PEP_DEVICE_ACCEPTANCE_TYPE</b> enumeration indicates whether a PEP accepts ownership of a device.

## Syntax
```
typedef enum _PEP_DEVICE_ACCEPTANCE_TYPE {
  PepDeviceNotAccepted  ,
  PepDeviceAccepted     ,
  PepDeviceAceptedMax
} PEP_DEVICE_ACCEPTANCE_TYPE, *PPEP_DEVICE_ACCEPTANCE_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>PepDeviceNotAccepted</td>
                    <td>The PEP does not claim ownership of this device.</td>
                </tr>
            
                <tr>
                    <td>PepDeviceAccepted</td>
                    <td>The PEP claims ownership of this device.</td>
                </tr>
            
                <tr>
                    <td>PepDeviceAceptedMax</td>
                    <td></td>
                </tr>
</table>

## Remarks

This enumeration is used by <b>DeviceAccepted</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186851">PEP_REGISTER_DEVICE_V2</a> structure to indicate whether a PEP accepts ownership of a device.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186851">PEP_REGISTER_DEVICE_V2</a>