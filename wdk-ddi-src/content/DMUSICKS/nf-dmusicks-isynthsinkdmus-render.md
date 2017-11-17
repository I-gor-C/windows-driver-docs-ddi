---
UID: NF.dmusicks.ISynthSinkDMus.Render
title: ISynthSinkDMus::Render
author: windows-driver-content
description: The Render method renders wave data into a destination sink.
old-location: audio\isynthsinkdmus_render.htm
ms.assetid: 731abdaf-f84b-4d4b-a6e0-ee11899fba27
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: dmusicks.h
req.include-header: Dmusicks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISynthSinkDMus.Render
req.alt-loc: dmusicks.h
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
ms.keywords: ISynthSinkDMus, Render, ISynthSinkDMus::Render
req.iface: ISynthSinkDMus
---

# ISynthSinkDMus::Render method



## -description
<p>The <code>Render</code> method renders wave data into a destination sink.</p>


## -syntax

````
void Render(
  [in] PBYTE    pbBuffer,
  [in] DWORD    dwLength,
  [in] LONGLONG llPosition
);
````


## -parameters
<dl>

### -param <i>pbBuffer</i> [in]

<dd>
<p>Pointer to the buffer that the synth sink wants data written to</p>
</dd>

### -param <i>dwLength</i> [in]

<dd>
<p>Specifies the length (in bytes) of the data to be rendered.</p>
</dd>

### -param <i>llPosition</i> [in]

<dd>
<p>Specifies the position (in bytes) in the PCM buffer at which to begin rendering. Rendering continues from this position for the number of bytes specified in <i>dwLength</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The port driver's synth-sink object calls this method when the miniport driver needs to render more wave data into the destination buffer.</p>

<p>The port driver's synth-sink object calls this method when the miniport driver needs to render more wave data into the destination buffer.</p>

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
<dt>Dmusicks.h (include Dmusicks.h)</dt>
</dl>
</td>
</tr>
</table>