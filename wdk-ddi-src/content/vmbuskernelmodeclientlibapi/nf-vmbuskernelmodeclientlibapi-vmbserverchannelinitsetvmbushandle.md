---
UID: NF.vmbuskernelmodeclientlibapi.VmbServerChannelInitSetVmbusHandle
title: VmbServerChannelInitSetVmbusHandle
author: windows-driver-content
description: The VmbServerChannelInitSetVmbusHandle function associates an instance of VMBus with this channel.
old-location: netvista\vmbserverchannelinitsetvmbushandle.htm
old-project: netvista
ms.assetid: 0ECF76C7-9475-439E-8E59-B2B7CD350D24
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbServerChannelInitSetVmbusHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: VmbServerChannelInitSetVmbusHandle
req.alt-loc: VmbusKernelModeClientLibApi.h
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

# VmbServerChannelInitSetVmbusHandle function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbServerChannelInitSetVmbusHandle</b> function associates an instance of VMBus with this channel.  </p>


## -syntax

````
NTSTATUS VmbServerChannelInitSetVmbusHandle(
  _In_ VMBCHANNEL Channel,
  _In_ HANDLE     VmbusHandle
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for a channel.</p>
</dd>

### -param <i>VmbusHandle</i> [in]

<dd>
<p>A kernel mode handle to the VMBus vdev of the partition.</p>
</dd>
</dl>

## -remarks
<p>The VMBus
instance was previously initialized for the specific guest virtual machine. Therefore, invoking this function identifies the child virtual machine to which this channel is offered.</p>

<p> Obtain a value for the <i>VmbusHandle</i> parameter by using the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbconvertvmbushandletokernelhandle.md">VmbConvertVmbusHandleToKernelHandle</a> function.
</p>

<p>This function can be called while running in any thread context.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.13</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>VmbusKernelModeClientLibApi.h (include VmbusKernelModeClientLibApi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbconvertvmbushandletokernelhandle.md">VmbConvertVmbusHandleToKernelHandle</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20VmbServerChannelInitSetVmbusHandle function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
