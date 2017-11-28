---
UID: NC.wlanihv.DOT11EXT_REQUEST_VIRTUAL_STATION
title: DOT11EXT_REQUEST_VIRTUAL_STATION
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extrequestvirtualstation.htm
old-project: netvista
ms.assetid: a7f6d53a-439e-4274-80b0-9fb183459824
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtRequestVirtualStation
req.alt-loc: wlanihv.h
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
req.iface: 
req.product: Windows 10 or later.
---

# DOT11EXT_REQUEST_VIRTUAL_STATION callback



## -description

## -prototype

````
DWORD WINAPI * Dot11ExtRequestVirtualStation(
  _In_opt_   HANDLE hDot11PrimaryHandle,
  _Reserved_ LPVOID pvReserved
);
````


## -parameters
<dl>

### -param <i>hDot11PrimaryHandle</i> [in, optional]

<dd>
<p>A handle used by the operating system to reference the primary physical wireless LAN (WLAN)
     adapter. This handle value was received as the 
     <i>hDot11SvcHandle</i> parameter through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>pvReserved</i> 

<dd>
<p>This parameter is reserved for use by the operating system and should be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>When this request function completes successfully, the operating system begins to process the request
    to create a virtual station. It is possible that the operating system will call the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
    Handler function to initialize the virtual station before or after the call to 
    <b>Dot11ExtRequestVirtualStation</b> returns.</p>

<p>After the operating system creates the new virtual station, the IHV Extensions DLL should expect to
    receive a call to the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
    Handler function. In this call, the operating system passes a handle to the new virtual adapter through
    the 
    <i>hDot11SvcHandle</i> parameter.</p>

<p>When this request function completes successfully, the operating system begins to process the request
    to create a virtual station. It is possible that the operating system will call the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
    Handler function to initialize the virtual station before or after the call to 
    <b>Dot11ExtRequestVirtualStation</b> returns.</p>

<p>After the operating system creates the new virtual station, the IHV Extensions DLL should expect to
    receive a call to the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
    Handler function. In this call, the operating system passes a handle to the new virtual adapter through
    the 
    <i>hDot11SvcHandle</i> parameter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wlanihv.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-release-virtual-station.md">
   Dot11ExtReleaseVirtualStation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_REQUEST_VIRTUAL_STATION callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
