---
UID: NF.portcls.IPortWavePci.NewMasterDmaChannel
title: IPortWavePci::NewMasterDmaChannel
author: windows-driver-content
description: The NewMasterDmaChannel method creates a new instance of a bus-master DMA channel.
old-location: audio\iportwavepci_newmasterdmachannel.htm
ms.assetid: a4128541-1982-413d-a013-422ca1cf4542
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortWavePci.NewMasterDmaChannel
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
ms.keywords: IPortWavePci, NewMasterDmaChannel, IPortWavePci::NewMasterDmaChannel
req.iface: IPortWavePci
---

# IPortWavePci::NewMasterDmaChannel method



## -description
<p>The <code>NewMasterDmaChannel</code> method creates a new instance of a bus-master DMA channel.</p>


## -syntax

````
NTSTATUS NewMasterDmaChannel(
  [out]          PDMACHANNEL   *DmaChannel,
  [in, optional] PUNKNOWN      OuterUnknown,
  [in]           POOL_TYPE     PoolType,
  [in, optional] PRESOURCELIST ResourceList,
  [in]           BOOLEAN       ScatterGather,
  [in]           BOOLEAN       Dma32BitAddresses,
  [in]           BOOLEAN       Dma64BitAddresses,
  [in]           BOOLEAN       IgnoreCount,
  [in]           DMA_WIDTH     DmaWidth,
  [in]           DMA_SPEED     DmaSpeed,
  [in]           ULONG         MaximumLength,
  [in]           ULONG         DmaPort
);
````


## -parameters
<dl>

### -param <i>DmaChannel</i> [out]

<dd>
<p>Output pointer for the DMA channel. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the new DMA-channel object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a> interface.</p>
</dd>

### -param <i>OuterUnknown</i> [in, optional]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of an object that needs to aggregate the DMA-channel object. This parameter is optional. If aggregation is not required, specify this parameter as <b>NULL</b>.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Specifies the type of storage pool from which the object is to be allocated. This is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a> enumeration value. Specify a nonpaged pool type for this parameter.</p>
</dd>

### -param <i>ResourceList</i> [in, optional]

<dd>
<p>Pointer to the miniport driver's resource list, which is an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a> object. This parameter is optional and can be specified as <b>NULL</b>. The <code>NewMasterDmaChannel</code> method currently makes no use of this parameter.</p>
</dd>

### -param <i>ScatterGather</i> [in]

<dd>
<p>Requests that the DMA channel support scatter/gather DMA. Always set this parameter to <b>TRUE</b>.</p>
</dd>

### -param <i>Dma32BitAddresses</i> [in]

<dd>
<p>Specifies the use of 32-bit addresses for DMA operations.</p>
</dd>

### -param <i>Dma64BitAddresses</i> [in]

<dd>
<p>Specifies the use of 64-bit addresses for DMA operations.</p>
</dd>

### -param <i>IgnoreCount</i> [in]

<dd>
<p>Indicates whether to ignore the DMA controller's transfer counter. Set to <b>TRUE</b> if the DMA controller in this platform does not maintain an accurate transfer counter, and therefore requires a workaround.</p>
</dd>

### -param <i>DmaWidth</i> [in]

<dd>
<p>Not used. Set to (DMA_WIDTH)(-1).</p>
</dd>

### -param <i>DmaSpeed</i> [in]

<dd>
<p>Not used. Set to (DMA_SPEED)(-1).</p>
</dd>

### -param <i>MaximumLength</i> [in]

<dd>
<p>Maximum number of bytes in the buffer that will be associated with this DMA channel.</p>
</dd>

### -param <i>DmaPort</i> [in]

<dd>
<p>Not used. Set to 0.</p>
</dd>
</dl>

## -returns
<p><code>NewMasterDmaChannel</code> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>The definitions of the call parameters for the <code>NewMasterDmaChannel</code> method are similar to those for the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a> structure with the same names.</p>

<p>Specify the <i>PoolType</i> parameter to be one of the nonpaged pool types defined in the POOL_TYPE enumeration. The DMA-channel object must not reside in paged memory because several of the methods in the <b>IDmaChannel</b> interface can be called from IRQL DISPATCH_LEVEL.</p>

<p>The <i>DmaChannel</i>, <i>OuterUnknown</i>, and <i>ResourceList</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>The definitions of the call parameters for the <code>NewMasterDmaChannel</code> method are similar to those for the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a> structure with the same names.</p>

<p>Specify the <i>PoolType</i> parameter to be one of the nonpaged pool types defined in the POOL_TYPE enumeration. The DMA-channel object must not reside in paged memory because several of the methods in the <b>IDmaChannel</b> interface can be called from IRQL DISPATCH_LEVEL.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536547">IDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543107">DEVICE_DESCRIPTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWavePci::NewMasterDmaChannel method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
