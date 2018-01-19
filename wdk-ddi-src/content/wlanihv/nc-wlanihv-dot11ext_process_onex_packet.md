---
UID : NC:wlanihv.DOT11EXT_PROCESS_ONEX_PACKET
title : DOT11EXT_PROCESS_ONEX_PACKET
author : windows-driver-content
description : Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location : netvista\dot11extprocessonexpacket.htm
old-project : netvista
ms.assetid : 796c2976-b7b1-49ea-bf23-c018efd228ee
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _DRIVER_INFO_8W, *LPDRIVER_INFO_8W, *PDRIVER_INFO_8W, DRIVER_INFO_8W, DRIVER_INFO_8
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wlanihv.h
req.include-header : Wlanihv.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : Dot11ExtProcessOneXPacket
req.alt-loc : wlanihv.h
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
req.typenames : "*LPDRIVER_INFO_8W, *PDRIVER_INFO_8W, DRIVER_INFO_8W"
req.product : Windows 10 or later.
---


# DOT11EXT_PROCESS_ONEX_PACKET callback function


## Syntax

```
DOT11EXT_PROCESS_ONEX_PACKET Dot11extProcessOnexPacket;

DWORD Dot11extProcessOnexPacket(
  HANDLE hDot11SvcHandle,
  DWORD dwInPacketSize,
  LPVOID pvInPacket
)
{...}
```

## Parameters

`hDot11SvcHandle`

The handle used by the operating system to reference the wireless LAN (WLAN) adapter. This handle
     value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.

`dwInPacketSize`

The length, in bytes, of the packet data within the buffer that is referenced by the 
     <i>pvInPacket</i> parameter.

`pvInPacket`

The EAPOL packet received from the AP. The 
     <i>pvInPacket</i> parameter must reference the EAPOL packet starting from the packet type field in the
     EAPOL protocol data unit (PDU). For more information about the EAPOL packet type field, refer to Clause
     7.5.4 in the IEEE 802.1X-2001 standard.


## Return Value

If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.

## Remarks

When it calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11ext_onex_start.md">Dot11ExtStartOneX</a> function, the IHV
    Extensions DLL initiates an 802.1X authentication operation by using the 802.1X module of the Native
    802.11 framework. This allows the DLL to use the standard extensible authentication protocol (EAP)
    algorithms that are supported by the operating system.

While the 802.1X authentication operation is pending, the IHV Extensions DLL forwards received EAP
    over LAN (EAPOL) packets to the operating system through a call to the 
    <b>Dot11ExtProcessOneXPacket</b> function. The IHV Extensions DLL receives these
    packets through the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv_receive_packet.md">Dot11ExtIhvReceivePacket</a> IHV
    Handler function.

For more information about EAPOL packets, refer to Clause 7 of the IEEE 802.1X-2001 standard.

For more information about using the 802.1X module for authentication, see 
    <a href="netvista.interface_to_the_native_802_11_802_1x_module">Interface to the Native
    802.11 802.1X Module</a>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wlanihv.h (include Wlanihv.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv_onex_indicate_result.md">
   Dot11ExtIhvOneXIndicateResult</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv_receive_packet.md">Dot11ExtIhvReceivePacket</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext_onex_start.md">Dot11ExtStartOneX</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext_onex_stop.md">Dot11ExtStopOneX</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_PROCESS_ONEX_PACKET callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>