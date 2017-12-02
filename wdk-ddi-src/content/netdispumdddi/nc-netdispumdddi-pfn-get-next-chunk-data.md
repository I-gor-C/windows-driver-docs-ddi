---
UID: NC.netdispumdddi.PFN_GET_NEXT_CHUNK_DATA
title: PFN_GET_NEXT_CHUNK_DATA
author: windows-driver-content
description: Provides info about the next Miracast encode chunk that was reported to the Microsoft DirectX graphics kernel subsystem when the DXGK_INTERRUPT_TYPE interrupt type is DXGK_INTERRUPT_MICACAST_CHUNK_PROCESSING_COMPLETE.The data type of this function is PFN_GET_NEXT_CHUNK_DATA.
old-location: display\getnextchunkdata.htm
old-project: display
ms.assetid: 24b1d89a-4200-41ec-aa73-15b37e4cca6d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: NDK_SRQ, NDK_SRQ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetNextChunkData
req.alt-loc: Netdispumdddi.h
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
---

# PFN_GET_NEXT_CHUNK_DATA callback



## -description
<p>Provides info about the next Miracast encode chunk that was reported to the Microsoft DirectX graphics kernel subsystem when the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-interrupt-type.md">DXGK_INTERRUPT_TYPE</a> interrupt type is  <b>DXGK_INTERRUPT_MICACAST_CHUNK_PROCESSING_COMPLETE</b>.<p>The data type of this function is <b>PFN_GET_NEXT_CHUNK_DATA</b>.</p>
</p>
<p>The data type of this function is <b>PFN_GET_NEXT_CHUNK_DATA</b>.</p>


## -prototype

````
PFN_GET_NEXT_CHUNK_DATA GetNextChunkData;

NTSTATUS GetNextChunkData(
  _In_     HANDLE              hMiracastDeviceHandle,
  _In_     UINT                TimeoutInMilliseconds,
  _In_     UINT                AdditionalWaitEventCount,
  _In_opt_ HANDLE              *pAdditionalWaitEvents,
  _Inout_  UINT                *pChunkDataBufferSize,
  _Out_    MIRACAST_CHUNK_DATA *pChunkDataBuffer,
  _Out_    UINT                *pOutstandingChunksToProcess
)
{ ... }
````


## -parameters
<dl>

### -param hMiracastDeviceHandle [in]

<dd>
<p>A handle that represents a Miracast device. The Miracast user-mode driver previously obtained this handle as the <i>hMiracastDeviceHandle</i> parameter in a call to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> function.</p>
</dd>

### -param TimeoutInMilliseconds [in]

<dd>
<p>The timeout interval value, in milliseconds, supplied by the Miracast user-mode driver.</p>
<p>If this value is <b>INFINITE</b>, the operating system blocks calls to <b>GetNextChunkData</b> until a chunk becomes available.</p>
<p>If this value is zero and a chunk is not ready, the operating system will not block a call to <b>GetNextChunkData</b>.</p>
</dd>

### -param AdditionalWaitEventCount [in]

<dd>
<p>The number of additional events that are supplied in the <i>pAdditionalWaitEvents</i> parameter.</p>
<p> A maximum of 4 wait events can be supplied.</p>
</dd>

### -param pAdditionalWaitEvents [in, optional]

<dd>
<p>An optional pointer to an array of events that  <b>GetNextChunkData</b> will wait on while waiting for a new encode chunk.</p>
</dd>

### -param pChunkDataBufferSize [in, out]

<dd>
<p>A pointer to a variable that contains the size, in bytes, of the <i>pChunkDataBuffer</i> buffer.</p>
<p>When <b>GetNextChunkData</b> is called, this parameter contains the size of <i>pChunkDataBuffer</i>.</p>
<p>When  <b>GetNextChunkData</b> returns a success code, this parameter contains the size of actual encode chunk data returned in <i>pChunkDataBuffer</i>.</p>
</dd>

### -param pChunkDataBuffer [out]

<dd>
<p>A pointer to a buffer of type  <a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-data.md">MIRACAST_CHUNK_DATA</a> that the operating system provides to store information about the next encode chunk. This parameter is provided only if the call to <b>GetNextChunkData</b> is successful.</p>
</dd>

### -param pOutstandingChunksToProcess [out]

