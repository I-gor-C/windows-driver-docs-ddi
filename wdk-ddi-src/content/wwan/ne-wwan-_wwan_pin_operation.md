---
UID: NE:wwan._WWAN_PIN_OPERATION
title: "_WWAN_PIN_OPERATION"
author: windows-driver-content
description: The WWAN_PIN_OPERATION enumeration lists the different Personal Identification Number (PIN) operations that are supported by the MB device.
old-location: netvista\wwan_pin_operation.htm
old-project: netvista
ms.assetid: 1b21b4b4-a35d-47c4-9cd6-e31e2dfbe59f
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_PIN_OPERATION, PWWAN_PIN_OPERATION, PWWAN_PIN_OPERATION enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_PIN_OPERATION, WWAN_PIN_OPERATION enumeration [Network Drivers Starting with Windows Vista], WwanPinOperationChange, WwanPinOperationDisable, WwanPinOperationEnable, WwanPinOperationEnter, WwanPinOperationMax, WwanRef_06404d11-22d3-4b07-9c6f-60771ecfc154.xml, _WWAN_PIN_OPERATION, netvista.wwan_pin_operation, wwan/PWWAN_PIN_OPERATION, wwan/WWAN_PIN_OPERATION, wwan/WwanPinOperationChange, wwan/WwanPinOperationDisable, wwan/WwanPinOperationEnable, wwan/WwanPinOperationEnter, wwan/WwanPinOperationMax"
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
-	WWAN_PIN_OPERATION
product:
- Windows
targetos: Windows
req.typenames: WWAN_PIN_OPERATION, *PWWAN_PIN_OPERATION
req.product: Windows 10 or later.
---

# _WWAN_PIN_OPERATION Enumeration
The WWAN_PIN_OPERATION enumeration lists the different Personal Identification Number (PIN)
  operations that are supported by the MB device.

## Syntax
```
typedef enum _WWAN_PIN_OPERATION {
  WwanPinOperationEnter    ,
  WwanPinOperationEnable   ,
  WwanPinOperationDisable  ,
  WwanPinOperationChange   ,
  WwanPinOperationMax
} WWAN_PIN_OPERATION, *PWWAN_PIN_OPERATION;
```

## Constants

<table>
            
                <tr>
                    <td>WwanPinOperationEnter</td>
                    <td>Enter the specified PIN into the device.</td>
                </tr>
            
                <tr>
                    <td>WwanPinOperationEnable</td>
                    <td>Enable the specified PIN.</td>
                </tr>
            
                <tr>
                    <td>WwanPinOperationDisable</td>
                    <td>Disable the specified PIN.</td>
                </tr>
            
                <tr>
                    <td>WwanPinOperationChange</td>
                    <td>Change the specified PIN.</td>
                </tr>
            
                <tr>
                    <td>WwanPinOperationMax</td>
                    <td>The total number of supported PIN operations.</td>
                </tr>
</table>

## Remarks

If a PIN disable operation for a given PIN type is tried when that PIN type is locked, miniport
    drivers can either fail the request with WWAN_STATUS_PIN_REQUIRED or they can successfully complete the
    request. If miniport drivers complete the request successfully, the disable operation should also unlock
    the PIN.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571213">WWAN_PIN_ACTION</a>