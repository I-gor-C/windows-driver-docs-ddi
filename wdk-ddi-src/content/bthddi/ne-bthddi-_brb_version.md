---
UID: NE:bthddi._BRB_VERSION
title: "_BRB_VERSION"
author: windows-driver-content
description: Reserved for internal use.
old-location: bltooth\brb_version.htm
old-project: bltooth
ms.assetid: 2bd4f3f6-94a4-47a6-8c15-a8f9bef5d2b5
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: BLUETOOTH_V1, BLUETOOTH_V2, BRB_VERSION, BRB_VERSION enumeration [Bluetooth Devices], _BRB_VERSION, bltooth.brb_version, bth_enums_d14431ac-24e9-4a27-90b9-a8aef7e38769.xml, bthddi/BLUETOOTH_V1, bthddi/BLUETOOTH_V2, bthddi/BRB_VERSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows Vista, and later.
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
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	bthddi.h
api_name:
-	BRB_VERSION
product: Windows
targetos: Windows
req.typenames: BRB_VERSION
---

# _BRB_VERSION Enumeration
Reserved for internal use.

## Syntax
```
typedef enum _BRB_VERSION {
  BLUETOOTH_V1  ,
  BLUETOOTH_V2
} BRB_VERSION;
```

## Constants

<table>
            
                <tr>
                    <td>BLUETOOTH_V1</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>BLUETOOTH_V2</td>
                    <td>Reserved.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536607">BRB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536612">BRB_HEADER</a>



<a href="https://msdn.microsoft.com/e1ac9d4c-75e2-4d37-86d7-3c3f1486222e">BthAllocateBrb</a>



<a href="https://msdn.microsoft.com/0b822d28-edaa-40cc-a678-112a356d9022">BthInitializeBrb</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536751">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>