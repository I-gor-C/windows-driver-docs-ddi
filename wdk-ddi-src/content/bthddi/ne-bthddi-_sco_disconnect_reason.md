---
UID: NE:bthddi._SCO_DISCONNECT_REASON
title: "_SCO_DISCONNECT_REASON"
author: windows-driver-content
description: The SCO_DISCONNECT_REASON enumeration type gives the reason an SCO channel has been disconnected.
old-location: bltooth\sco_disconnect_reason.htm
old-project: bltooth
ms.assetid: bca4bfc6-d44f-4b10-a30a-ba2acefad7a9
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PSCO_DISCONNECT_REASON, PSCO_DISCONNECT_REASON, PSCO_DISCONNECT_REASON enumeration pointer [Bluetooth Devices], SCO_DISCONNECT_REASON, SCO_DISCONNECT_REASON enumeration [Bluetooth Devices], ScoDisconnectRequest, ScoHardwareRemoval, ScoHciDisconnect, ScoRadioPoweredDown, _SCO_DISCONNECT_REASON, bltooth.sco_disconnect_reason, bth_enums_ea951efc-1250-4414-9592-2bffe239dc95.xml, bthddi/PSCO_DISCONNECT_REASON, bthddi/SCO_DISCONNECT_REASON, bthddi/ScoDisconnectRequest, bthddi/ScoHardwareRemoval, bthddi/ScoHciDisconnect, bthddi/ScoRadioPoweredDown"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows Vista and later versions of Windows.
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
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	bthddi.h
api_name:
-	SCO_DISCONNECT_REASON
product: Windows
targetos: Windows
req.typenames: SCO_DISCONNECT_REASON, *PSCO_DISCONNECT_REASON
---

# _SCO_DISCONNECT_REASON Enumeration
The SCO_DISCONNECT_REASON enumeration type gives the reason an SCO channel has been
  disconnected.

## Syntax
```
typedef enum _SCO_DISCONNECT_REASON {
  ScoHciDisconnect      ,
  ScoDisconnectRequest  ,
  ScoRadioPoweredDown   ,
  ScoHardwareRemoval
} SCO_DISCONNECT_REASON, *PSCO_DISCONNECT_REASON;
```

## Constants

<table>
            
                <tr>
                    <td>ScoHciDisconnect</td>
                    <td>This value specifies to the profile driver that the Bluetooth driver stack has received a
     disconnect notification from the host controller interface (HCI) layer.</td>
                </tr>
            
                <tr>
                    <td>ScoDisconnectRequest</td>
                    <td>This value specifies to the profile driver that a disconnect request has been received from the
     remote device.</td>
                </tr>
            
                <tr>
                    <td>ScoRadioPoweredDown</td>
                    <td>This value specifies to the profile driver that the local radio has been turned off.</td>
                </tr>
            
                <tr>
                    <td>ScoHardwareRemoval</td>
                    <td>This value specifies to the profile driver that the local radio has been physically
     removed.</td>
                </tr>
</table>

## Remarks

A value from this enumeration is used as the 
    <b>Reason</b> member of the 
    <a href="https://msdn.microsoft.com/2d3ae219-8a40-476c-b8eb-94f4c0566527">
    SCO_INDICATION_PARAMETERS</a> structure.

Hardware limitations may prevent the Bluetooth driver stack from distinguishing between 
    <b>ScoRadioPoweredDown</b> and 
    <b>ScoHardwareRemoval</b> events.

Currently, 
    <i>ScoHciDisconnect</i> is the only value the Bluetooth driver stack passes to the 
    <a href="https://msdn.microsoft.com/abc9fc88-6852-4bfb-8271-7a73a508c397">SCO Callback Function</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista and later versions of Windows. Versions:\_Supported in Windows Vista and later versions of Windows. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="https://msdn.microsoft.com/abc9fc88-6852-4bfb-8271-7a73a508c397">SCO Callback Function</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536779">SCO_INDICATION_PARAMETERS</a>