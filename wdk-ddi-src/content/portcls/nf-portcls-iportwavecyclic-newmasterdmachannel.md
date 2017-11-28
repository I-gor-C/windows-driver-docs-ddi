---
UID: NF.portcls.IPortWaveCyclic.NewMasterDmaChannel
title: IPortWaveCyclic::NewMasterDmaChannel
author: windows-driver-content
description: The NewMasterDmaChannel method creates a new instance of a bus-master DMA channel.
old-location: audio\iportwavecyclic_newmasterdmachannel.htm
old-project: audio
ms.assetid: bbd2b6e2-e332-49ae-aa18-490fd5631479
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IPortWaveCyclic, NewMasterDmaChannel, IPortWaveCyclic::NewMasterDmaChannel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortWaveCyclic.NewMasterDmaChannel
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: IPortWaveCyclic
---

# IPortWaveCyclic::NewMasterDmaChannel method



## -description
<p>The <code>NewMasterDmaChannel</code> method creates a new instance of a bus-master DMA channel.</p>


## -syntax

````
NTSTATUS NewMasterDmaChannel(
  [out]          PDMACHANNEL   *DmaChannel,
  [in]           PUNKNOWN      OuterUnknown,
  [in, optional] PRESOURCELIST ResourceList,
  [in]           ULONG         MaximumLength,
  [in]           BOOLEAN       Dma32BitAddresses,
  [in]           BOOLEAN       Dma64BitAddresses,
  [in]           DMA_WIDTH     DmaWidth,
  [in]           DMA_SPEED     DmaSpeed
);
````


## -parameters
<dl>

### -param <i>DmaChannel</i> [out]

<dd>
<p>Pointer to a caller-allocated pointer variable into which the method writes a pointer to the new <a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a> object. Specify a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>

### -param <i>OuterUnknown</i> [in]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of an object that needs to aggregate the DMA-channel object. This parameter is optional. If aggregation is not required, specify this parameter as <b>NULL</b>.</p>
</dd>

### -param <i>ResourceList</i> [in, optional]

<dd>
<p>Pointer to the miniport driver's resource list, which is an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a> object. This parameter is optional and can be specified as <b>NULL</b>. The <code>NewMasterDmaChannel</code> method currently makes no use of this parameter.</p>
</dd>

### -param <i>MaximumLength</i> [in]

<dd>
<p>Maximum length in bytes of the cyclic DMA buffer that will be associated with this channel.</p>
</dd>

### -param <i>Dma32BitAddresses</i> [in]

<dd>
<p>Specifies the use of 32-bit addresses.</p>
</dd>

### -param <i>Dma64BitAddresses</i> [in]

<dd>
<p>Specifies the use of 64-bit addresses.</p>
</dd>

### -param <i>DmaWidth</i> [in]

<dd>
<p>Not used. Set to (DMA_WIDTH)(-1).</p>
</dd>

### -param <i>DmaSpeed</i> [in]

<dd>
<p>Not used. Set to (DMA_SPEED)(-1).</p>
</dd>
</dl>

## -returns
<p><code>NewMasterDmaChannel</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>Parameters <i>MaximumLength</i>, <i>Dma32BitAddresses</i>, <i>Dma64BitAddresses</i>, <i>DmaWidth</i>, and <i>DmaSpeed</i> are similar in meaning to the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a> structure with the same names.</p>

<p>A WaveCyclic device with built-in bus-mastering DMA hardware is referred to as a <i>master device</i>. In contrast, a <i>subordinate device</i> lacks DMA hardware and has to rely on the system DMA controller to perform any data transfers that it requires. The <code>NewMasterDmaChannel</code> method creates a DMA-channel object for a master device. To create a DMA-channel object for a subordinate device, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536902">IPortWaveCyclic::NewSlaveDmaChannel</a> method instead. For more information about master and subordinate devices, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536548">IDmaChannelSlave</a>.</p>

<p>The <i>DmaChannel</i>, <i>OuterUnknown</i>, and <i>ResourceList</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>Parameters <i>MaximumLength</i>, <i>Dma32BitAddresses</i>, <i>Dma64BitAddresses</i>, <i>DmaWidth</i>, and <i>DmaSpeed</i> are similar in meaning to the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a> structure with the same names.</p>

<p>A WaveCyclic device with built-in bus-mastering DMA hardware is referred to as a <i>master device</i>. In contrast, a <i>subordinate device</i> lacks DMA hardware and has to rely on the system DMA controller to perform any data transfers that it requires. The <code>NewMasterDmaChannel</code> method creates a DMA-channel object for a master device. To create a DMA-channel object for a subordinate device, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536902">IPortWaveCyclic::NewSlaveDmaChannel</a> method instead. For more information about master and subordinate devices, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536548">IDmaChannelSlave</a>.</p>

<p>The <i>DmaChannel</i>, <i>OuterUnknown</i>, and <i>ResourceList</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536899">IPortWaveCyclic</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536902">IPortWaveCyclic::NewSlaveDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536548">IDmaChannelSlave</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWaveCyclic::NewMasterDmaChannel method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
