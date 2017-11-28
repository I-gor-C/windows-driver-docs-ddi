---
UID: NC.hdaudio.PALLOCATE_RENDER_DMA_ENGINE
title: PALLOCATE_RENDER_DMA_ENGINE
author: windows-driver-content
description: The AllocateRenderDmaEngine routine allocates a DMA engine for a render stream.The function pointer type for an AllocateRenderDmaEngine routine is defined as:
old-location: audio\allocaterenderdmaengine.htm
old-project: audio
ms.assetid: fb2a64ca-7e8e-4352-86c6-b9500e535c75
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: SM_SetRNIDMgmtInfo_OUT, SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: hdaudio.h
req.include-header: Hdaudio.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AllocateRenderDmaEngine
req.alt-loc: hdaudio.h
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
req.iface: 
---

# PALLOCATE_RENDER_DMA_ENGINE callback



## -description
<p>The <code>AllocateRenderDmaEngine</code> routine allocates a DMA engine for a render stream.</p>
<p>The function pointer type for an <code>AllocateRenderDmaEngine</code> routine is defined as:</p>


## -prototype

````
PALLOCATE_RENDER_DMA_ENGINE AllocateRenderDmaEngine;

NTSTATUS AllocateRenderDmaEngine(
  _In_  PVOID                     context,
  _In_  PHDAUDIO_STREAM_FORMAT    streamFormat,
  _In_  BOOLEAN                   stripe,
  _Out_ PHANDLE                   handle,
  _Out_ PHDAUDIO_CONVERTER_FORMAT converterFormat
)
{ ... }
````


## -parameters
<dl>

### -param <i>context</i> [in]

<dd>
<p>Specifies the context value from the <b>Context</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536413">HDAUDIO_BUS_INTERFACE</a><u>,</u><a href="https://msdn.microsoft.com/library/windows/hardware/ff536418">HDAUDIO_BUS_INTERFACE_V2</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a> structures.</p>
</dd>

### -param <i>streamFormat</i> [in]

<dd>
<p>Specifies the requested stream format. This parameter points to a caller-allocated structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536430">HDAUDIO_STREAM_FORMAT</a> that specifies a data format for the stream.</p>
</dd>

### -param <i>stripe</i> [in]

<dd>
<p>Specifies whether to enable striping. If <b>TRUE</b>, the routine enables striping in the DMA transfers. If <b>FALSE</b>, striping is disabled.</p>
</dd>

### -param <i>handle</i> [out]

<dd>
<p>Retrieves the handle to the DMA engine. This parameter points to a caller-allocated HANDLE variable into which the routine writes a handle that identifies the DMA engine.</p>
</dd>

### -param <i>converterFormat</i> [out]

<dd>
<p>Retrieves the converter format. This parameter points to a caller-allocated structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536426">HDAUDIO_CONVERTER_FORMAT</a> into which the routine writes the encoded format.</p>
</dd>
</dl>

## -returns
<p><code>AllocateRenderDmaEngine</code> returns STATUS_SUCCESS if the call succeeds in reserving a DMA engine. Otherwise, the routine returns an appropriate error code. The following table shows some of the possible return error codes.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>Indicates that the DMA engine is unable to allocate sufficient internal FIFO storage to support the requested stream format.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates that either no DMA engine is available or the request exceeds the available bandwidth resources.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that one of the parameter values is incorrect (invalid parameter value or bad pointer).</p>

<p> </p>

## -remarks
<p>This routine allocates a render DMA engine and specifies the data format for the stream. If successful, the routine outputs a handle that the caller subsequently uses to identify the DMA engine.</p>

<p>The <code>AllocateRenderDmaEngine</code> routine reserves hardware resources (the DMA engine) but does not configure the DMA hardware. After calling this routine to reserve a DMA engine, a function driver must assign a DMA buffer to the DMA engine and configure the engine to use the buffer:</p>

<p>If using the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI, the function driver calls the <a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer.md">AllocateDmaBuffer</a> routine to have the HD Audio bus driver allocate a data buffer for DMA transfers and set up the DMA engine to use the buffer.</p>

<p>If using the HDAUDIO_BUS_INTERFACE_BDL version of the DDI, the function driver calls <a href="..\hdaudio\nc-hdaudio-pallocate-contiguous-dma-buffer.md">AllocateContiguousDmaBuffer</a> to allocate the DMA buffer and calls the <a href="..\hdaudio\nc-hdaudio-psetup-dma-engine-with-bdl.md">SetupDmaEngineWithBdl</a> routine to set up the DMA engine to use the buffer.</p>

<p>The <i>streamFormat</i> parameter specifies the data format for the capture stream. Following the call to <code>AllocateRenderDmaEngine</code>, the stream's format can be changed by calling <a href="..\hdaudio\nc-hdaudio-pchange-bandwidth-allocation.md">ChangeBandwidthAllocation</a>.</p>

<p>The <i>stripe</i> parameter specifies whether the DMA engine is to use striping to speed up data transfers. For more information, see <a href="NULL">Striping</a>.</p>

