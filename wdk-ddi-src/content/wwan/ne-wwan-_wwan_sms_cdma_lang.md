---
UID: NE:wwan._WWAN_SMS_CDMA_LANG
title: "_WWAN_SMS_CDMA_LANG"
author: windows-driver-content
description: The WWAN_SMS_CDMA_LANG enumeration lists the different SMS CDMA languages that are supported by the MB device.
old-location: netvista\wwan_sms_cdma_lang.htm
old-project: netvista
ms.assetid: 5294ce07-a4eb-4c21-88f1-04889dfbc1a1
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: "*PWWAN_SMS_CDMA_LANG, wwan/WwanSmsCdmaLangJapanese, wwan/WwanSmsCdmaLangChinese, WwanSmsCdmaLangMax, wwan/WwanSmsCdmaLangSpanish, WwanSmsCdmaLangSpanish, WwanSmsCdmaLangChinese, wwan/WwanSmsCdmaLangHebrew, wwan/WwanSmsCdmaLangKorean, _WWAN_SMS_CDMA_LANG, wwan/WwanSmsCdmaLangUnknown, WWAN_SMS_CDMA_LANG enumeration [Network Drivers Starting with Windows Vista], PWWAN_SMS_CDMA_LANG enumeration pointer [Network Drivers Starting with Windows Vista], wwan/WwanSmsCdmaLangEnglish, PWWAN_SMS_CDMA_LANG, WwanSmsCdmaLangJapanese, WwanSmsCdmaLangFrench, wwan/WwanSmsCdmaLangFrench, wwan/WWAN_SMS_CDMA_LANG, wwan/PWWAN_SMS_CDMA_LANG, WwanSmsCdmaLangUnknown, WwanSmsCdmaLangEnglish, WwanSmsCdmaLangHebrew, WWAN_SMS_CDMA_LANG, WwanRef_21c9fcf4-07b0-43b3-86df-a2de613f5018.xml, WwanSmsCdmaLangKorean, wwan/WwanSmsCdmaLangMax, netvista.wwan_sms_cdma_lang"
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wwan.h
apiname:
-	WWAN_SMS_CDMA_LANG
product: Windows
targetos: Windows
req.typenames: WWAN_SMS_CDMA_LANG, *PWWAN_SMS_CDMA_LANG
req.product: Windows 10 or later.
---

# _WWAN_SMS_CDMA_LANG Enumeration
The WWAN_SMS_CDMA_LANG enumeration lists the different SMS CDMA languages that are supported by the
  MB device.

## Syntax
````
typedef enum _WWAN_SMS_CDMA_LANG { 
  WwanSmsCdmaLangUnknown   = 0,
  WwanSmsCdmaLangEnglish,
  WwanSmsCdmaLangFrench,
  WwanSmsCdmaLangSpanish,
  WwanSmsCdmaLangJapanese,
  WwanSmsCdmaLangKorean,
  WwanSmsCdmaLangChinese,
  WwanSmsCdmaLangHebrew,
  WwanSmsCdmaLangMax
} WWAN_SMS_CDMA_LANG, *PWWAN_SMS_CDMA_LANG;
````

## Constants

<table>
            
                <tr>
                    <td>WwanSmsCdmaLangChinese</td>
                    <td>The message is in Chinese.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangEnglish</td>
                    <td>The message is in English.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangFrench</td>
                    <td>The message is in French.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangHebrew</td>
                    <td>The message is in Hebrew.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangJapanese</td>
                    <td>The message is in Japanese.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangKorean</td>
                    <td>The message is in Korean.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangMax</td>
                    <td>The total number of supported SMS CDMA languages.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangSpanish</td>
                    <td>The message is in Spanish.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsCdmaLangUnknown</td>
                    <td>The message language is unknown.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_sms_send_cdma.md">WWAN_SMS_SEND_CDMA</a>



<a href="..\wwan\ns-wwan-_wwan_sms_cdma_record.md">WWAN_SMS_CDMA_RECORD</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_CDMA_LANG enumeration%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>