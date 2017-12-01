---
UID: NC.wlanihv.DOT11EXT_SEND_PACKET
title: DOT11EXT_SEND_PACKET
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extsendpacket.htm
old-project: netvista
ms.assetid: 0672eed0-4824-464b-9f4e-93862f27d586
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
req.alt-api: Dot11ExtSendPacket
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

# DOT11EXT_SEND_PACKET callback



## -description

## -prototype

````
DWORD WINAPI * Dot11ExtSendPacket(
  _In_opt_ HANDLE hDot11SvcHandle,
  _In_     ULONG  uPacketLen,
  _In_     LPVOID pvPacket,
  _In_opt_ HANDLE hSendCompletion
);
````


## -parameters
<dl>

### -param <i>hDot11SvcHandle</i> [in, optional]

<dd>
<p>The handle used by the operating system to reference the WLAN adapter. This handle value was
     specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>uPacketLen</i> [in]

<dd>
<p>The length, in bytes, of the caller-allocated buffer referenced by the 
     <i>pvPacket</i> parameter.</p>
</dd>

### -param <i>pvPacket</i> [in]

<dd>
<p>A pointer to a caller-allocated buffer that contains the data to be transmitted, as described in
     the Remarks section.</p>
</dd>

### -param <i>hSendCompletion</i> [in, optional]

<dd>
<p>A handle value that uniquely identifies the send packet. 
     </p>
<p>When the WLAN adapter completes the send operation, the operating system notifies the IHV Extensions
     DLL through a call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-send-packet-completion.md">
     Dot11ExtIhvSendPacketCompletion</a> IHV Handler function. When making this call, the operating system
     passes the handle value of the packet through the 
     <i>hSendCompletion</i> parameter.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The IHV Extensions DLL must follow these guidelines when calling the 
    <b>Dot11ExtSendPacket</b> function.</p>

<p>The packet sent through a call of the 
      <b>Dot11ExtSendPacket</b> function will complete asynchronously. The IHV
      Extensions DLL must not free the memory referenced by the 
      <i>pvPacket</i> parameter until the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-send-packet-completion.md">
      Dot11ExtIhvSendPacketCompletion</a> IHV Handler function is called with the same handle value as the 
      <i>hSendCompletion</i> parameter.</p>

<p>The IHV Extensions DLL must set the 
      <i>hSendCompletion</i> parameter to a value that uniquely identifies the packet data that is referenced
      by the 
      <i>pvPacket</i> parameter.</p>

<p>For more information about the IHV Handler functions, see 
    <a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
    Functions</a>.</p>

<p>The buffer pointed to by 
    <i>pvPacket</i> should contain the following packet data, specified in network byte order:</p>

<p>MAC address of destination (6 bytes), formatted according to the guidelines discussed in 
      <a href="netvista.802_11_mac_header_management">802.11 MAC Header
      Management</a>
</p>

<p>IEEE EtherType (2 bytes)</p>

<p>Payload</p>

<p>This packet data is passed to the miniport driver.</p>

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
<a href="NULL">802.11 MAC Header Management</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-send-packet-completion.md">
   Dot11ExtIhvSendPacketCompletion</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
   Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_SEND_PACKET callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
