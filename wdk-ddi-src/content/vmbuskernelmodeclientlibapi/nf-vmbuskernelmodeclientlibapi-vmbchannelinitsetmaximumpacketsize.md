---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelInitSetMaximumPacketSize
title: VmbChannelInitSetMaximumPacketSize
author: windows-driver-content
description: The VmbChannelInitSetMaximumPacketSize function sets the maximum packet size that can be delivered through a channel, which is the maximum size that will ever be specified by the VmbPacketSend function.
old-location: netvista\vmbchannelinitsetmaximumpacketsize.htm
old-project: netvista
ms.assetid: E1CD6911-A54F-4B24-B9BE-59EF9F2C30E5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelInitSetMaximumPacketSize
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
req.alt-api: VmbChannelInitSetMaximumPacketSize
req.alt-loc: vmbkmcl.lib,vmbkmcl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Vmbkmcl.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# VmbChannelInitSetMaximumPacketSize function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The  <b>VmbChannelInitSetMaximumPacketSize</b> function sets the maximum packet size that can be delivered through a channel, which is the maximum size that will ever be specified by the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketsend.md">VmbPacketSend</a> function.  </p>


## -syntax

````
NTSTATUS VmbChannelInitSetMaximumPacketSize(
  _In_ VMBCHANNEL         Channel,
  _In_ range_(>,0) UINT32 PacketSize
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for the channel.  </p>
</dd>

### -param <i>PacketSize</i> [in]

<dd>
<p>Maximum size, in bytes, of a packet.</p>
</dd>
</dl>

## -returns
<p><b>VmbChannelInitSetMaximumPacketSize</b> returns one of the following status values: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function finished successfully.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The <i>Channel</i> value was invalid or in an invalid state, such as Disabled.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The <i>PacketSize</i> value is invalid. Zero (0) is invalid.</p>

<p> </p>

## -remarks
<p>This function can only be called during channel initialization. </p>

<p>The size of
the ring buffers is, in part, based on this maximum packet size. </p>

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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Vmbkmcl.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketsend.md">VmbPacketSend</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20VmbChannelInitSetMaximumPacketSize function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
