---
UID: NS.wsk._WSK_TRANSPORT
title: WSK_TRANSPORT
author: windows-driver-content
description: The WSK_TRANSPORT structure specifies an available transport that is supported by the WSK subsystem.
old-location: netvista\wsk_transport.htm
ms.assetid: aaf7b5ac-0401-4b6a-a478-3d50559817db
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WSK_TRANSPORT
req.alt-loc: wsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WSK_TRANSPORT, WSK_TRANSPORT, *PWSK_TRANSPORT
req.iface: 
req.product: Windows 10 or later.
---

# WSK_TRANSPORT structure



## -description
<p>The WSK_TRANSPORT structure specifies an available transport that is supported by the WSK
  subsystem.</p>


## -syntax

````
typedef struct _WSK_TRANSPORT {
  USHORT         Version;
  USHORT         SocketType;
  ULONG          Protocol;
  ADDRESS_FAMILY AddressFamily;
  GUID           ProviderId;
} WSK_TRANSPORT, *PWSK_TRANSPORT;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the transport. The format of the version number is transport-specific.</p>
</dd>

### -field <b>SocketType</b>

<dd>
<p>The type of socket that is supported by the transport. This member can be one of the following:
     </p>
<p></p>
<dl>

### -field <a id="SOCK_STREAM"></a><a id="sock_stream"></a>SOCK_STREAM

<dd>
<p>Supports reliable connection-oriented byte stream communication.</p>
</dd>

### -field <a id="SOCK_DGRAM"></a><a id="sock_dgram"></a>SOCK_DGRAM

<dd>
<p>Supports unreliable connectionless datagram communication.</p>
</dd>

### -field <a id="SOCK_RAW"></a><a id="sock_raw"></a>SOCK_RAW

<dd>
<p>Supports raw access to the transport protocol.</p>
</dd>
</dl>
<p>For more information about the socket types that are supported for each supported address family, see
     
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571151">WSK Address Families</a>.</p>
</dd>

### -field <b>Protocol</b>

<dd>
<p>The protocol that is supported by the transport. For more information about the protocols that are
     supported for each supported address family, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571151">WSK Address Families</a>.</p>
</dd>

### -field <b>AddressFamily</b>

<dd>
<p>The address family that is supported by the transport. For more information about supported
     address families, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571151">WSK Address Families</a>.</p>
</dd>

### -field <b>ProviderId</b>

<dd>
<p>The identifier of the transport provider that implements the transport.</p>
</dd>
</dl>

## -remarks
<p>A WSK application passes a pointer to an array of WSK_TRANSPORT structures to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571126">WskControlClient</a> function when specifying
    the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571195">WSK_TRANSPORT_LIST_QUERY</a> control
    code. The WSK subsystem fills in the array with the list of available transports that can be used for
    socket communication. When a WSK application calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a> function to create a new
    socket, it can pass the values contained in the 
    <b>AddressFamily</b>, 
    <b>SocketType</b>, and 
    <b>Protocol</b> members of a returned WSK_TRANSPORT structure for the 
    <i>AddressFamily</i>, 
    <i>SocketType</i>, and 
    <i>Protocol</i> parameters.</p>

<p>A single transport provider can support multiple combinations of values for the 
    <b>AddressFamily</b>, 
    <b>SocketType</b>, and 
    <b>Protocol</b> members.</p>

## -requirements
<table>
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
<dt>Wsk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571126">WskControlClient</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_TRANSPORT structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
