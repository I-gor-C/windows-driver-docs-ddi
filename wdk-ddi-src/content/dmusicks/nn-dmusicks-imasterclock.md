---
UID: NN:dmusicks.IMasterClock
title: IMasterClock
author: windows-driver-content
description: The IMasterClock interface provides Microsoft DirectMusic streams with access to the current reference time from the master clock.
old-location: audio\imasterclock.htm
old-project: audio
ms.assetid: 754aad8a-834c-4197-8505-dbf1cd74c697
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IMasterClock, IMasterClock interface [Audio Devices], IMasterClock interface [Audio Devices], described, audio.imasterclock, audmp-routines_b8172e0e-55ac-4abd-8b62-39be5d708f9b.xml, dmusicks/IMasterClock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dmusicks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: dmusicks.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dmusicks.h
api_name:
-	IMasterClock
product: Windows
targetos: Windows
req.typenames: DMUS_STREAM_TYPE
---

# IMasterClock interface

The <code>IMasterClock</code> interface provides Microsoft DirectMusic streams with access to the current reference time from the <a href="https://msdn.microsoft.com/bdd228c1-a15f-4c08-8991-299a3f2e1ee8">master clock</a>. The DMus port driver implements this interface to support accurate timing in the <a href="..\dmusicks\nn-dmusicks-imxf.md">IMXF</a> and <a href="..\dmusicks\nn-dmusicks-iallocatormxf.md">IAllocatorMXF</a> interfaces that make up the MIDI-transport part of the filter graph. When calling a DMus miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536701">IMiniportDMus::NewStream</a> method, the DMus port driver passes an <code>IMasterClock</code> reference as a call parameter. The <code>IMasterClock</code> interface wraps the master clock, as described in <a href="https://msdn.microsoft.com/3cdd4c69-d99d-48bc-a1d9-9da2a2511e94">Latency Clocks</a>.

## Methods

<p>The <b>IMasterClock</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IMasterClock::GetTime](nf-dmusicks-imasterclock-gettime.md) | The GetTime method retrieves the current reference time read from the master clock. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dmusicks.h |