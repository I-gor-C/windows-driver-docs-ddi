---
UID: NE:wwan._WWAN_CONTEXT_TYPE
title: "_WWAN_CONTEXT_TYPE"
author: windows-driver-content
description: The WWAN_CONTEXT_TYPE enumeration lists the different types of connection contexts that are supported by the MB device.
old-location: netvista\wwan_context_type.htm
old-project: netvista
ms.assetid: 73a18050-fc89-41df-82ce-0f29c5716496
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_CONTEXT_TYPE, PWWAN_CONTEXT_TYPE, PWWAN_CONTEXT_TYPE enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_CONTEXT_TYPE, WWAN_CONTEXT_TYPE enumeration [Network Drivers Starting with Windows Vista], WwanContextTypeCustom, WwanContextTypeInternet, WwanContextTypeMax, WwanContextTypeNone, WwanContextTypePurchase, WwanContextTypeVideoShare, WwanContextTypeVoice, WwanContextTypeVpn, WwanRef_2f94e3ef-ec5c-47cc-8fe0-295c517ad43a.xml, _WWAN_CONTEXT_TYPE, netvista.wwan_context_type, wwan/PWWAN_CONTEXT_TYPE, wwan/WWAN_CONTEXT_TYPE, wwan/WwanContextTypeCustom, wwan/WwanContextTypeInternet, wwan/WwanContextTypeMax, wwan/WwanContextTypeNone, wwan/WwanContextTypePurchase, wwan/WwanContextTypeVideoShare, wwan/WwanContextTypeVoice, wwan/WwanContextTypeVpn"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
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
-	WWAN_CONTEXT_TYPE
product:
- Windows
targetos: Windows
req.typenames: WWAN_CONTEXT_TYPE, *PWWAN_CONTEXT_TYPE
req.product: Windows 10 or later.
---

# _WWAN_CONTEXT_TYPE Enumeration
The WWAN_CONTEXT_TYPE enumeration lists the different types of connection contexts that are supported
  by the MB device.

## Syntax
```
typedef enum _WWAN_CONTEXT_TYPE {
  WwanContextTypeNone           ,
  WwanContextTypeInternet       ,
  WwanContextTypeVpn            ,
  WwanContextTypeVoice          ,
  WwanContextTypeVideoShare     ,
  WwanContextTypeCustom         ,
  WwanContextTypePurchase       ,
  WwanContextTypeMms            ,
  WwanContextTypeIms            ,
  WwanContextTypeAdmin          ,
  WwanContextTypeApp            ,
  WwanContextTypeXcap           ,
  WwanContextTypeTethering      ,
  WwanContextTypeEmergencyCall  ,
  WwanContextTypeLteAttach      ,
  WwanContextTypeMax
} WWAN_CONTEXT_TYPE, *PWWAN_CONTEXT_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>WwanContextTypeNone</td>
                    <td>The context is not yet provisioned.</td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeInternet</td>
                    <td>The context represents a connection to the Internet.</td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeVpn</td>
                    <td>The context represents a connection to virtual private network (VPN to a corporate
     network).</td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeVoice</td>
                    <td>The context represents a connection to a Voice-over-IP (VOIP) service.</td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeVideoShare</td>
                    <td>The context represents a connection to a video sharing service.</td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeCustom</td>
                    <td>The context represents a connection to a custom service.</td>
                </tr>
            
                <tr>
                    <td>WwanContextTypePurchase</td>
                    <td>Purchase a connection. For example, a walled garden, hot-lining or captive portal.</td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeMms</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeIms</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeAdmin</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeApp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeXcap</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeTethering</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeEmergencyCall</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeLteAttach</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanContextTypeMax</td>
                    <td>The total number of supported context types.</td>
                </tr>
</table>

## Remarks

This enumeration indicates the usage of the provisioned context. For example, whether the context is
    used to connect to the Internet, or to a VPN into a corporate network. Miniport driver should specify 
    <b>WwanContextTypeNone</b> for empty (unprovisioned) context slots.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 8 and later versions of Windows. Available in Windows 8 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571201">WWAN_CONTEXT</a>