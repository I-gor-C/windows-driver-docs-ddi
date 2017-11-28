---
UID: NE.hdaudio._HDAUDIO_STREAM_STATE
title: HDAUDIO_STREAM_STATE
author: windows-driver-content
description: The HDAUDIO_STREAM_STATE enumeration defines constants that specify the different stream states supported by HDAudio.
old-location: audio\hdaudio_stream_state.htm
old-project: audio
ms.assetid: A1029A2D-980F-44F5-B7D6-1C37F97D0368
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: SM_SetRNIDMgmtInfo_OUT, SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: hdaudio.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HDAUDIO_STREAM_STATE
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
req.irql: PASSIVE_LEVEL.
req.iface: 
---

# HDAUDIO_STREAM_STATE enumeration



## -description
<p>The <b>HDAUDIO_STREAM_STATE</b> enumeration defines constants that specify the different stream states supported by HDAudio.</p>


## -syntax

````
typedef enum _HDAUDIO_STREAM_STATE { 
  ResetState  = 0,
  StopState   = 1,
  PauseState  = 1,
  RunState    = 2
} HDAUDIO_STREAM_STATE, *PHDAUDIO_STREAM_STATE;
````


## -enum-fields
<dl>

### -field <a id="ResetState"></a><a id="resetstate"></a><a id="RESETSTATE"></a><b>ResetState</b>

<dd>
<p>The reset state.</p>
</dd>

### -field <a id="StopState"></a><a id="stopstate"></a><a id="STOPSTATE"></a><b>StopState</b>

<dd>
<p>The stop state.</p>
</dd>

### -field <a id="PauseState"></a><a id="pausestate"></a><a id="PAUSESTATE"></a><b>PauseState</b>

<dd>
<p>The pause state.</p>
</dd>

### -field <a id="RunState"></a><a id="runstate"></a><a id="RUNSTATE"></a><b>RunState</b>

<dd>
<p>The run state.</p>
</dd>
</dl>

## -remarks
<p>This enumeration is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537889">PSET_DMA_ENGINE_STATE</a>.</p>

<p>This enumeration is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537889">PSET_DMA_ENGINE_STATE</a>.</p>

<p>This enumeration is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537889">PSET_DMA_ENGINE_STATE</a>.</p>

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
</table>