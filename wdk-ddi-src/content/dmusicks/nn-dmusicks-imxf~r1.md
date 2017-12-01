---
UID: NN.dmusicks.IMXF~r1
title: IMXF
author: windows-driver-content
description: The IMXF interface represents the DirectMusic stream on a MIDI transport filter (MXF).
old-location: audio\imxf.htm
old-project: audio
ms.assetid: 97e24c86-a97d-42ed-9402-4c387c7cec5b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ISynthSinkDMus, SyncToMaster, ISynthSinkDMus::SyncToMaster
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
req.alt-api: IMXF
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
req.iface: ISynthSinkDMus
---

# IMXF interface



## -description
<p>The <code>IMXF</code> interface represents the DirectMusic stream on a MIDI transport filter (MXF). The DMus miniport driver implements this interface and exposes it to the DMus port driver. MIDI transport occurs through IMXF, which is the DMus miniport driver's primary interface for managing DirectMusic streams. The DMus port driver uses this interface to manage a DirectMusic stream on a MIDI transport filter (MXF). The miniport driver creates a stream object with this interface when the port driver calls the miniport driver's <a href="audio.iminiportdmus_newstream">IMiniportDMus::NewStream</a> method. <code>IMXF</code> inherits from the <b>IUnknown</b> interface.</p>
<p>The <a href="..\dmusicks\nn-dmusicks-iallocatormxf~r1.md">IAllocatorMXF</a> and <a href="..\dmusicks\nn-dmusicks-isynthsinkdmus.md">ISynthSinkDMus</a> interfaces both inherit from <code>IMXF</code>. For information about using these interfaces to manage MIDI streams, see <a href="NULL">MIDI Transport</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IMXF</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusicks.h</dt>
</dl>
</td>
</tr>
</table>