---
UID : NF:dmusicks.ISynthSinkDMus.Render
title : ISynthSinkDMus::Render method
author : windows-driver-content
description : The Render method renders wave data into a destination sink.
old-location : audio\isynthsinkdmus_render.htm
old-project : audio
ms.assetid : 731abdaf-f84b-4d4b-a6e0-ee11899fba27
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audio.isynthsinkdmus_render, audmp-routines_ada0270e-6234-4508-a323-f4bdaee295ce.xml, Render method [Audio Devices], ISynthSinkDMus::Render, ISynthSinkDMus interface [Audio Devices], Render method, ISynthSinkDMus, Render, dmusicks/ISynthSinkDMus::Render, Render method [Audio Devices], ISynthSinkDMus interface
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dmusicks.h
req.include-header : Dmusicks.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : dmusicks.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DMUS_STREAM_TYPE
---


# Render method
The <code>Render</code> method renders wave data into a destination sink.

## Syntax

````
void Render(
  [in] PBYTE    pbBuffer,
  [in] DWORD    dwLength,
  [in] LONGLONG llPosition
);
````

## Parameters

`pBuffer`



`dwLength`

Specifies the length (in bytes) of the data to be rendered.

`llPosition`

Specifies the position (in bytes) in the PCM buffer at which to begin rendering. Rendering continues from this position for the number of bytes specified in <i>dwLength</i>.


## Return Value

None

## Remarks

The port driver's synth-sink object calls this method when the miniport driver needs to render more wave data into the destination buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dmusicks.h (include Dmusicks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |