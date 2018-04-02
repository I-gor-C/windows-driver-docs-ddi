---
UID: NE:wwan._WWAN_SMS_FLAG
title: "_WWAN_SMS_FLAG"
author: windows-driver-content
description: The WWAN_SMS_FLAG enumeration lists different flags to filter SMS text messages.
old-location: netvista\wwan_sms_flag.htm
old-project: netvista
ms.assetid: 6620d6c8-2b8a-440e-acf4-fb08570b13bf
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_SMS_FLAG, PWWAN_SMS_FLAG, PWWAN_SMS_FLAG enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_SMS_FLAG, WWAN_SMS_FLAG enumeration [Network Drivers Starting with Windows Vista], WwanRef_379a284f-534f-4acb-88c7-d60f7627ab32.xml, WwanSmsFlagAll, WwanSmsFlagDraft, WwanSmsFlagIndex, WwanSmsFlagMax, WwanSmsFlagNew, WwanSmsFlagOld, WwanSmsFlagSent, _WWAN_SMS_FLAG, netvista.wwan_sms_flag, wwan/PWWAN_SMS_FLAG, wwan/WWAN_SMS_FLAG, wwan/WwanSmsFlagAll, wwan/WwanSmsFlagDraft, wwan/WwanSmsFlagIndex, wwan/WwanSmsFlagMax, wwan/WwanSmsFlagNew, wwan/WwanSmsFlagOld, wwan/WwanSmsFlagSent"
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
-	WWAN_SMS_FLAG
product: Windows
targetos: Windows
req.typenames: WWAN_SMS_FLAG, *PWWAN_SMS_FLAG
req.product: Windows 10 or later.
---

# _WWAN_SMS_FLAG Enumeration
The WWAN_SMS_FLAG enumeration lists different flags to filter SMS text messages.

## Syntax
```
typedef enum _WWAN_SMS_FLAG {
  WwanSmsFlagAll    ,
  WwanSmsFlagIndex  ,
  WwanSmsFlagNew    ,
  WwanSmsFlagOld    ,
  WwanSmsFlagSent   ,
  WwanSmsFlagDraft  ,
  WwanSmsFlagMax
} WWAN_SMS_FLAG, *PWWAN_SMS_FLAG;
```

## Constants

<table>
            
                <tr>
                    <td>WwanSmsFlagAll</td>
                    <td>No filter is set.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFlagIndex</td>
                    <td>Filter based on the value of an index.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFlagNew</td>
                    <td>Filter for new (unread) messages.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFlagOld</td>
                    <td>Filter for old (read) messages.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFlagSent</td>
                    <td>Filter for sent messages.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFlagDraft</td>
                    <td>Filter for draft messages.</td>
                </tr>
            
                <tr>
                    <td>WwanSmsFlagMax</td>
                    <td>The total number of filter flags.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571245">WWAN_SMS_FILTER</a>