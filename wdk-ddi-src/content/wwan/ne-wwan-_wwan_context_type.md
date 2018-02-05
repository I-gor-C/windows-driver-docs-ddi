---
UID : NE:wwan._WWAN_CONTEXT_TYPE
title : "_WWAN_CONTEXT_TYPE"
author : windows-driver-content
description : The WWAN_CONTEXT_TYPE enumeration lists the different types of connection contexts that are supported by the MB device.
old-location : netvista\wwan_context_type.htm
old-project : netvista
ms.assetid : 73a18050-fc89-41df-82ce-0f29c5716496
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : wwan/WwanContextTypeVoice, WwanContextTypeCustom, wwan/WwanContextTypeCustom, WwanRef_2f94e3ef-ec5c-47cc-8fe0-295c517ad43a.xml, WwanContextTypePurchase, *PWWAN_CONTEXT_TYPE, WwanContextTypeVoice, wwan/WWAN_CONTEXT_TYPE, WwanContextTypeInternet, netvista.wwan_context_type, wwan/WwanContextTypePurchase, wwan/WwanContextTypeMax, WWAN_CONTEXT_TYPE enumeration [Network Drivers Starting with Windows Vista], PWWAN_CONTEXT_TYPE enumeration pointer [Network Drivers Starting with Windows Vista], WwanContextTypeMax, WwanContextTypeVpn, wwan/WwanContextTypeInternet, WwanContextTypeVideoShare, wwan/WwanContextTypeVpn, wwan/PWWAN_CONTEXT_TYPE, WWAN_CONTEXT_TYPE, wwan/WwanContextTypeVideoShare, _WWAN_CONTEXT_TYPE, wwan/WwanContextTypeNone, PWWAN_CONTEXT_TYPE, WwanContextTypeNone
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wwan.h
req.include-header : Wwan.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 8 and later versions of Windows.
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
req.typenames : "*PWWAN_CONTEXT_TYPE, WWAN_CONTEXT_TYPE"
req.product : Windows 10 or later.
---

# _WWAN_CONTEXT_TYPE Enumeration
The WWAN_CONTEXT_TYPE enumeration lists the different types of connection contexts that are supported
  by the MB device.

## Syntax
````
typedef enum _WWAN_CONTEXT_TYPE { 
  WwanContextTypeNone        = 0,
  WwanContextTypeInternet,
  WwanContextTypeVpn,
  WwanContextTypeVoice,
  WwanContextTypeVideoShare,
  WwanContextTypeCustom,
  WwanContextTypePurchase,
  WwanContextTypeMax
} WWAN_CONTEXT_TYPE, *PWWAN_CONTEXT_TYPE;
````

## Constants

<table>

<tr>
<td>WwanContextTypeAdmin</td>
<td></td>
</tr>

<tr>
<td>WwanContextTypeApp</td>
<td></td>
</tr>

<tr>
<td>WwanContextTypeCustom</td>
<td>The context represents a connection to a custom service.</td>
</tr>

<tr>
<td>WwanContextTypeEmergencyCall</td>
<td></td>
</tr>

<tr>
<td>WwanContextTypeIms</td>
<td></td>
</tr>

<tr>
<td>WwanContextTypeInternet</td>
<td>The context represents a connection to the Internet.</td>
</tr>

<tr>
<td>WwanContextTypeLteAttach</td>
<td></td>
</tr>

<tr>
<td>WwanContextTypeMax</td>
<td>The total number of supported context types.</td>
</tr>

<tr>
<td>WwanContextTypeMms</td>
<td></td>
</tr>

<tr>
<td>WwanContextTypeNone</td>
<td>The context is not yet provisioned.</td>
</tr>

<tr>
<td>WwanContextTypePurchase</td>
<td>Purchase a connection. For example, a walled garden, hot-lining or captive portal.</td>
</tr>

<tr>
<td>WwanContextTypeTethering</td>
<td></td>
</tr>

<tr>
<td>WwanContextTypeVideoShare</td>
<td>The context represents a connection to a video sharing service.</td>
</tr>

<tr>
<td>WwanContextTypeVoice</td>
<td>The context represents a connection to a Voice-over-IP (VOIP) service.</td>
</tr>

<tr>
<td>WwanContextTypeVpn</td>
<td>The context represents a connection to virtual private network (VPN to a corporate
     network).</td>
</tr>

<tr>
<td>WwanContextTypeXcap</td>
<td></td>
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

<a href="..\wwan\ns-wwan-_wwan_context.md">WWAN_CONTEXT</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_CONTEXT_TYPE enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>