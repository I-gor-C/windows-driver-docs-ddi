---
UID : NC:wlanihv.DOT11EXT_REQUEST_VIRTUAL_STATION
title : DOT11EXT_REQUEST_VIRTUAL_STATION
author : windows-driver-content
description : Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location : netvista\dot11extrequestvirtualstation.htm
old-project : netvista
ms.assetid : a7f6d53a-439e-4274-80b0-9fb183459824
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
req.alt-api : Dot11ExtRequestVirtualStation
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


# DOT11EXT_REQUEST_VIRTUAL_STATION callback function


## Syntax

```
DOT11EXT_REQUEST_VIRTUAL_STATION Dot11extRequestVirtualStation;

DWORD Dot11extRequestVirtualStation(
  HANDLE hDot11PrimaryHandle,
  LPVOID pvReserved
)
{...}
```

## Parameters

`hDot11PrimaryHandle`

A handle used by the operating system to reference the primary physical wireless LAN (WLAN)
     adapter. This handle value was received as the 
     <i>hDot11SvcHandle</i> parameter through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.

`pvReserved`

This parameter is reserved for use by the operating system and should be <b>NULL</b>.


## Return Value

If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.

## Remarks

When this request function completes successfully, the operating system begins to process the request
    to create a virtual station. It is possible that the operating system will call the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a> IHV
    Handler function to initialize the virtual station before or after the call to 
    <b>Dot11ExtRequestVirtualStation</b> returns.

After the operating system creates the new virtual station, the IHV Extensions DLL should expect to
    receive a call to the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a> IHV
    Handler function. In this call, the operating system passes a handle to the new virtual adapter through
    the 
    <i>hDot11SvcHandle</i> parameter.

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
<a href="..\wlanihv\nc-wlanihv-dot11ext_release_virtual_station.md">
   Dot11ExtReleaseVirtualStation</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_REQUEST_VIRTUAL_STATION callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>