<dd>
<p>A pointer to a variable that contains the number of outstanding encode chunks that are available for the driver at the time this call returned.  This parameter is provided only if the call to <b>GetNextChunkData</b> is successful.</p>
<p>Note that as chunks are completed by the GPU asynchronously, this parameter only gives an indication of the number of outstanding chunks.</p>
</dd>
</dl>

## -returns
<p>If info on an encode chunk was returned successfully, the <b>STATUS_SUCCESS</b> status code is returned, and the value of *<i>pChunkDataBufferSize</i> is non-zero.</p>

<p>These additional status codes can be returned:</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
<dd>
<p>A chunk was available, but the provided buffer was not large enough to contain the chunk data.</p>
</dd>
<dt><b>STATUS_CONNECTION_RESET</b></dt>
<dd>
<p>The operating system ran out of free encode chunks to satisfy all chunk requests. In this case all outstanding chunks are lost, and the driver should generate a new I-Frame. Using the dropped chunks, this I-Frame will  recover  the image that the sink displayed.</p>
</dd>
<dt><b>STATUS_INSTANCE_NOT_AVAILABLE</b></dt>
<dd>
<p>The Miracast connect session was destroyed.</p>
</dd>
<dt><b>STATUS_TIMEOUT</b></dt>
<dd>
<p>A chunk was not available within the specified timeout period.</p>
</dd>
<dt><b>STATUS_WAIT_0 through STATUS_WAIT_3</b></dt>
<dd>
<p>One of the additional supplied events caused the wait criterion to be satisfied, and the value of *<i>pChunkDataBufferSize</i> is zero. The <b>STATUS_WAIT_X</b> value will match the specified index of the <i>pAdditionalWaitEvents</i> array.</p>
<p>For example, if the second event in the array caused the wait to be satisfied, then <b>STATUS_WAIT_1</b> would be returned.</p>
<p><b>STATUS_WAIT_0</b> has the same value as <b>STATUS_SUCCESS</b>, so check *<i>pChunkDataBufferSize</i> to determine if the return value was <b>STATUS_WAIT_0</b> (a user event signaled the event) or <b>STATUS_SUCCESS</b> (a new chunk is ready).</p>
</dd>
</dl><p>A chunk was available, but the provided buffer was not large enough to contain the chunk data.</p>

<p>The operating system ran out of free encode chunks to satisfy all chunk requests. In this case all outstanding chunks are lost, and the driver should generate a new I-Frame. Using the dropped chunks, this I-Frame will  recover  the image that the sink displayed.</p>

<p>The Miracast connect session was destroyed.</p>

<p>A chunk was not available within the specified timeout period.</p>

<p>One of the additional supplied events caused the wait criterion to be satisfied, and the value of *<i>pChunkDataBufferSize</i> is zero. The <b>STATUS_WAIT_X</b> value will match the specified index of the <i>pAdditionalWaitEvents</i> array.</p>

<p>For example, if the second event in the array caused the wait to be satisfied, then <b>STATUS_WAIT_1</b> would be returned.</p>

<p><b>STATUS_WAIT_0</b> has the same value as <b>STATUS_SUCCESS</b>, so check *<i>pChunkDataBufferSize</i> to determine if the return value was <b>STATUS_WAIT_0</b> (a user event signaled the event) or <b>STATUS_SUCCESS</b> (a new chunk is ready).</p>

## -remarks
<p>This function is optional. The user-mode display driver should only call it if the display miniport driver responds to  interrupts from the GPU when the GPU completes the encoding of a chunk by passing data in the <a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-data.md">MIRACAST_CHUNK_DATA</a>.<b>PrivateDriverData</b> member at that interrupt time.</p>

<p>The user-mode display driver can use the sizes of the <a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-data.md">MIRACAST_CHUNK_DATA</a> structure and the <b>MIRACAST_CHUNK_DATA</b>.<b>PrivateDriverData</b> member to compute the size of a chunk and hence how to move from chunk to chunk in the returned buffer.</p>

<p>In a call to this function, as many available packets as can fit will be placed sequentially in the supplied buffer. This code snippet shows how to calculate the size of each packet:</p>

<p>Only one thread should call this function at a time. Otherwise it's unpredictable which call would receive chunk info and which call would fail.</p>

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
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-interrupt-type.md">DXGK_INTERRUPT_TYPE</a>
</dt>
<dt>
<a href="..\netdispumdddi\ns-netdispumdddi-miracast-chunk-data.md">MIRACAST_CHUNK_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_GET_NEXT_CHUNK_DATA callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
