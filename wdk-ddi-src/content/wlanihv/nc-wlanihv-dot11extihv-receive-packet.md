---
UID: NC.wlanihv.DOT11EXTIHV_RECEIVE_PACKET
title: DOT11EXTIHV_RECEIVE_PACKET
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvreceivepacket.htm
ms.assetid: 4a08c6dc-61ac-421f-83b7-73f1f54aea71
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvReceivePacket
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
ms.keywords: PrintPropertyValue, PrintPropertyValue
req.iface: 
req.product: Windows 10 or later.
---

# DOT11EXTIHV_RECEIVE_PACKET callback



## -description

## -prototype

````
DOT11EXTIHV_RECEIVE_PACKET Dot11ExtIhvReceivePacket;

DWORD APIENTRY Dot11ExtIhvReceivePacket(
  _In_opt_ HANDLE hIhvExtAdapter,
  _In_     DWORD  dwInBufferSize,
  _In_     LPVOID pvInBuffer
)
{ ... }
````


## -parameters
<dl>

### -param <i>hIhvExtAdapter</i> [in, optional]

<dd>
<p>The handle used by the IHV Extensions DLL to reference the WLAN adapter. This handle value was
     specified through a previous call to the 
     <a href="https://msdn.microsoft.com/96dc1718-ee35-440a-94e8-eba4a41c9559">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>dwInBufferSize</i> [in]

<dd>
<p>The length, in bytes, of the received packet referenced by the 
     <i>pvInBuffer</i> parameter.</p>
</dd>

### -param <i>pvInBuffer</i> [in]

<dd>
<p>A pointer to a buffer, allocated by the operating system, which contains the packet data, as
     described in the Remarks section.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The operating system calls the 
    <i>Dot11ExtIhvReceivePacket</i> function when the following occur:</p>

<p>The WLAN adapter receives a packet and the Native 802.11 miniport driver, which manages the adapter,
      indicates the packet to the operating system.</p>

<p>The packet's IEEE EtherType matches an entry in the list of EtherTypes specified by the IHV
      Extensions DLL through a call to the 
      <a href="https://msdn.microsoft.com/0681519e-022a-487c-ae5e-39a293b060ec">
      Dot11ExtSetEtherTypeHandling</a> function.</p>

<p>The buffer pointed to by 
    <i>pvPacket</i> should contain the following packet data, specified in network byte order:</p>

<p>MAC address of destination (6 bytes), formatted according to the guidelines discussed in 
      <a href="netvista.802_11_mac_header_management">802.11 MAC Header
      Management</a>
</p>

<p>IEEE EtherType (2 bytes)</p>

<p>Payload</p>

<p>The operating system calls the 
    <i>Dot11ExtIhvReceivePacket</i> function when the following occur:</p>

<p>The WLAN adapter receives a packet and the Native 802.11 miniport driver, which manages the adapter,
      indicates the packet to the operating system.</p>

<p>The packet's IEEE EtherType matches an entry in the list of EtherTypes specified by the IHV
      Extensions DLL through a call to the 
      <a href="https://msdn.microsoft.com/0681519e-022a-487c-ae5e-39a293b060ec">
      Dot11ExtSetEtherTypeHandling</a> function.</p>

<p>The buffer pointed to by 
    <i>pvPacket</i> should contain the following packet data, specified in network byte order:</p>

<p>MAC address of destination (6 bytes), formatted according to the guidelines discussed in 
      <a href="netvista.802_11_mac_header_management">802.11 MAC Header
      Management</a>
</p>

<p>IEEE EtherType (2 bytes)</p>

<p>Payload</p>

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
<a href="https://msdn.microsoft.com/96dc1718-ee35-440a-94e8-eba4a41c9559">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547587">Dot11ExtSetEtherTypeHandling</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_RECEIVE_PACKET callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
