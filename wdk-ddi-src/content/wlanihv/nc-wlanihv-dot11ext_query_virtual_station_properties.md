---
UID : NC:wlanihv.DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES
title : DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES
author : windows-driver-content
description : Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location : netvista\dot11extqueryvirtualstationproperties.htm
old-project : netvista
ms.assetid : 4ea71ef7-c897-413c-a542-e8068bcc66a6
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _DRIVER_INFO_8W, *LPDRIVER_INFO_8W, *PDRIVER_INFO_8W, DRIVER_INFO_8W, DRIVER_INFO_8
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wlanihv.h
req.include-header : Wlanihv.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows 7 and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : Dot11ExtQueryVirtualStationProperties
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


# DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES callback function


## Syntax

```
DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES Dot11extQueryVirtualStationProperties;

DWORD Dot11extQueryVirtualStationProperties(
  HANDLE hDot11SvcHandle,
  BOOL *pbIsVirtualStation,
  GUID *pgPrimary,
  LPVOID pvReserved
)
{...}
```

## Parameters

`hDot11SvcHandle`

A handle used by the operating system to reference the primary physical wireless LAN (WLAN)
     adapter. This handle value was received as the 
     <i>hDot11SvcHandle</i> parameter through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.

`*pbIsVirtualStation`



`*pgPrimary`



`pvReserved`

This parameter is reserved for use by the operating system and should be <b>NULL</b>.


## Return Value

If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.


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
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>