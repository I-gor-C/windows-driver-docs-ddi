---
UID: NC.hdaudio.PSET_DMA_ENGINE_STATE
title: PSET_DMA_ENGINE_STATE
author: windows-driver-content
description: The SetDmaEngineState routine sets the state of one or more DMA engines to the Running, Stopped, Paused, or Reset state.The function pointer type for a SetDmaEngineState routine is defined as:
old-location: audio\setdmaenginestate.htm
ms.assetid: 05cfb827-e143-4d77-b378-e02dd381e429
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: audio
req.header: hdaudio.h
req.include-header: Hdaudio.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetDmaEngineState
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
req.irql: <=DISPATCH_LEVEL
ms.keywords: SM_SetRNIDMgmtInfo_OUT, SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
req.iface: 
---

# PSET_DMA_ENGINE_STATE callback



## -description
<p>The <i>SetDmaEngineState</i> routine sets the state of one or more DMA engines to the Running, Stopped, Paused, or Reset state.</p>
<p>The function pointer type for a <i>SetDmaEngineState</i> routine is defined as:</p>


## -prototype

````
PSET_DMA_ENGINE_STATE SetDmaEngineState;

NTSTATUS SetDmaEngineState(
  _In_ PVOID                context,
  _In_ HDAUDIO_STREAM_STATE streamState,
  _In_ ULONG                numberOfHandles,
  _In_ PHANDLE              handles
)
{ ... }
````


## -parameters
<dl>

### -param <i>context</i> [in]

<dd>
<p>Specifies the context value from the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536413">HDAUDIO_BUS_INTERFACE</a><u>, </u><a href="https://msdn.microsoft.com/library/windows/hardware/ff536418">HDAUDIO_BUS_INTERFACE_V2</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a> structure.</p>
</dd>

### -param <i>streamState</i> [in]

<dd>
<p>Specifies the new stream state. Set this parameter to one of the following HDAUDIO_STREAM_STATE enumeration values:</p>
<ul>
<li>
<p><b>PauseState</b> (paused)</p>
</li>
<li>
<p><b>ResetState</b> (reset)</p>
</li>
<li>
<p><b>RunState</b> (running)</p>
</li>
<li>
<p><b>StopState</b> (stopped)</p>
</li>
</ul>
<p>In the current implementation, <b>PauseState</b> and <b>StopState</b> represent the same hardware state.</p>
</dd>

### -param <i>numberOfHandles</i> [in]

<dd>
<p>Specifies the number of handles in the <i>handles</i> array. Set this parameter to a nonzero value.</p>
</dd>

### -param <i>handles</i> [in]

<dd>
<p>Pointer to an array of handles to DMA engines. Specify a non-<b>NULL</b> value for this parameter.</p>
</dd>
</dl>

## -returns
<p><i>SetDmaEngineState</i> returns STATUS_SUCCESS if the call succeeds in changing the DMA engines' states. Otherwise, the routine returns an appropriate error code. The following table shows some of the possible return status codes.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>Indicates that one of the handles is invalid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that one of the parameter values is incorrect (invalid parameter value or bad pointer).</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>Indicates that no buffer is currently allocated for one of the DMA engines.</p>

<p> </p>

## -remarks
<p>This routine changes the state of one or more DMA engines to the state that the <i>streamState</i> parameter specifies. The routine synchronizes the state transitions of all the DMA engines that the handles in the <i>handles</i> array identify. For more information, see <a href="NULL">Synchronizing Two or More Streams</a>.</p>

<p>Before calling this routine, set up each DMA engine in the <i>handles</i> array:</p>

<p>If using the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI, call <a href="https://msdn.microsoft.com/44fd988a-24b3-4587-88d9-30585800ffbf">AllocateDmaBuffer</a> to set up the DMA engine.</p>

<p>If using the HDAUDIO_BUS_INTERFACE_BDL version of the DDI, call <a href="https://msdn.microsoft.com/2760579b-9922-4709-a049-a73f3abd5043">SetupDmaEngineWithBdl</a> to set up the DMA engine.</p>

<p>If no DMA buffer is currently allocated for any DMA engine in the <i>handles</i> array, an attempt to change the stream to any state other than Reset causes the <i>SetDmaEngineState</i> call to fail and return error code STATUS_INVALID_DEVICE_REQUEST.</p>

<p>The stream state cannot transition directly between Running and Reset. Instead, the stream must first pass through an intermediate state of Paused or Stopped:</p>

<p>From a Running or Reset state, the stream state can change directly to either Paused or Stopped.</p>

<p>From a paused or stopped state, the stream state can change directly to either Running or Reset.</p>

<p>A WDM audio driver calls this routine during a call to its <b>SetState</b> method. For example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536720">IMiniportWaveCyclicStream::SetState</a>.</p>

<p>This routine changes the state of one or more DMA engines to the state that the <i>streamState</i> parameter specifies. The routine synchronizes the state transitions of all the DMA engines that the handles in the <i>handles</i> array identify. For more information, see <a href="NULL">Synchronizing Two or More Streams</a>.</p>

<p>Before calling this routine, set up each DMA engine in the <i>handles</i> array:</p>

<p>If using the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI, call <a href="https://msdn.microsoft.com/44fd988a-24b3-4587-88d9-30585800ffbf">AllocateDmaBuffer</a> to set up the DMA engine.</p>

<p>If using the HDAUDIO_BUS_INTERFACE_BDL version of the DDI, call <a href="https://msdn.microsoft.com/2760579b-9922-4709-a049-a73f3abd5043">SetupDmaEngineWithBdl</a> to set up the DMA engine.</p>

<p>If no DMA buffer is currently allocated for any DMA engine in the <i>handles</i> array, an attempt to change the stream to any state other than Reset causes the <i>SetDmaEngineState</i> call to fail and return error code STATUS_INVALID_DEVICE_REQUEST.</p>

<p>The stream state cannot transition directly between Running and Reset. Instead, the stream must first pass through an intermediate state of Paused or Stopped:</p>

<p>From a Running or Reset state, the stream state can change directly to either Paused or Stopped.</p>

<p>From a paused or stopped state, the stream state can change directly to either Running or Reset.</p>

<p>A WDM audio driver calls this routine during a call to its <b>SetState</b> method. For example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536720">IMiniportWaveCyclicStream::SetState</a>.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
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
<a href="https://msdn.microsoft.com/44fd988a-24b3-4587-88d9-30585800ffbf">AllocateDmaBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2760579b-9922-4709-a049-a73f3abd5043">SetupDmaEngineWithBdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536720">IMiniportWaveCyclicStream::SetState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PSET_DMA_ENGINE_STATE callback function%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
