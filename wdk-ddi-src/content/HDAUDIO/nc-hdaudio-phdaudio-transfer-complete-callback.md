---
UID: NC.hdaudio.PHDAUDIO_TRANSFER_COMPLETE_CALLBACK
title: PHDAUDIO_TRANSFER_COMPLETE_CALLBACK
author: windows-driver-content
description: HDAudio codec transfer complete callback function. PHDAUDIO_TRANSFER_COMPLETE_CALLBACK is used by the PTRANSFER_CODEC_VERBS callback function.
old-location: audio\phdaudio_transfer_complete_callback.htm
ms.assetid: 6B3DA3B1-33E9-4BE4-A3EE-146080C483A6
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: audio
req.header: hdaudio.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HDAudioTransferCompleteCallback
req.alt-loc: Hdaudio.h
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
ms.keywords: SM_SetRNIDMgmtInfo_OUT, SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
req.iface: 
---

# PHDAUDIO_TRANSFER_COMPLETE_CALLBACK callback



## -description
<p>HDAudio codec transfer complete callback function. <b>PHDAUDIO_TRANSFER_COMPLETE_CALLBACK</b> is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538596">PTRANSFER_CODEC_VERBS</a> callback function. </p>


## -prototype

````
PHDAUDIO_TRANSFER_COMPLETE_CALLBACK HDAudioTransferCompleteCallback;

VOID HDAudioTransferCompleteCallback(
   HDAUDIO_CODEC_TRANSFER *pHDAudioCodecTransfer,
   PVOID                  Context
)
{ ... }

typedef PHDAUDIO_TRANSFER_COMPLETE_CALLBACK HDAudioTransferCompleteCallback;
````


## -parameters
<dl>

### -param <i>pHDAudioCodecTransfer</i> 

<dd>
<p>A pointer to the codecTransfer array element that contains the codec command and the response that triggered the callback. </p>
</dd>

### -param <i>Context</i> 

<dd>
<p> This is the same  context value that was specified previously in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538596">PTRANSFER_CODEC_VERBS</a> routine's callbackContext parameter.</p>
</dd>
</dl>

## -returns
<p>Void</p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538596">PTRANSFER_CODEC_VERBS</a>.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff538596">PTRANSFER_CODEC_VERBS</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hdaudio.h</dt>
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