<p>Through the handle parameter, the routine outputs a handle that the caller uses to identify the allocated DMA engine in subsequent calls to <b>AllocateDmaBuffer</b>, <b>ChangeBandwidthAllocation</b>, <a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer.md">FreeDmaBuffer</a>, <b>SetupDmaEngineWithBdl</b>, and <a href="..\hdaudio\nc-hdaudio-pset-dma-engine-state.md">SetDmaEngineState</a>. The function driver frees the handle by calling <a href="..\hdaudio\nc-hdaudio-pfree-dma-engine.md">FreeDmaEngine</a>.</p>

<p>Through the <i>converterFormat</i> parameter, the routine outputs a stream descriptor value that the caller can use to program the output converters. The routine encodes the information from the <i>streamFormat</i> parameter into a 16-bit integer. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536426">HDAUDIO_CONVERTER_FORMAT</a>.</p>

<p>Immediately following a successful call to <code>AllocateRenderDmaEngine</code>, the DMA engine is in the reset stream state. Before calling <b>SetDmaEngineState</b> to change the DMA engine to the running, paused, or stopped state, the client must first allocate a DMA buffer for the engine.</p>

<p>A WDM audio driver calls <code>AllocateRenderDmaEngine</code> at pin-creation time during execution of its <b>NewStream</b> method (for example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536735">IMiniportWavePci::NewStream</a>).</p>

<p>This routine allocates a render DMA engine and specifies the data format for the stream. If successful, the routine outputs a handle that the caller subsequently uses to identify the DMA engine.</p>

<p>The <code>AllocateRenderDmaEngine</code> routine reserves hardware resources (the DMA engine) but does not configure the DMA hardware. After calling this routine to reserve a DMA engine, a function driver must assign a DMA buffer to the DMA engine and configure the engine to use the buffer:</p>

<p>If using the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI, the function driver calls the <a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer.md">AllocateDmaBuffer</a> routine to have the HD Audio bus driver allocate a data buffer for DMA transfers and set up the DMA engine to use the buffer.</p>

<p>If using the HDAUDIO_BUS_INTERFACE_BDL version of the DDI, the function driver calls <a href="..\hdaudio\nc-hdaudio-pallocate-contiguous-dma-buffer.md">AllocateContiguousDmaBuffer</a> to allocate the DMA buffer and calls the <a href="..\hdaudio\nc-hdaudio-psetup-dma-engine-with-bdl.md">SetupDmaEngineWithBdl</a> routine to set up the DMA engine to use the buffer.</p>

<p>The <i>streamFormat</i> parameter specifies the data format for the capture stream. Following the call to <code>AllocateRenderDmaEngine</code>, the stream's format can be changed by calling <a href="..\hdaudio\nc-hdaudio-pchange-bandwidth-allocation.md">ChangeBandwidthAllocation</a>.</p>

<p>The <i>stripe</i> parameter specifies whether the DMA engine is to use striping to speed up data transfers. For more information, see <a href="NULL">Striping</a>.</p>

<p>Through the handle parameter, the routine outputs a handle that the caller uses to identify the allocated DMA engine in subsequent calls to <b>AllocateDmaBuffer</b>, <b>ChangeBandwidthAllocation</b>, <a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer.md">FreeDmaBuffer</a>, <b>SetupDmaEngineWithBdl</b>, and <a href="..\hdaudio\nc-hdaudio-pset-dma-engine-state.md">SetDmaEngineState</a>. The function driver frees the handle by calling <a href="..\hdaudio\nc-hdaudio-pfree-dma-engine.md">FreeDmaEngine</a>.</p>

<p>Through the <i>converterFormat</i> parameter, the routine outputs a stream descriptor value that the caller can use to program the output converters. The routine encodes the information from the <i>streamFormat</i> parameter into a 16-bit integer. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536426">HDAUDIO_CONVERTER_FORMAT</a>.</p>

<p>Immediately following a successful call to <code>AllocateRenderDmaEngine</code>, the DMA engine is in the reset stream state. Before calling <b>SetDmaEngineState</b> to change the DMA engine to the running, paused, or stopped state, the client must first allocate a DMA buffer for the engine.</p>

<p>A WDM audio driver calls <code>AllocateRenderDmaEngine</code> at pin-creation time during execution of its <b>NewStream</b> method (for example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536735">IMiniportWavePci::NewStream</a>).</p>

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
<dt>Hdaudio.h (include Hdaudio.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536413">HDAUDIO_BUS_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536418">HDAUDIO_BUS_INTERFACE_V2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536430">HDAUDIO_STREAM_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536426">HDAUDIO_CONVERTER_FORMAT</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-dma-buffer.md">AllocateDmaBuffer</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pchange-bandwidth-allocation.md">ChangeBandwidthAllocation</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pfree-dma-engine.md">FreeDmaEngine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536735">IMiniportWavePci::NewStream</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PALLOCATE_RENDER_DMA_ENGINE callback function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
