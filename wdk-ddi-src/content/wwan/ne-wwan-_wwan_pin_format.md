---
UID: NE:wwan._WWAN_PIN_FORMAT
title: "_WWAN_PIN_FORMAT"
author: windows-driver-content
description: The WWAN_PIN_FORMAT enumeration lists the different Personal Identification Number (PIN) formats that are supported by the MB device.
old-location: netvista\wwan_pin_format.htm
old-project: netvista
ms.assetid: ccc3934c-fed4-4f9d-ae2a-d5e96bdb1e46
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_PIN_FORMAT, PWWAN_PIN_FORMAT, PWWAN_PIN_FORMAT enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_PIN_FORMAT, WWAN_PIN_FORMAT enumeration [Network Drivers Starting with Windows Vista], WwanPinFormatAlphaNumeric, WwanPinFormatMax, WwanPinFormatNumeric, WwanPinFormatUnknown, WwanRef_f3030aa5-70d9-46d6-85e1-dc112a5889ce.xml, _WWAN_PIN_FORMAT, netvista.wwan_pin_format, wwan/PWWAN_PIN_FORMAT, wwan/WWAN_PIN_FORMAT, wwan/WwanPinFormatAlphaNumeric, wwan/WwanPinFormatMax, wwan/WwanPinFormatNumeric, wwan/WwanPinFormatUnknown"
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
-	WWAN_PIN_FORMAT
product: Windows
targetos: Windows
req.typenames: WWAN_PIN_FORMAT, *PWWAN_PIN_FORMAT
req.product: Windows 10 or later.
---

# _WWAN_PIN_FORMAT Enumeration
The WWAN_PIN_FORMAT enumeration lists the different Personal Identification Number (PIN) formats that
  are supported by the MB device.

## Syntax
```
typedef enum _WWAN_PIN_FORMAT {
  WwanPinFormatUnknown       ,
  WwanPinFormatNumeric       ,
  WwanPinFormatAlphaNumeric  ,
  WwanPinFormatMax
} WWAN_PIN_FORMAT, *PWWAN_PIN_FORMAT;
```

## Constants

<table>
            
                <tr>
                    <td>WwanPinFormatUnknown</td>
                    <td>The format of PIN is not specified.</td>
                </tr>
            
                <tr>
                    <td>WwanPinFormatNumeric</td>
                    <td>The format of the PIN allows only the numerical characters 0 through 9.</td>
                </tr>
            
                <tr>
                    <td>WwanPinFormatAlphaNumeric</td>
                    <td>The format of the PIN allows alphanumeric characters a through z (lowercase), A through Z
     (uppercase), 0 through 9 (numeric), the asterisk symbol (*), and the pound symbol (#).</td>
                </tr>
            
                <tr>
                    <td>WwanPinFormatMax</td>
                    <td>The total number of supported PIN formats.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571214">WWAN_PIN_DESC</a>