---
UID: NE:wwan._WWAN_SMS_FORMAT
title: "_WWAN_SMS_FORMAT"
author: windows-driver-content
description: The WWAN_SMS_FORMAT enumeration lists different Short Message Service (SMS) formats.
old-location: netvista\wwan_sms_format.htm
old-project: netvista
ms.assetid: fb583ded-8292-4486-8e85-3d3039611d14
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_SMS_FORMAT, PWWAN_SMS_FORMAT, PWWAN_SMS_FORMAT enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_SMS_FORMAT, WWAN_SMS_FORMAT enumeration [Network Drivers Starting with Windows Vista], WwanRef_594a5286-7ead-4877-939c-ed4bf2eb99e0.xml, WwanSmsFormatCdma, WwanSmsFormatMax, WwanSmsFormatPdu, WwanSmsFormatReserved0, WwanSmsFormatReserved1, WwanSmsFormatReserved2, _WWAN_SMS_FORMAT, netvista.wwan_sms_format, wwan/PWWAN_SMS_FORMAT, wwan/WWAN_SMS_FORMAT, wwan/WwanSmsFormatCdma, wwan/WwanSmsFormatMax, wwan/WwanSmsFormatPdu, wwan/WwanSmsFormatReserved0, wwan/WwanSmsFormatReserved1, wwan/WwanSmsFormatReserved2"
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
-	WWAN_SMS_FORMAT
product:
- Windows
targetos: Windows
req.typenames: WWAN_SMS_FORMAT, *PWWAN_SMS_FORMAT
req.product: Windows 10 or later.
---

# _WWAN_SMS_FORMAT Enumeration
The WWAN_SMS_FORMAT enumeration lists different Short Message Service (SMS) formats.

## Syntax
```
typedef enum _WWAN_SMS_FORMAT {
  WwanSmsFormatPdu        ,
  WwanSmsFormatReserved0  ,
  WwanSmsFormatReserved1  ,
  WwanSmsFormatReserved2  ,
  WwanSmsFormatCdma       ,
  WwanSmsFormatMax
} *PWWAN_SMS_FORMAT, WWAN_SMS_FORMAT;
```

## Constants

<table>
            
                <tr>
                    <td>WwanSmsFormatPdu</td>
                    <td>SMS messages are in PDU format. For GSM-based devices, messages are hexadecimal strings that
     represent messages in PDU format as defined in the 3GPP TS 27.005 and 3GPP TS 23.040 specifications. For
     CDMA-based devices messages are byte arrays that represent messages as defined in section 3.4.2.1 SMS
     Point-to-Point Message in 3GPP2 specification C.S0015-A "Short Message Service (SMS) for Wideband Spread
     Spectrum Systems".</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFormatReserved0</td>
                    <td>This value is reserved for future use. Do not use.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFormatReserved1</td>
                    <td>This value is reserved for future use. Do not use.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFormatReserved2</td>
                    <td>This value is reserved for future use. Do not use.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFormatCdma</td>
                    <td>The message is in text format. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a> and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571251">WWAN_SMS_SEND_CDMA</a>. This value applies
     only to CDMA-based devices.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFormatMax</td>
                    <td>This value is reserved. Do not use.</td>
                </tr>
</table>

## Remarks

CDMA-based devices support only 
    <b>WwanSmsFormatCdma</b>. The 
    <b>WwanSmsFormatCdma</b> format is not applicable for GSM-based devices.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571238">WWAN_SET_SMS_CONFIGURATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff571244">WWAN_SMS_CONFIGURATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff571249">WWAN_SMS_READ</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff571250">WWAN_SMS_SEND</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff571251">WWAN_SMS_SEND_CDMA</a>