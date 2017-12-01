---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelMapGpadl
title: VmbChannelMapGpadl
author: windows-driver-content
description: The VmbChannelMapGpadl function maps a client-side buffer into server-side physical address space by using a Guest Physical Address Descriptor List (GPADL) number.
old-location: netvista\vmbchannelmapgpadl.htm
old-project: netvista
ms.assetid: A7801EE9-BFDB-4F77-9DA4-A6612F63AD48
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelMapGpadl
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
req.alt-api: VmbChannelMapGpadl
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

# VmbChannelMapGpadl function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelMapGpadl</b>  function maps a client-side buffer into server-side physical address space by using a Guest Physical Address Descriptor List (GPADL) number. </p>


## -syntax

````
NTSTATUS VmbChannelMapGpadl(
  _In_  VMBCHANNEL Channel,
  _In_  UINT32     Flags,
  _In_  UINT32     GpadlHandle,
  _Out_ PMDL       *Mdl
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for a channel.  </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Flags.  The possible flag values are:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="VMBUS_CHANNEL_GPADL_FLAG_READ_ONLY"></a><a id="vmbus_channel_gpadl_flag_read_only"></a><dl>

### -param <b>VMBUS_CHANNEL_GPADL_FLAG_READ_ONLY</b>

</dl>
</td>
<td width="60%">
<p>Map with read-only access. </p>
</td>
</tr>
</table>
<p> </p>
<p>If
this flag value is not set, the function tries to map the GPADL for write access. If the GPADL was not
created with write access, this mapping attempt fails. The
caller is not prevented from writing to the buffer if this flag is set. This scheme is used to improve the performance of live migration
and snapshotting.
</p>
</dd>

### -param <i>GpadlHandle</i> [in]

<dd>
<p>The GPADL handle of the GPADL to map.
</p>
</dd>

### -param <i>Mdl</i> [out]

<dd>
<p> A pointer to a MDL describing the client buffer. This
buffer is only mapped into physical address space. The caller must take
additional steps to map it into virtual address space.</p>
</dd>
</dl>

## -remarks
<p>The GPADL must have been pre-established by the client, for instance, by using the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelcreategpadlfrombuffer.md">VmbChannelCreateGpadlFromBuffer</a> function.  </p>

<p>Only a single mapping may exist for any given GPADL at a time.  </p>

<p>You must pair calls to this
function with calls to the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelunmapgpadl.md">VmbChannelUnmapGpadl</a> function.</p>

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
<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelcreategpadlfrombuffer.md">VmbChannelCreateGpadlFromBuffer</a>
</dt>
<dt>
<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelunmapgpadl.md">VmbChannelUnmapGpadl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20VmbChannelMapGpadl function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
