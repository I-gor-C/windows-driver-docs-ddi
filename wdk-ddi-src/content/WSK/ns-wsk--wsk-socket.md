---
UID: NS.wsk._WSK_SOCKET
title: WSK_SOCKET
author: windows-driver-content
description: The WSK_SOCKET structure defines a socket object for a socket.
old-location: netvista\wsk_socket.htm
ms.assetid: dce4a087-a14b-400b-bdc1-944c1d4d492a
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
req.alt-api: WSK_SOCKET
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
ms.keywords: WSK_SOCKET, WSK_SOCKET, *PWSK_SOCKET
req.iface: 
req.product: Windows 10 or later.
---

# WSK_SOCKET structure



## -description
<p>The WSK_SOCKET structure defines a socket object for a socket.</p>


## -syntax

````
typedef struct _WSK_SOCKET {
  const VOID *Dispatch;
} WSK_SOCKET, *PWSK_SOCKET;
````


## -struct-fields
<dl>

### -field <b>Dispatch</b>

<dd>
<p>A pointer to a constant provider dispatch structure. This structure is a dispatch table that
     contains pointers to a socket's functions. Depending on the WSK 
     <a href="netvista.winsock_kernel_socket_categories">socket category</a> of the
     socket, this pointer is a pointer to one of the following structures:
     </p>
<table>
<tr>
<th>Socket category</th>
<th>Dispatch table structure</th>
</tr>
<tr>
<td>
<p>Basic socket</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/15cd5336-fe29-4a59-8071-04c802552a5a">
         WSK_PROVIDER_BASIC_DISPATCH</a>
</p>
</td>
</tr>
<tr>
<td>
<p>Listening socket</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/56df7cb9-9ae7-4249-9583-a9259e604238">
         WSK_PROVIDER_LISTEN_DISPATCH</a>
</p>
</td>
</tr>
<tr>
<td>
<p>Datagram socket</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/fa8d3395-b800-4e5c-af03-b21520f69158">
         WSK_PROVIDER_DATAGRAM_DISPATCH</a>
</p>
</td>
</tr>
<tr>
<td>
<p>Connection-oriented socket</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/70a86809-07f2-4723-9e50-4dbdd31ff900">
         WSK_PROVIDER_CONNECTION_DISPATCH</a>
</p>
</td>
</tr>
<tr>
<td>
<p>Stream socket</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/A10B901E-9987-40E9-976B-4CD9455E0AEE">
         WSK_PROVIDER_STREAM_DISPATCH</a>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>The WSK subsystem allocates and fills in a WSK_SOCKET structure whenever a new socket is created. A
    WSK application receives a pointer to the WSK_SOCKET structure for a socket from the WSK subsystem in one
    of the following ways:</p>

<p>The WSK application calls the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a> function to create a socket.</p>

<p>The WSK application calls the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a> function to create,
      bind, and connect a connection-oriented socket.</p>

<p>The WSK application calls the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff571109">WskAccept</a> function to accept an incoming
      connection-oriented socket on a listening socket.</p>

<p>The WSK subsystem calls the WSK application's 
      <a href="https://msdn.microsoft.com/672440f0-810a-4e68-82a5-d038770898c5">WskAcceptEvent</a> event callback function to
      notify the WSK application that an incoming connection-oriented socket has been accepted on a listening
      socket.</p>

<p>A WSK application passes the pointer to a socket's WSK_SOCKET structure when calling any of the
    socket's functions.</p>

<p>The WSK subsystem frees the memory for the WSK_SOCKET structure when the WSK application calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a> function to close the
    socket.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571109">WskAccept</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571150">WskSocketConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/672440f0-810a-4e68-82a5-d038770898c5">WskAcceptEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571171">WSK_PROVIDER_BASIC_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/70a86809-07f2-4723-9e50-4dbdd31ff900">
   WSK_PROVIDER_CONNECTION_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fa8d3395-b800-4e5c-af03-b21520f69158">
   WSK_PROVIDER_DATAGRAM_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571176">WSK_PROVIDER_LISTEN_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/A10B901E-9987-40E9-976B-4CD9455E0AEE">WSK_PROVIDER_STREAM_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_SOCKET structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
