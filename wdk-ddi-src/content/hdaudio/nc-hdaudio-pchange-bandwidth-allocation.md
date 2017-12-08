---
UID: NC.hdaudio.PCHANGE_BANDWIDTH_ALLOCATION
title: PCHANGE_BANDWIDTH_ALLOCATION
author: windows-driver-content
description: The ChangeBandwidthAllocation routine changes a DMA engine's bandwidth allocation on the HD Audio Link.The function pointer type for a ChangeBandwidthAllocation routine is defined as:
old-location: audio\changebandwidthallocation.htm
old-project: audio
ms.assetid: 4dcf8fb6-71f5-4e11-a92a-0292c2a1515c
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: ChangeBandwidthAllocation
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

# PCHANGE_BANDWIDTH_ALLOCATION callback



## -description
<p>The <code>ChangeBandwidthAllocation</code> routine changes a DMA engine's bandwidth allocation on the HD Audio Link.</p>
<p>The function pointer type for a <code>ChangeBandwidthAllocation</code> routine is defined as:</p>


## -prototype

````
PCHANGE_BANDWIDTH_ALLOCATION ChangeBandwidthAllocation;

NTSTATUS ChangeBandwidthAllocation(
  _In_  PVOID                     context,
  _In_  HANDLE                    handle,
  _In_  PHDAUDIO_STREAM_FORMAT    streamFormat,
  _Out_ PHDAUDIO_CONVERTER_FORMAT converterFormat
)
{ ... }
````


## -parameters
<dl>

### -param context [in]

<dd>
<p>Specifies the context value from the <b>Context</b> member of the <a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface.md">HDAUDIO_BUS_INTERFACE</a><u>, </u><a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface-v2.md">HDAUDIO_BUS_INTERFACE_V2</a>, or <a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface-bdl.md">HDAUDIO_BUS_INTERFACE_BDL</a> structure.</p>
</dd>

### -param handle [in]

<dd>
<p>Handle identifying the DMA engine. This handle value was obtained from a previous call to <a href="..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md">AllocateCaptureDmaEngine</a> or <a href="..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md">AllocateRenderDmaEngine</a>.</p>
</dd>

### -param streamFormat [in]

<dd>
<p>Specifies the requested stream format. This parameter points to a caller-allocated structure of type <a href="..\hdaudio\ns-hdaudio--hdaudio-stream-format.md">HDAUDIO_STREAM_FORMAT</a> that specifies a data format for the stream.</p>
</dd>

### -param converterFormat [out]

<dd>
<p>Retrieves the converter format. This parameter points to a caller-allocated structure of type <a href="..\hdaudio\ns-hdaudio--hdaudio-converter-format.md">HDAUDIO_CONVERTER_FORMAT</a> into which the routine writes the encoded format. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><code>ChangeBandwidthAllocation</code> returns STATUS_SUCCESS if the call succeeds. Otherwise, the routine returns an appropriate error code. The following table shows some of the possible return error codes.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>Indicates that the caller is running at an IRQL that is too high.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>Indicates that the <i>handle</i> parameter value is invalid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that one of the parameter values is not correct (bad pointer or invalid stream format).</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>Indicates that the DMA engine is unable to allocate sufficient internal FIFO storage to support the requested stream format.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates that insufficient bandwidth is available to satisfy the request.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>Indicates that the stream is not in the reset state or that a buffer is still allocated for the DMA engine.</p>

<p> </p>

## -remarks
<p>The caller obtains an initial bandwidth allocation for a DMA engine by calling <a href="..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md">AllocateCaptureDmaEngine</a> or <a href="..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md">AllocateRenderDmaEngine</a>. Thereafter, the caller can change the bandwidth allocation by calling <code>ChangeBandwidthAllocation</code>.</p>

<p>Through the <i>converterFormat</i> parameter, the routine outputs a stream descriptor value that the caller can use to program the input or output converters. The routine encodes the information from the <i>streamFormat</i> parameter into a 16-bit integer. For more information, see <a href="..\hdaudio\ns-hdaudio--hdaudio-converter-format.md">HDAUDIO_CONVERTER_FORMAT</a>.</p>

<p>This routine fails and returns error code STATUS_INVALID_DEVICE_REQUEST in either of the following circumstances:</p>

<p>Any previously allocated DMA buffer has not been freed (by calling <a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer.md">FreeDmaBuffer</a> or <a href="..\hdaudio\nc-hdaudio-pfree-contiguous-dma-buffer.md">FreeContiguousDmaBuffer</a>).</p>

<p>The stream is in a state other than reset.</p>

<p>If the <code>ChangeBandwidthAllocation</code> call fails, the existing bandwidth reservation remains in effect. The bandwidth allocation changes only if the call succeeds.</p>

<p>In Windows Vista and later, a wave miniport driver calls this routine during execution of its <b>SetFormat</b> method (after calling one of the Allocate<i>Xxx</i>DmaEngine routines in the HD Audio DDI). For more information, see <a href="audio.iminiportwavepcistream_setformat">IMiniportWavePciStream::SetFormat</a>.</p>

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
<a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface.md">HDAUDIO_BUS_INTERFACE</a>
</dt>
<dt>
<a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface-v2.md">HDAUDIO_BUS_INTERFACE_V2</a>
</dt>
<dt>
<a href="..\hdaudio\ns-hdaudio--hdaudio-bus-interface-bdl.md">HDAUDIO_BUS_INTERFACE_BDL</a>
</dt>
<dt>
<a href="..\hdaudio\ns-hdaudio--hdaudio-stream-format.md">HDAUDIO_STREAM_FORMAT</a>
</dt>
<dt>
<a href="..\hdaudio\ns-hdaudio--hdaudio-converter-format.md">HDAUDIO_CONVERTER_FORMAT</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-capture-dma-engine.md">AllocateCaptureDmaEngine</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pallocate-render-dma-engine.md">AllocateRenderDmaEngine</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pfree-dma-buffer.md">FreeDmaBuffer</a>
</dt>
<dt>
<a href="..\hdaudio\nc-hdaudio-pfree-contiguous-dma-buffer.md">FreeContiguousDmaBuffer</a>
</dt>
<dt>
<a href="audio.iminiportwavepcistream_setformat">IMiniportWavePciStream::SetFormat</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCHANGE_BANDWIDTH_ALLOCATION callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
