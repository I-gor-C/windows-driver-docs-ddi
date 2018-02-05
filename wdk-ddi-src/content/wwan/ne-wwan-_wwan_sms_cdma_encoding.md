---
UID : NE:wwan._WWAN_SMS_CDMA_ENCODING
title : "_WWAN_SMS_CDMA_ENCODING"
author : windows-driver-content
description : The WWAN_SMS_CDMA_ENCODING enumeration lists the different SMS CDMA encoding formats that are supported by the MB device.
old-location : netvista\wwan_sms_cdma_encoding.htm
old-project : netvista
ms.assetid : 1f632da2-36bb-491e-b445-5c320277a446
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : WwanRef_a106195c-4a1c-4f95-9c38-91390dadf046.xml, WWAN_SMS_CDMA_ENCODING enumeration [Network Drivers Starting with Windows Vista], wwan/WwanSmsCdmaEncodingShiftJis, WwanSmsCdmaEncodingGsm7Bit, _WWAN_SMS_CDMA_ENCODING, wwan/WwanSmsCdmaEncodingEpm, WwanSmsCdmaEncodingLatinHebrew, WwanSmsCdmaEncodingShiftJis, wwan/WwanSmsCdmaEncoding7BitAscii, wwan/WwanSmsCdmaEncodingLatin, WwanSmsCdmaEncodingIa5, PWWAN_SMS_CDMA_ENCODING, WwanSmsCdmaEncoding7BitAscii, wwan/WwanSmsCdmaEncodingKorean, WwanSmsCdmaEncodingLatin, WwanSmsCdmaEncodingUnicode, wwan/WwanSmsCdmaEncodingIa5, WwanSmsCdmaEncodingEpm, wwan/WwanSmsCdmaEncodingMax, *PWWAN_SMS_CDMA_ENCODING, wwan/WWAN_SMS_CDMA_ENCODING, wwan/WwanSmsCdmaEncodingUnicode, wwan/WwanSmsCdmaEncodingGsm7Bit, PWWAN_SMS_CDMA_ENCODING enumeration pointer [Network Drivers Starting with Windows Vista], netvista.wwan_sms_cdma_encoding, WWAN_SMS_CDMA_ENCODING, WwanSmsCdmaEncodingMax, WwanSmsCdmaEncodingOctet, wwan/WwanSmsCdmaEncodingOctet, WwanSmsCdmaEncodingKorean, wwan/WwanSmsCdmaEncodingLatinHebrew, wwan/PWWAN_SMS_CDMA_ENCODING
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
req.typenames : "*PWWAN_SMS_CDMA_ENCODING, WWAN_SMS_CDMA_ENCODING"
req.product : Windows 10 or later.
---

# _WWAN_SMS_CDMA_ENCODING Enumeration
The WWAN_SMS_CDMA_ENCODING enumeration lists the different SMS CDMA encoding formats that are
  supported by the MB device.

## Syntax
````
typedef enum _WWAN_SMS_CDMA_ENCODING { 
  WwanSmsCdmaEncodingOctet        = 0,
  WwanSmsCdmaEncodingEpm,
  WwanSmsCdmaEncoding7BitAscii,
  WwanSmsCdmaEncodingIa5,
  WwanSmsCdmaEncodingUnicode,
  WwanSmsCdmaEncodingShiftJis,
  WwanSmsCdmaEncodingKorean,
  WwanSmsCdmaEncodingLatinHebrew,
  WwanSmsCdmaEncodingLatin,
  WwanSmsCdmaEncodingGsm7Bit,
  WwanSmsCdmaEncodingMax
} WWAN_SMS_CDMA_ENCODING, *PWWAN_SMS_CDMA_ENCODING;
````

## Constants

<table>

<tr>
<td>WwanSmsCdmaEncoding7BitAscii</td>
<td>The message uses 7-bit ASCII encoding. The encoded message is represented in bytes per character.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingEpm</td>
<td>The message uses EPM encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingGsm7Bit</td>
<td>The message uses 7-bit GSM encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingIa5</td>
<td>The message uses IA5 encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingKorean</td>
<td>The message uses Korean encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingLatin</td>
<td>The message uses Latin encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingLatinHebrew</td>
<td>The message uses Latin Hebrew encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingMax</td>
<td>The total number of supported SMS CDMA encoding formats.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingOctet</td>
<td>The message uses octet encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingShiftJis</td>
<td>The message uses shifted JIS encoding.</td>
</tr>

<tr>
<td>WwanSmsCdmaEncodingUnicode</td>
<td>The message uses Unicode encoding.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_sms_cdma_record.md">WWAN_SMS_CDMA_RECORD</a>

<a href="..\wwan\ns-wwan-_wwan_sms_send_cdma.md">WWAN_SMS_SEND_CDMA</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_CDMA_ENCODING enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>