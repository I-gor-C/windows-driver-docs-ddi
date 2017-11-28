---
UID: NF.irb.AtaPortRegistryAllocateBuffer
title: AtaPortRegistryAllocateBuffer
author: windows-driver-content
description: The AtaPortRegistryAllocateBuffer routine allocates a buffer for registry operations.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportregistryallocatebuffer.htm
old-project: storage
ms.assetid: c888fd84-2828-4f2d-921d-ba92a5ce9c84
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AtaPortRegistryAllocateBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortRegistryAllocateBuffer
req.alt-loc: ataport.lib,ataport.dll,pciidex.lib,pciidex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ataport.lib; 
Pciidex.lib
req.dll: 
req.irql: 
req.iface: 
---

# AtaPortRegistryAllocateBuffer function



## -description
<p>The <b>AtaPortRegistryAllocateBuffer</b> routine allocates a buffer for registry operations.</p>


## -syntax

````
PVOID AtaPortRegistryAllocateBuffer(
  _In_ PVOID ChannelExtension,
  _In_ ULONG Count
);
````


## -parameters
<dl>

### -param <i>ChannelExtension</i> [in]

<dd>
<p>A pointer to the channel extension. </p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>Specifies the length of the buffer, in bytes.</p>
</dd>
</dl>

## -returns
<p><b>AtaPortRegistryAllocateBuffer</b> returns a pointer to the allocated buffer on success. Otherwise, it returns <b>NULL</b>. </p>

## -remarks
<p>The port driver enables the miniport driver to allocate one buffer for all its registry operations. After the miniport driver has allocated a buffer with <b>AtaPortRegistryAllocateBuffer</b>, later calls to <b>AtaPortRegistryAllocateBuffer</b> will fail and return <b>NULL</b>. After the miniport driver frees the allocated buffer with a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550212">AtaPortRegistryFreeBuffer</a> routine, it can again allocate buffers by calling <b>AtaPortRegistryAllocateBuffer</b>.</p>

<p>The miniport driver must call <b>AtaPortRegistryAllocateBuffer</b> either in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550141">AtaChannelInitRoutine</a> routine or in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff557465">IdeHwControl</a> routine. It cannot call <b>AtaPortRegistryAllocateBuffer</b> from any other routine. Additionally, the miniport driver can only call <b>AtaPortRegistryAllocateBuffer</b> from its <b>IdeHwControl</b> routine if its <b>IdeHwControl</b> routine was called and had a value of either <b>StartChannel</b> or <b>StopChannel</b> in its <i>ControlAction </i>parameter. </p>

<p>The port driver enables the miniport driver to allocate one buffer for all its registry operations. After the miniport driver has allocated a buffer with <b>AtaPortRegistryAllocateBuffer</b>, later calls to <b>AtaPortRegistryAllocateBuffer</b> will fail and return <b>NULL</b>. After the miniport driver frees the allocated buffer with a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550212">AtaPortRegistryFreeBuffer</a> routine, it can again allocate buffers by calling <b>AtaPortRegistryAllocateBuffer</b>.</p>

<p>The miniport driver must call <b>AtaPortRegistryAllocateBuffer</b> either in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff550141">AtaChannelInitRoutine</a> routine or in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff557465">IdeHwControl</a> routine. It cannot call <b>AtaPortRegistryAllocateBuffer</b> from any other routine. Additionally, the miniport driver can only call <b>AtaPortRegistryAllocateBuffer</b> from its <b>IdeHwControl</b> routine if its <b>IdeHwControl</b> routine was called and had a value of either <b>StartChannel</b> or <b>StopChannel</b> in its <i>ControlAction </i>parameter. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Ata.h or Irb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ataport.lib; </dt>
<dt>Pciidex.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557465">IdeHwControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550141">AtaChannelInitRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550212">AtaPortRegistryFreeBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortRegistryAllocateBuffer routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
