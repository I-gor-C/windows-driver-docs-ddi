---
UID: NE:wwan._WWAN_SMS_CDMA_ENCODING
title: "_WWAN_SMS_CDMA_ENCODING"
author: windows-driver-content
description: The WWAN_SMS_CDMA_ENCODING enumeration lists the different SMS CDMA encoding formats that are supported by the MB device.
old-location: netvista\wwan_sms_cdma_encoding.htm
old-project: netvista
ms.assetid: 1f632da2-36bb-491e-b445-5c320277a446
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_SMS_CDMA_ENCODING, PWWAN_SMS_CDMA_ENCODING, PWWAN_SMS_CDMA_ENCODING enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_SMS_CDMA_ENCODING, WWAN_SMS_CDMA_ENCODING enumeration [Network Drivers Starting with Windows Vista], WwanRef_a106195c-4a1c-4f95-9c38-91390dadf046.xml, WwanSmsCdmaEncoding7BitAscii, WwanSmsCdmaEncodingEpm, WwanSmsCdmaEncodingGsm7Bit, WwanSmsCdmaEncodingIa5, WwanSmsCdmaEncodingKorean, WwanSmsCdmaEncodingLatin, WwanSmsCdmaEncodingLatinHebrew, WwanSmsCdmaEncodingMax, WwanSmsCdmaEncodingOctet, WwanSmsCdmaEncodingShiftJis, WwanSmsCdmaEncodingUnicode, _WWAN_SMS_CDMA_ENCODING, netvista.wwan_sms_cdma_encoding, wwan/PWWAN_SMS_CDMA_ENCODING, wwan/WWAN_SMS_CDMA_ENCODING, wwan/WwanSmsCdmaEncoding7BitAscii, wwan/WwanSmsCdmaEncodingEpm, wwan/WwanSmsCdmaEncodingGsm7Bit, wwan/WwanSmsCdmaEncodingIa5, wwan/WwanSmsCdmaEncodingKorean, wwan/WwanSmsCdmaEncodingLatin, wwan/WwanSmsCdmaEncodingLatinHebrew, wwan/WwanSmsCdmaEncodingMax, wwan/WwanSmsCdmaEncodingOctet, wwan/WwanSmsCdmaEncodingShiftJis, wwan/WwanSmsCdmaEncodingUnicode"
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
-	WWAN_SMS_CDMA_ENCODING
product: Windows
targetos: Windows
req.typenames: WWAN_SMS_CDMA_ENCODING, *PWWAN_SMS_CDMA_ENCODING
req.product: Windows 10 or later.
---

# _WWAN_SMS_CDMA_ENCODING Enumeration
The WWAN_SMS_CDMA_ENCODING enumeration lists the different SMS CDMA encoding formats that are
  supported by the MB device.

## Syntax
```
typedef enum _WWAN_SMS_CDMA_ENCODING {
  WwanSmsCdmaEncodingOctet        ,
  WwanSmsCdmaEncodingEpm          ,
  WwanSmsCdmaEncoding7BitAscii    ,
  WwanSmsCdmaEncodingIa5          ,
  WwanSmsCdmaEncodingUnicode      ,
  WwanSmsCdmaEncodingShiftJis     ,
  WwanSmsCdmaEncodingKorean       ,
  WwanSmsCdmaEncodingLatinHebrew  ,
  WwanSmsCdmaEncodingLatin        ,
  WwanSmsCdmaEncodingGsm7Bit      ,
  WwanSmsCdmaEncodingMax
} *PWWAN_SMS_CDMA_ENCODING, WWAN_SMS_CDMA_ENCODING;
```

## Constants

<table>
            
                <tr>
                    <td>WwanSmsCdmaEncodingOctet</td>
                    <td>The message uses octet encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingEpm</td>
                    <td>The message uses EPM encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncoding7BitAscii</td>
                    <td>The message uses 7-bit ASCII encoding. The encoded message is represented in bytes per character.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingIa5</td>
                    <td>The message uses IA5 encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingUnicode</td>
                    <td>The message uses Unicode encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingShiftJis</td>
                    <td>The message uses shifted JIS encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingKorean</td>
                    <td>The message uses Korean encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingLatinHebrew</td>
                    <td>The message uses Latin Hebrew encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingLatin</td>
                    <td>The message uses Latin encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingGsm7Bit</td>
                    <td>The message uses 7-bit GSM encoding.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaEncodingMax</td>
                    <td>The total number of supported SMS CDMA encoding formats.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff571251">WWAN_SMS_SEND_CDMA</a>