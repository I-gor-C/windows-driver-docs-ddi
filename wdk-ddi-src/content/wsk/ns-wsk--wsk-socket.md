---
UID: NS.wsk._WSK_SOCKET
title: WSK_SOCKET
author: windows-driver-content
description: The WSK_SOCKET structure defines a socket object for a socket.
old-location: netvista\wsk_socket.htm
old-project: netvista
ms.assetid: dce4a087-a14b-400b-bdc1-944c1d4d492a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WSK_SOCKET, WSK_SOCKET, *PWSK_SOCKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
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

### -field Dispatch

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
<a href="..\wsk\ns-wsk--wsk-provider-basic-dispatch.md">
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
<a href="..\wsk\ns-wsk--wsk-provider-listen-dispatch.md">
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
<a href="..\wsk\ns-wsk--wsk-provider-datagram-dispatch.md">
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
<a href="..\wsk\ns-wsk--wsk-provider-connection-dispatch.md">
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
<a href="..\wsk\ns-wsk--wsk-provider-stream-dispatch.md">
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
      <a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a> function to create a socket.</p>

<p>The WSK application calls the 
      <a href="..\wsk\nc-wsk-pfn-wsk-socket-connect.md">WskSocketConnect</a> function to create,
      bind, and connect a connection-oriented socket.</p>

<p>The WSK application calls the 
      <a href="..\wsk\nc-wsk-pfn-wsk-accept.md">WskAccept</a> function to accept an incoming
      connection-oriented socket on a listening socket.</p>

<p>The WSK subsystem calls the WSK application's 
      <a href="..\wsk\nc-wsk-pfn-wsk-accept-event.md">WskAcceptEvent</a> event callback function to
      notify the WSK application that an incoming connection-oriented socket has been accepted on a listening
      socket.</p>

<p>A WSK application passes the pointer to a socket's WSK_SOCKET structure when calling any of the
    socket's functions.</p>

<p>The WSK subsystem frees the memory for the WSK_SOCKET structure when the WSK application calls the 
    <a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a> function to close the
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
<a href="..\wsk\nc-wsk-pfn-wsk-accept.md">WskAccept</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-close-socket.md">WskCloseSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-socket.md">WskSocket</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-socket-connect.md">WskSocketConnect</a>
</dt>
<dt>
<a href="..\wsk\nc-wsk-pfn-wsk-accept-event.md">WskAcceptEvent</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-basic-dispatch.md">WSK_PROVIDER_BASIC_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-connection-dispatch.md">
   WSK_PROVIDER_CONNECTION_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-datagram-dispatch.md">
   WSK_PROVIDER_DATAGRAM_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-listen-dispatch.md">WSK_PROVIDER_LISTEN_DISPATCH</a>
</dt>
<dt>
<a href="..\wsk\ns-wsk--wsk-provider-stream-dispatch.md">WSK_PROVIDER_STREAM_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_SOCKET structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
