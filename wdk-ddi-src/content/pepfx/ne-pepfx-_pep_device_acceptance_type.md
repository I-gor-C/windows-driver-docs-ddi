---
UID: NE:pepfx._PEP_DEVICE_ACCEPTANCE_TYPE
title: "_PEP_DEVICE_ACCEPTANCE_TYPE"
author: windows-driver-content
description: The PEP_DEVICE_ACCEPTANCE_TYPE enumeration indicates whether a PEP accepts ownership of a device.
old-location: kernel\pep_device_acceptance_type.htm
old-project: kernel
ms.assetid: 72D0BEC2-F5D5-4045-AD63-F263993817B0
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: PepDeviceAcceptedReserved, PEP_DEVICE_ACCEPTANCE_TYPE enumeration [Kernel-Mode Driver Architecture], pepfx/PepDeviceAcceptedMax, PepDeviceNotAccepted, PEP_DEVICE_ACCEPTANCE_TYPE, *PPEP_DEVICE_ACCEPTANCE_TYPE, kernel.pep_device_acceptance_type, PepDeviceAccepted, _PEP_DEVICE_ACCEPTANCE_TYPE, pepfx/PEP_DEVICE_ACCEPTANCE_TYPE, pepfx/PepDeviceNotAccepted, pepfx/PepDeviceAccepted, pepfx/PepDeviceAcceptedReserved, PepDeviceAcceptedMax
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pepfx.h
req.include-header: 
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
req.irql: See Remarks.
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	pepfx.h
apiname:
-	PEP_DEVICE_ACCEPTANCE_TYPE
product: Windows
targetos: Windows
req.typenames: "*PPEP_DEVICE_ACCEPTANCE_TYPE, PEP_DEVICE_ACCEPTANCE_TYPE"
---

# _PEP_DEVICE_ACCEPTANCE_TYPE Enumeration
The <b>PEP_DEVICE_ACCEPTANCE_TYPE</b> enumeration indicates whether a PEP accepts ownership of a device.

## Syntax
````
typedef enum _PEP_DEVICE_ACCEPTANCE_TYPE { 
  PepDeviceNotAccepted       = 0,
  PepDeviceAcceptedReserved,
  PepDeviceAccepted,
  PepDeviceAcceptedMax
} PEP_DEVICE_ACCEPTANCE_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>PepDeviceAccepted</td>
                    <td>The PEP claims ownership of this device.</td>
                </tr>
            
                <tr>
                    <td>PepDeviceAceptedMax</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PepDeviceNotAccepted</td>
                    <td>The PEP does not claim ownership of this device.</td>
                </tr>
</table>

    ## Remarks

        This enumeration is used by <b>DeviceAccepted</b> member of the <a href="..\pepfx\ns-pepfx-_pep_register_device_v2.md">PEP_REGISTER_DEVICE_V2</a> structure to indicate whether a PEP accepts ownership of a device.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pepfx.h |

    ## See Also

        <a href="..\pepfx\ns-pepfx-_pep_register_device_v2.md">PEP_REGISTER_DEVICE_V2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_DEVICE_ACCEPTANCE_TYPE enumeration%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>