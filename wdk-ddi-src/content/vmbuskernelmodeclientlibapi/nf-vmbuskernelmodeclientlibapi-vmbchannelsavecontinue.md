---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelSaveContinue
title: VmbChannelSaveContinue
author: windows-driver-content
description: The VmbChannelSaveContinue function saves the channel state to a buffer. Run the VmbChannelSaveBegin before you run this function. The driver must check the return value of the function.
old-location: netvista\vmbchannelsavecontinue.htm
old-project: netvista
ms.assetid: 57266CAE-C069-4379-92FD-0F93FECC6EB5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelSaveContinue
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
req.alt-api: VmbChannelSaveContinue
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

# VmbChannelSaveContinue function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelSaveContinue</b> function saves the channel state to a buffer.  Run the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelsavebegin.md">VmbChannelSaveBegin</a> before you run this function. The driver must check the return value of the function.</p>


## -syntax

````
NTSTATUS VmbChannelSaveContinue(
  _In_  VMBCHANNEL                                                       Channel,
  _Out_ writes_bytes_to_(SaveBufferSize, *BytesFilled)
            PVOID SaveBuffer,
  _In_  ULONG                                                            SaveBufferSize,
  _Out_ PULONG                                                           BytesFilled,
  _Out_ PULONG                                                           BytesRequired
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for a channel to save.  </p>
</dd>

### -param <i>SaveBuffer</i> [out]

<dd>
<p>A pointer to buffer into which to save state information. </p>
</dd>

### -param <i>SaveBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the save buffer.
</p>
</dd>

### -param <i>BytesFilled</i> [out]

<dd>
<p>A pointer to a variable that receives the number of bytes
that were copied to the save buffer.
</p>
</dd>

### -param <i>BytesRequired</i> [out]

<dd>
<p>A pointer to a variable that receives the number of
bytes that are needed for this function to make progress on the next
call.</p>
</dd>
</dl>

## -returns
<p><b>VmbChannelSaveContinue</b> returns the following values: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The state was saved.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL </b></dt>
</dl><p>The save buffer was too small.  The <i>BytesNeeded</i>
parameter     contains the number of bytes that are required to make any progress.
</p><dl>
<dt><b>STATUS_STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>Some data was written to the save
buffer, but there is more data to be saved.</p>

<p> </p>

## -remarks
<p>The save process saves
the data in "chunks" and can continue from the point it stopped. </p>

<p>If the caller did not allocate enough space in advance, multiple calls may be needed.</p>

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
<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelsavebegin.md">VmbChannelSaveBegin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20VmbChannelSaveContinue function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
