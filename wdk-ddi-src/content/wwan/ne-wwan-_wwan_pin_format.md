---
UID : NE:wwan._WWAN_PIN_FORMAT
title : "_WWAN_PIN_FORMAT"
author : windows-driver-content
description : The WWAN_PIN_FORMAT enumeration lists the different Personal Identification Number (PIN) formats that are supported by the MB device.
old-location : netvista\wwan_pin_format.htm
old-project : netvista
ms.assetid : ccc3934c-fed4-4f9d-ae2a-d5e96bdb1e46
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.wwan_pin_format, WwanPinFormatUnknown, WwanPinFormatNumeric, wwan/WwanPinFormatNumeric, WwanRef_f3030aa5-70d9-46d6-85e1-dc112a5889ce.xml, wwan/PWWAN_PIN_FORMAT, wwan/WwanPinFormatUnknown, PWWAN_PIN_FORMAT, _WWAN_PIN_FORMAT, wwan/WWAN_PIN_FORMAT, wwan/WwanPinFormatMax, PWWAN_PIN_FORMAT enumeration pointer [Network Drivers Starting with Windows Vista], WwanPinFormatAlphaNumeric, *PWWAN_PIN_FORMAT, WwanPinFormatMax, WWAN_PIN_FORMAT, WWAN_PIN_FORMAT enumeration [Network Drivers Starting with Windows Vista], wwan/WwanPinFormatAlphaNumeric
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wwan.h
req.include-header : Wwan.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 7 and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WWAN_PIN_FORMAT, *PWWAN_PIN_FORMAT
req.product : Windows 10 or later.
---

# _WWAN_PIN_FORMAT Enumeration
The WWAN_PIN_FORMAT enumeration lists the different Personal Identification Number (PIN) formats that
  are supported by the MB device.

## Syntax
````
typedef enum _WWAN_PIN_FORMAT { 
  WwanPinFormatUnknown       = 0,
  WwanPinFormatNumeric,
  WwanPinFormatAlphaNumeric,
  WwanPinFormatMax
} WWAN_PIN_FORMAT, *PWWAN_PIN_FORMAT;
````

## Constants

<table>

<tr>
<td>WwanPinFormatAlphaNumeric</td>
<td>The format of the PIN allows alphanumeric characters a through z (lowercase), A through Z
     (uppercase), 0 through 9 (numeric), the asterisk symbol (*), and the pound symbol (#).</td>
</tr>

<tr>
<td>WwanPinFormatMax</td>
<td>The total number of supported PIN formats.</td>
</tr>

<tr>
<td>WwanPinFormatNumeric</td>
<td>The format of the PIN allows only the numerical characters 0 through 9.</td>
</tr>

<tr>
<td>WwanPinFormatUnknown</td>
<td>The format of PIN is not specified.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_pin_desc.md">WWAN_PIN_DESC</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PIN_FORMAT enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>