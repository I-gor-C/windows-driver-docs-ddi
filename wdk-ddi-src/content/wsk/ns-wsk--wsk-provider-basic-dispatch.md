---
UID: NS.wsk._WSK_PROVIDER_BASIC_DISPATCH
title: WSK_PROVIDER_BASIC_DISPATCH
author: windows-driver-content
description: The WSK_PROVIDER_BASIC_DISPATCH structure specifies the WSK subsystem's dispatch table of functions for a basic socket.
old-location: netvista\wsk_provider_basic_dispatch.htm
old-project: netvista
ms.assetid: 15cd5336-fe29-4a59-8071-04c802552a5a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WSK_PROVIDER_BASIC_DISPATCH, WSK_PROVIDER_BASIC_DISPATCH, *PWSK_PROVIDER_BASIC_DISPATCH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WSK_PROVIDER_BASIC_DISPATCH
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

# WSK_PROVIDER_BASIC_DISPATCH structure



## -description
<p>The WSK_PROVIDER_BASIC_DISPATCH structure specifies the WSK subsystem's dispatch table of functions
  for a basic socket.</p>


## -syntax

````
typedef struct _WSK_PROVIDER_BASIC_DISPATCH {
  PFN_WSK_CONTROL_SOCKET WskControlSocket;
  PFN_WSK_CLOSE_SOCKET   WskCloseSocket;
} WSK_PROVIDER_BASIC_DISPATCH, *PWSK_PROVIDER_BASIC_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>WskControlSocket</b>

<dd>
<p>A pointer to the WSK subsystem's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571127">WskControlSocket</a> function for the
     socket.</p>
</dd>

### -field <b>WskCloseSocket</b>

<dd>
<p>A pointer to the WSK subsystem's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a> function for the
     socket.</p>
</dd>
</dl>

## -remarks
<p>A WSK application receives a pointer to a WSK_PROVIDER_BASIC_DISPATCH structure when the WSK
    application calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a> function to create a basic socket. The
    pointer is contained in the 
    <b>Dispatch</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a> structure that is received from the
    WSK subsystem.</p>

<p>The WSK_PROVIDER_BASIC_DISPATCH structure is also included in the 
    <a href="..\wsk\ns-wsk--wsk-provider-connection-dispatch.md">
    WSK_PROVIDER_CONNECTION_DISPATCH</a>, 
    <a href="..\wsk\ns-wsk--wsk-provider-datagram-dispatch.md">
    WSK_PROVIDER_DATAGRAM_DISPATCH</a>, and 
    <a href="..\wsk\ns-wsk--wsk-provider-listen-dispatch.md">
    WSK_PROVIDER_LISTEN_DISPATCH</a> structures. The 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571127">WskControlSocket</a> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a> functions that are included
    in the WSK_PROVIDER_BASIC_DISPATCH structure are supported by all of the 
    <a href="netvista.winsock_kernel_socket_categories">socket categories</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571124">WskCloseSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571127">WskControlSocket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571149">WskSocket</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571176">WSK_PROVIDER_LISTEN_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571182">WSK_SOCKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_PROVIDER_BASIC_DISPATCH structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
