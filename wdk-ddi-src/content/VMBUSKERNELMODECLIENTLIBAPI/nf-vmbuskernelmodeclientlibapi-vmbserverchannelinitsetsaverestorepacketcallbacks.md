---
UID: NF.vmbuskernelmodeclientlibapi.VmbServerChannelInitSetSaveRestorePacketCallbacks
title: VmbServerChannelInitSetSaveRestorePacketCallbacks
author: windows-driver-content
description: The VmbServerChannelInitSetSaveRestorePacketCallbacks function sets the save and restore callback functions that are called for each packet when the driver calls a save function, such as VmbChannelSaveBegin, VmbChannelSaveContinue, and VmbChannelSaveEnd, or the VmbChannelRestoreFromBuffer function.
old-location: netvista\vmbserverchannelinitsetsaverestorepacketcallbacks.htm
ms.assetid: 2E704BF1-21E2-498E-82C2-2B55BF44D044
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: VmbServerChannelInitSetSaveRestorePacketCallbacks
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
ms.keywords: VmbServerChannelInitSetSaveRestorePacketCallbacks
req.iface: 
req.product: Windows 10 or later.
---

# VmbServerChannelInitSetSaveRestorePacketCallbacks function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbServerChannelInitSetSaveRestorePacketCallbacks</b> function sets the save and restore callback functions that are called for each packet when the
driver calls a save function, such as <a href="https://msdn.microsoft.com/A0946287-3ED2-4DE1-A3D7-46611B25BB93">VmbChannelSaveBegin</a>, <a href="https://msdn.microsoft.com/57266CAE-C069-4379-92FD-0F93FECC6EB5">VmbChannelSaveContinue</a>, and <a href="https://msdn.microsoft.com/0E61AF98-DC71-4234-B337-71B2AF65D858">VmbChannelSaveEnd</a>, or the <a href="https://msdn.microsoft.com/5A063585-AC45-44DF-BE21-FA1BB6283E6F">VmbChannelRestoreFromBuffer</a> function.</p>


## -syntax

````
NTSTATUS
 VmbServerChannelInitSetSaveRestorePacketCallbacks(
  _In_ VMBCHANNEL                     Channel,
  _In_ PFN_VMB_CHANNEL_SAVE_PACKET    SavePacketCallback,
  _In_ PFN_VMB_CHANNEL_RESTORE_PACKET RestorePacketCallback
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p> A handle for a channel.  </p>
</dd>

### -param <i>SavePacketCallback</i> [in]

<dd>
<p>A callback function to call during channel
save. </p>
</dd>

### -param <i>RestorePacketCallback</i> [in]

<dd>
<p>A callback function to call during channel     restore.</p>
</dd>
</dl>

## -returns
<p><b>VmbServerChannelInitSetSaveRestorePacketCallbacks</b> returns the following status values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The <i>Channel</i> value was invalid or in an invalid state, such as Disabled.</p>

<p> </p>

## -remarks


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
<a href="https://msdn.microsoft.com/5A063585-AC45-44DF-BE21-FA1BB6283E6F">VmbChannelRestoreFromBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/A0946287-3ED2-4DE1-A3D7-46611B25BB93">VmbChannelSaveBegin</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/57266CAE-C069-4379-92FD-0F93FECC6EB5">VmbChannelSaveContinue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0E61AF98-DC71-4234-B337-71B2AF65D858">VmbChannelSaveEnd</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20VmbServerChannelInitSetSaveRestorePacketCallbacks function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
