---
UID: NE:wwan._WWAN_ACTIVATION_COMMAND
title: "_WWAN_ACTIVATION_COMMAND"
author: windows-driver-content
description: The WWAN_ACTIVATION_COMMAND enumeration lists the Packet Data Protocol (PDP) activation commands that are supported by the MB device.
old-location: netvista\wwan_activation_command.htm
old-project: netvista
ms.assetid: e9d25ac3-8ffc-4137-8409-731d8caaa730
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_ACTIVATION_COMMAND, PWWAN_ACTIVATION_COMMAND, PWWAN_ACTIVATION_COMMAND enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_ACTIVATION_COMMAND, WWAN_ACTIVATION_COMMAND enumeration [Network Drivers Starting with Windows Vista], WwanActivationCommandActivate, WwanActivationCommandDeactivate, WwanActivationCommandMax, WwanRef_55137856-bb05-49ac-b318-cc6922a90445.xml, _WWAN_ACTIVATION_COMMAND, netvista.wwan_activation_command, wwan/PWWAN_ACTIVATION_COMMAND, wwan/WWAN_ACTIVATION_COMMAND, wwan/WwanActivationCommandActivate, wwan/WwanActivationCommandDeactivate, wwan/WwanActivationCommandMax"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wwan.h
api_name:
-	WWAN_ACTIVATION_COMMAND
product:
- Windows
targetos: Windows
req.typenames: WWAN_ACTIVATION_COMMAND, *PWWAN_ACTIVATION_COMMAND
req.product: Windows 10 or later.
---

# _WWAN_ACTIVATION_COMMAND Enumeration
The WWAN_ACTIVATION_COMMAND enumeration lists the Packet Data Protocol (PDP) activation commands that
  are supported by the MB device.

## Syntax
```
typedef enum _WWAN_ACTIVATION_COMMAND {
  WwanActivationCommandDeactivate  ,
  WwanActivationCommandActivate    ,
  WwanActivationCommandMax
} WWAN_ACTIVATION_COMMAND, *PWWAN_ACTIVATION_COMMAND;
```

## Constants

<table>
            
                <tr>
                    <td>WwanActivationCommandDeactivate</td>
                    <td>Deactivate a currently activated PDP context identified by 
     <b>ConnectionId</b> .</td>
                </tr>
            
                <tr>
                    <td>WwanActivationCommandActivate</td>
                    <td>Activate PDP context.</td>
                </tr>
            
                <tr>
                    <td>WwanActivationCommandMax</td>
                    <td>The total number of supported activation commands.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571235">WWAN_SET_CONTEXT_STATE</a>