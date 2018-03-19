---
UID: NE:wwan._WWAN_MSG_STATUS
title: "_WWAN_MSG_STATUS"
author: windows-driver-content
description: The WWAN_MSG_STATUS enumeration lists different SMS message statuses.
old-location: netvista\wwan_msg_status.htm
old-project: netvista
ms.assetid: 60eb0494-fcc6-4546-a13a-b6d1dcf165e6
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_MSG_STATUS, PWWAN_MSG_STATUS, PWWAN_MSG_STATUS enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_MSG_STATUS, WWAN_MSG_STATUS enumeration [Network Drivers Starting with Windows Vista], WwanMsgStatusDraft, WwanMsgStatusMax, WwanMsgStatusNew, WwanMsgStatusOld, WwanMsgStatusSent, WwanRef_2cd2fe07-ee6c-4193-960e-434e31561f9e.xml, _WWAN_MSG_STATUS, netvista.wwan_msg_status, wwan/PWWAN_MSG_STATUS, wwan/WWAN_MSG_STATUS, wwan/WwanMsgStatusDraft, wwan/WwanMsgStatusMax, wwan/WwanMsgStatusNew, wwan/WwanMsgStatusOld, wwan/WwanMsgStatusSent"
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
-	WWAN_MSG_STATUS
product: Windows
targetos: Windows
req.typenames: WWAN_MSG_STATUS, *PWWAN_MSG_STATUS
req.product: Windows 10 or later.
---

# _WWAN_MSG_STATUS Enumeration
The WWAN_MSG_STATUS enumeration lists different SMS message statuses.

## Syntax
````
typedef enum _WWAN_MSG_STATUS { 
  WwanMsgStatusNew    = 0,
  WwanMsgStatusOld,
  WwanMsgStatusDraft,
  WwanMsgStatusSent,
  WwanMsgStatusMax
} WWAN_MSG_STATUS, *PWWAN_MSG_STATUS;
````

## Constants

<table>
            
                <tr>
                    <td>WwanMsgStatusNew</td>
                    <td>The message is new or unread.</td>
                </tr>
            
                <tr>
                    <td>WwanMsgStatusOld</td>
                    <td>The message is old and is read.</td>
                </tr>
            
                <tr>
                    <td>WwanMsgStatusDraft</td>
                    <td>The message is unsent and stored in the device.</td>
                </tr>
            
                <tr>
                    <td>WwanMsgStatusSent</td>
                    <td>The message has already been sent.</td>
                </tr>
            
                <tr>
                    <td>WwanMsgStatusMax</td>
                    <td>The total number of supported SMS message statuses.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_sms_pdu_record.md">WWAN_SMS_PDU_RECORD</a>



<a href="..\wwan\ns-wwan-_wwan_sms_cdma_record.md">WWAN_SMS_CDMA_RECORD</a>