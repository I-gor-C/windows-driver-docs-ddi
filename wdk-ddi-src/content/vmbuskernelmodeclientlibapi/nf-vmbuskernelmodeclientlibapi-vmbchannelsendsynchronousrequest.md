---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelSendSynchronousRequest
title: VmbChannelSendSynchronousRequest
author: windows-driver-content
description: The VmbChannelSendSynchronousRequest function sends a packet to the opposite endpoint and waits for a response.
old-location: netvista\vmbchannelsendsynchronousrequest.htm
old-project: netvista
ms.assetid: 312DED8E-570E-4DEC-B084-36894970F49F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelSendSynchronousRequest
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
req.alt-api: VmbChannelSendSynchronousRequest
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

# VmbChannelSendSynchronousRequest function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelSendSynchronousRequest</b> function sends a packet to the opposite endpoint and waits for a response.
</p>


## -syntax

````
NTSTATUS VmbChannelSendSynchronousRequest(
  _In_        VMBCHANNEL                                                               Channel,
  _In_        reads_bytes_(BufferSize)   PVOID                                         Buffer,
  _In_        UINT32                                                                   BufferSize,
  _In_opt_    PMDL                                                                     ExternalDataMdl,
  _In_        UINT32                                                                   Flags,
  _Out_       writes_bytes_to_opt_(*CompletionBufferSize, *CompletionBufferSize) PVOID CompletionBuffer,
  _Inout_opt_ _Pre_satisfies_(*_Curr_ % 8 == 0) PUINT32                                CompletionBufferSize,
  _In_opt_    PLARGE_INTEGER                                                           Timeout
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for the channel.  </p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Data to send.
</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size, in bytes, of the data to send.
</p>
</dd>

### -param <i>ExternalDataMdl</i> [in, optional]

<dd>
<p>A Memory Descriptor List (MDL) that describes an additional buffer to     send.
</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Standard flags.</p>
</dd>

### -param <i>CompletionBuffer</i> [out]

<dd>
<p>Buffer in which to store completion packet results.
</p>
</dd>

### -param <i>CompletionBufferSize</i> [in, out, optional]

<dd>
<p>The size, in bytes, of the <i>CompletionBuffer</i> value. This value must be     rounded up to nearest 8 bytes, or else the function fails. On success,
returns the number of bytes written into <i>CompletionBuffer</i>.
</p>
</dd>

### -param <i>Timeout</i> [in, optional]

<dd>
<p>A timeout in the style of the <a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a> routing.
After this time elapses, the packet is cancelled. For a timeout of zero (0), if a packet does not fir in the ring buffer, it is not queued.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The functions finished successfully.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The packet did not fit in the buffer and
was not queued.</p><dl>
<dt><b>STATUS_CANCELLED</b></dt>
</dl><p>The packet was canceled.
</p><dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl><p>The channel is being shut down.</p>

<p> </p>

## -remarks
<p>Clients can run this function with any combination of parameters. </p>

<p>The root may only call
this if <code>*Timeout == 0</code> and the <b>VMBUS_CHANNEL_FORMAT_FLAG_WAIT_FOR_COMPLETION</b> flag is not set.</p>

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
<a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20VmbChannelSendSynchronousRequest function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
