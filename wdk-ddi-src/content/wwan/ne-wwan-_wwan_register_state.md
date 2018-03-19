---
UID: NE:wwan._WWAN_REGISTER_STATE
title: "_WWAN_REGISTER_STATE"
author: windows-driver-content
description: The WWAN_REGISTER_STATE enumeration lists the different provider network registration states that are supported by the MB device.
old-location: netvista\wwan_register_state.htm
old-project: netvista
ms.assetid: fba4e60e-c247-4466-9b0f-c8e7ffa594d2
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_REGISTER_STATE, PWWAN_REGISTER_STATE, PWWAN_REGISTER_STATE enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_REGISTER_STATE, WWAN_REGISTER_STATE enumeration [Network Drivers Starting with Windows Vista], WwanRef_927c04e0-b022-4d93-8052-696b5e9da51f.xml, WwanRegisterStateDenied, WwanRegisterStateDeregistered, WwanRegisterStateHome, WwanRegisterStateMax, WwanRegisterStatePartner, WwanRegisterStateRoaming, WwanRegisterStateSearching, WwanRegisterStateUnknown, _WWAN_REGISTER_STATE, netvista.wwan_register_state, wwan/PWWAN_REGISTER_STATE, wwan/WWAN_REGISTER_STATE, wwan/WwanRegisterStateDenied, wwan/WwanRegisterStateDeregistered, wwan/WwanRegisterStateHome, wwan/WwanRegisterStateMax, wwan/WwanRegisterStatePartner, wwan/WwanRegisterStateRoaming, wwan/WwanRegisterStateSearching, wwan/WwanRegisterStateUnknown"
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
-	WWAN_REGISTER_STATE
product: Windows
targetos: Windows
req.typenames: WWAN_REGISTER_STATE, *PWWAN_REGISTER_STATE
req.product: Windows 10 or later.
---

# _WWAN_REGISTER_STATE Enumeration
The WWAN_REGISTER_STATE enumeration lists the different provider network registration states that are
  supported by the MB device.

## Syntax
````
typedef enum _WWAN_REGISTER_STATE { 
  WwanRegisterStateUnknown       = 0,
  WwanRegisterStateDeregistered,
  WwanRegisterStateSearching,
  WwanRegisterStateHome,
  WwanRegisterStateRoaming,
  WwanRegisterStatePartner,
  WwanRegisterStateDenied,
  WwanRegisterStateMax
} WWAN_REGISTER_STATE, *PWWAN_REGISTER_STATE;
````

## Constants

<table>
            
                <tr>
                    <td>WwanRegisterStateUnknown</td>
                    <td>The current registration state is unknown. The miniport driver may specify this state on a failure
     to set an appropriate 
     <i>WwanRegisterActionXxx</i>.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterStateDeregistered</td>
                    <td>The device is not registered and is not searching for network providers.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterStateSearching</td>
                    <td>The device is searching for a network provider.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterStateHome</td>
                    <td>The device is using the home network provider.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterStateRoaming</td>
                    <td>The device is using a network provider that supports roaming.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterStatePartner</td>
                    <td>The device is using a roaming network partner.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterStateDenied</td>
                    <td>Registration of the device on visible networks has been denied. However, emergency voice calls may
     still be made. This value applies only to voice connections, and not to data connections.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterStateMax</td>
                    <td>The total number of supported registration states.</td>
                </tr>
</table>

## Remarks

The current registration state is typically reflected in the device's user interface.

The 
    <b>WwanRegisterStatePartner</b> value indicates that the device is roaming on a preferred partner network,
    whereas 
    <b>WwanRegisterStateRoaming</b> value indicates that the device is just roaming. If the partner
    characterization of the roaming state is not available, the miniport driver should report 
    <b>WwanRegisterStateRoaming</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_registration_state.md">WWAN_REGISTRATION_STATE</a>