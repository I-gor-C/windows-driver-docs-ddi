---
UID: NE:wwan._WWAN_READY_STATE
title: "_WWAN_READY_STATE"
author: windows-driver-content
description: The WWAN_READY_STATE enumeration lists the different device ready-states that are supported by the MB device.
old-location: netvista\wwan_ready_state.htm
old-project: netvista
ms.assetid: 46fec377-ba2c-469a-96be-23aa07079f8c
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_READY_STATE, PWWAN_READY_STATE, PWWAN_READY_STATE enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_READY_STATE, WWAN_READY_STATE enumeration [Network Drivers Starting with Windows Vista], WwanReadyStateBadSim, WwanReadyStateDeviceLocked, WwanReadyStateFailure, WwanReadyStateInitialized, WwanReadyStateNotActivated, WwanReadyStateOff, WwanReadyStateSimNotInserted, WwanRef_08468e16-e4da-49ff-9b2a-2cee4df6c72f.xml, _WWAN_READY_STATE, netvista.wwan_ready_state, wwan/PWWAN_READY_STATE, wwan/WWAN_READY_STATE, wwan/WwanReadyStateBadSim, wwan/WwanReadyStateDeviceLocked, wwan/WwanReadyStateFailure, wwan/WwanReadyStateInitialized, wwan/WwanReadyStateNotActivated, wwan/WwanReadyStateOff, wwan/WwanReadyStateSimNotInserted"
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
-	WWAN_READY_STATE
product: Windows
targetos: Windows
req.typenames: WWAN_READY_STATE, *PWWAN_READY_STATE
req.product: Windows 10 or later.
---

# _WWAN_READY_STATE Enumeration
The WWAN_READY_STATE enumeration lists the different device ready-states that are supported by the MB
  device.

## Syntax
```
typedef enum _WWAN_READY_STATE {
  WwanReadyStateOff             ,
  WwanReadyStateInitialized     ,
  WwanReadyStateSimNotInserted  ,
  WwanReadyStateBadSim          ,
  WwanReadyStateFailure         ,
  WwanReadyStateNotActivated    ,
  WwanReadyStateDeviceLocked    ,
  WwanReadyStateNoEsimProfile   ,
  WwanReadyStateMax
} *PWWAN_READY_STATE, WWAN_READY_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>WwanReadyStateOff</td>
                    <td>The device firmware stack is OFF or has not yet completed its initialization.</td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateInitialized</td>
                    <td>The device is ready to turn on and register with the provider.</td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateSimNotInserted</td>
                    <td>The SIM card is not inserted into the device.</td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateBadSim</td>
                    <td>The SIM card inserted into the device is invalid.</td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateFailure</td>
                    <td>A general device failure has occurred.</td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateNotActivated</td>
                    <td>The subscription is not activated.</td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateDeviceLocked</td>
                    <td>The device is locked and requires PIN1 or PUK1 to unlock.
     

Note that if a device is locked because it requires a PIN type other than PIN1 or PUK1 (for example,
     a network personalization PIN), miniport drivers should report 
     <b>WwanReadyStateInitialized</b>. Though miniport drivers should return WWAN_STATUS_PIN_REQUIRED for OID
     requests which are blocked because of PIN. Subsequent OID_WWAN_PIN 
     <i>query</i> requests should return the PIN type needed to unlock the device.</td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateNoEsimProfile</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanReadyStateMax</td>
                    <td></td>
                </tr>
</table>

## Remarks

For devices that use a SIM card, this enumeration indicates if the SIM card has been initialized and
    is ready for access.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571226">WWAN_READY_INFO</a>