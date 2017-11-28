---
UID: NC.wlanihv.DOT11EXTIHV_INIT_VIRTUAL_STATION
title: DOT11EXTIHV_INIT_VIRTUAL_STATION
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvinitvirtualstation.htm
old-project: netvista
ms.assetid: 1e18515c-2f24-4690-b5fd-0915ef30307b
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
req.alt-api: Dot11ExtIhvInitVirtualStation
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

# DOT11EXTIHV_INIT_VIRTUAL_STATION callback



## -description

## -prototype

````
DOT11EXTIHV_INIT_VIRTUAL_STATION Dot11ExtIhvInitVirtualStation;

DWORD APIENTRY Dot11ExtIhvInitVirtualStation(
  _In_       PDOT11EXT_VIRTUAL_STATION_APIS pDot11ExtVSAPI,
  _Reserved_ LPVOID                         pvReserved
)
{ ... }
````


## -parameters
<dl>

### -param <i>pDot11ExtVSAPI</i> [in]

<dd>
<p>A pointer to a 
     <a href="..\wlanihv\ns-wlanihv--dot11ext-virtual-station-apis.md">
     DOT11EXT_VIRTUAL_STATION_APIS</a> structure, which contains the addresses of the IHV Extensibility
     virtual station functions that are supported by the operating system. The operating system formats this
     parameter with the function addresses before making a call to the 
     <i>Dot11ExtIhvInitVirtualStation</i> function.</p>
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
<p>It is optional for the IHV Extensions DLL to implement and export this function.</p>

<p>The operating system calls the 
    <i>Dot11ExtIhvInitVirtualStation</i> function immediately after it calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-service.md">Dot11ExtIhvInitService</a> function,
    but before it calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">
    Dot11ExtIhvInitAdapter</a> function.</p>

<p>In response to a call to 
    <i>Dot11ExtIhvInitVirtualStation</i>, the IHV Extensions DLL can initialize its internal data structures
    with the information provided from the 
    <i>Dot11ExtIhvInitService</i> function call.</p>

<p>The operating system resolves the address of the 
    <i>Dot11ExtIhvInitVirtualStation</i> function by calling the 
    <b>GetProcAddress</b> function. As a result, the developer of the IHV Extensions DLL must follow these
    guidelines if this function is implemented.</p>

<p>The DLL must implement a function named Dot11ExtIhvInitVirtualStation, which has the format that is
      described in this topic.</p>

<p>The 
      <b>EXPORTS</b> statement of the source module-definition (.def) file, which is used to build the IHV
      Extensions DLL, must contain a function name entry for the 
      <i>Dot11ExtIhvInitVirtualStation</i> function.</p>

<p>For more information about 
    <b>GetProcAddress</b>, see the Microsoft Windows SDK documentation.</p>

<p>It is optional for the IHV Extensions DLL to implement and export this function.</p>

<p>The operating system calls the 
    <i>Dot11ExtIhvInitVirtualStation</i> function immediately after it calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-service.md">Dot11ExtIhvInitService</a> function,
    but before it calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">
    Dot11ExtIhvInitAdapter</a> function.</p>

<p>In response to a call to 
    <i>Dot11ExtIhvInitVirtualStation</i>, the IHV Extensions DLL can initialize its internal data structures
    with the information provided from the 
    <i>Dot11ExtIhvInitService</i> function call.</p>

<p>The operating system resolves the address of the 
    <i>Dot11ExtIhvInitVirtualStation</i> function by calling the 
    <b>GetProcAddress</b> function. As a result, the developer of the IHV Extensions DLL must follow these
    guidelines if this function is implemented.</p>

<p>The DLL must implement a function named Dot11ExtIhvInitVirtualStation, which has the format that is
      described in this topic.</p>

<p>The 
      <b>EXPORTS</b> statement of the source module-definition (.def) file, which is used to build the IHV
      Extensions DLL, must contain a function name entry for the 
      <i>Dot11ExtIhvInitVirtualStation</i> function.</p>

<p>For more information about 
    <b>GetProcAddress</b>, see the Microsoft Windows SDK documentation.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547617">DOT11EXT_APIS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547625">DOT11EXT_IHV_HANDLERS</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-get-version-info.md">Dot11ExtIhvGetVersionInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_INIT_VIRTUAL_STATION callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
