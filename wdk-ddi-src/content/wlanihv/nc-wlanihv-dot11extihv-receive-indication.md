---
UID: NC.wlanihv.DOT11EXTIHV_RECEIVE_INDICATION
title: DOT11EXTIHV_RECEIVE_INDICATION
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvreceiveindication.htm
old-project: netvista
ms.assetid: b4d5c33e-563d-459c-90da-a2912c82d1cd
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvReceiveIndication
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

# DOT11EXTIHV_RECEIVE_INDICATION callback



## -description

## -prototype

````
DOT11EXTIHV_RECEIVE_INDICATION Dot11ExtIhvReceiveIndication;

DWORD APIENTRY Dot11ExtIhvReceiveIndication(
  _In_opt_ HANDLE                       hIhvExtAdapter,
  _In_     DOT11EXT_IHV_INDICATION_TYPE indicationType,
  _In_     ULONG                        uBufferLength,
  _In_opt_ LPVOID                       pvBuffer
)
{ ... }
````


## -parameters
<dl>

### -param <i>hIhvExtAdapter</i> [in, optional]

<dd>
<p>The handle used by the IHV Extensions DLL to reference the WLAN adapter. This handle value was
     specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>indicationType</i> [in]

<dd>
<p>The 
     <a href="..\wlanihv\ne-wlanihv--dot11ext-ihv-indication-type.md">
     DOT11EXT_IHV_INDICATION_TYPE</a> indication type.</p>
</dd>

### -param <i>uBufferLength</i> [in]

<dd>
<p>The length, in bytes, of the data within the buffer that is referenced by the 
     <i>pvBuffer</i> parameter.</p>
</dd>

### -param <i>pvBuffer</i> [in, optional]

<dd>
<p>The pointer to a buffer, allocated by the operating system, which contains the notification data.
     The IHV is responsible for defining the format of the notification data.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>When the Native 802.11 miniport driver, which manages the WLAN adapter, makes an 
    <a href="netvista.ndis_status_media_specific_indication">
    NDIS_STATUS_MEDIA_SPECIFIC_INDICATION</a> indication, the operating system forwards the notification
    data to the IHV Extensions DLL by calling the 
    <i>Dot11ExtIhvReceiveIndication</i> function.</p>

<p>When the Native 802.11 miniport driver, which manages the WLAN adapter, makes an 
    <a href="netvista.ndis_status_media_specific_indication">
    NDIS_STATUS_MEDIA_SPECIFIC_INDICATION</a> indication, the operating system forwards the notification
    data to the IHV Extensions DLL by calling the 
    <i>Dot11ExtIhvReceiveIndication</i> function.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547626">DOT11EXT_IHV_INDICATION_TYPE</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="netvista.ndis_status_media_specific_indication">
   NDIS_STATUS_MEDIA_SPECIFIC_INDICATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_RECEIVE_INDICATION callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
