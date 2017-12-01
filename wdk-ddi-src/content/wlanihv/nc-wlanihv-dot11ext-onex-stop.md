---
UID: NC.wlanihv.DOT11EXT_ONEX_STOP
title: DOT11EXT_ONEX_STOP
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extstoponex.htm
old-project: netvista
ms.assetid: b4893698-47ae-4888-9dcd-0dbdf051266b
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: Dot11ExtStopOneX
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

# DOT11EXT_ONEX_STOP callback



## -description

## -prototype

````
DWORD WINAPI * Dot11ExtStopOneX(
  _In_opt_ HANDLE hDot11SvcHandle
);
````


## -parameters
<dl>

### -param <i>hDot11SvcHandle</i> [in, optional]

<dd>
<p>The handle used by the operating system to reference the wireless LAN (WLAN) adapter. This handle
     value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>When it calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11ext-onex-start.md">Dot11ExtStartOneX</a> function, the IHV
    Extensions DLL initiates an 802.1X authentication operation by using the 802.1X module of the Native
    802.11 framework. This allows the DLL to use the standard extensible authentication protocol (EAP)
    algorithms that are supported by the operating system.</p>

<p>Before the 802.1X authentication operation completes, the IHV Extensions DLL can call the 
    <b>Dot11ExtStopOneX</b> function to cancel the operation.</p>

<p>When calling the 
    <b>Dot11ExtStopOneX</b> function, the IHV Extensions DLL must follow these
    guidelines.</p>

<p><b>Dot11ExtStopOneX</b> can only be called while an 802.1X authentication
      operation is pending. The IHV Extensions DLL initiates the authentication with the AP by calling 
      <a href="..\wlanihv\nc-wlanihv-dot11ext-onex-start.md">Dot11ExtStartOneX</a>. When the 802.1X
      authentication operation is completed, the operating system calls the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
      Dot11ExtIhvOneXIndicateResult</a> IHV Handler function.</p>

<p>After the IHV Extensions DLL calls 
      <b>Dot11ExtStopOneX</b>, it must not call 
      <a href="..\wlanihv\nc-wlanihv-dot11ext-process-onex-packet.md">Dot11ExtProcessOneXPacket</a> to
      forward 802.1X EAP over LAN (EAPOL) packets to the operating system. For more information about EAPOL
      packets, refer to Clause 7 of the IEEE 802.1X-2001 standard.</p>

<p>For more information about using the 802.1X module for authentication, see 
    <a href="netvista.interface_to_the_native_802_11_802_1x_module">Interface to the Native
    802.11 802.1X Module</a>.</p>

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
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
   Dot11ExtIhvOneXIndicateResult</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-post-associate.md">
   Dot11ExtIhvPerformPostAssociate</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-packet.md">Dot11ExtIhvReceivePacket</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-onex-start.md">Dot11ExtStartOneX</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-post-associate-completion.md">
   Dot11ExtPostAssociateCompletion</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-process-onex-packet.md">Dot11ExtProcessOneXPacket</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_ONEX_STOP callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
