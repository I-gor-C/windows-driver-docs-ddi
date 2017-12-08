---
UID: NC.wlanihv.DOT11EXT_SEND_UI_REQUEST
title: DOT11EXT_SEND_UI_REQUEST
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extsenduirequest.htm
old-project: netvista
ms.assetid: c8d2ff26-d233-4683-9811-c23896203bd5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtSendUIRequest
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

# DOT11EXT_SEND_UI_REQUEST callback



## -description

## -prototype

````
DWORD WINAPI * Dot11ExtSendUIRequest(
  _In_opt_ HANDLE                   hDot11SvcHandle,
  _In_     PDOT11EXT_IHV_UI_REQUEST pIhvUIRequest
);
````


## -parameters
<dl>

### -param hDot11SvcHandle [in, optional]

<dd>
<p>The handle used by the operating system to reference the wireless LAN (WLAN) adapter. This handle
     value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param pIhvUIRequest [in]

<dd>
<p>A pointer to a caller-allocated buffer, formatted as a 
     <a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-ui-request.md">
     DOT11EXT_IHV_UI_REQUEST</a> structure.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The IHV Extensions DLL must follow these guidelines when calling the 
    <b>Dot11ExtSendUIRequest</b> function.</p>

<p>Requests for event notification by the 
      <a href="netvista.native_802_11_ihv_ui_extensions_dll">Native 802.11 IHV UI Extensions
      DLL</a> are completed through a call to the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-process-ui-response.md">
      Dot11ExtIhvProcessUIResponse</a> IHV Handler function. The IHV Extensions DLL must not free the
      memory referenced by the 
      <i>pIhvUIRequest</i> parameter until the request is completed.</p>

<p>If the operating system calls the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-adapter-reset.md">Dot11ExtIhvAdapterReset</a> or 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">Dot11ExtIhvDeinitAdapter</a> IHV
      handler functions, the IHV Extensions DLL can assume that the UI request has been canceled. In this
      situation, the DLL must free the memory referenced by the 
      <i>pIhvUIRequest</i> parameter.</p>

<p>The operating system can query the completion status of the request through a call to the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-is-ui-request-pending.md">
      Dot11ExtIhvIsUIRequestPending</a> IHV Handler function.</p>

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
<a href="..\wlanihv\nc-wlanihv-dot11extihv-adapter-reset.md">Dot11ExtIhvAdapterReset</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">Dot11ExtIhvDeinitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-is-ui-request-pending.md">
   Dot11ExtIhvIsUIRequestPending</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-process-ui-response.md">
   Dot11ExtIhvProcessUIResponse</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_SEND_UI_REQUEST callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
