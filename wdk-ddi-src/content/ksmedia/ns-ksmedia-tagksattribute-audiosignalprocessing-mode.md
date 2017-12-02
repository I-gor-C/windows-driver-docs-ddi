---
UID: NS.ksmedia.tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE
title: tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE
author: windows-driver-content
description: The KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE structure specifies an audio signal processing mode.
old-location: audio\ksattribute_audiosignalprocessing_mode.htm
old-project: audio
ms.assetid: A7EE4FC5-420A-419A-98D1-3411C29F1990
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE, KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE, *PKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE
req.alt-loc: ksmedia.h
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

# tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE structure



## -description
<p>The KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE structure specifies an audio signal processing mode.</p>
<p>This structure is used to by mode aware drivers with  <a href="stream.ksdataformat">KSDATAFORMAT</a> which contain a  <a href="https://msdn.microsoft.com/library/windows/hardware/ff563441">KSMULTIPLE_ITEM</a> of <a href="stream.ksattribute">KSATTRIBUTE</a> structures that reference a KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE. The KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE AttributeHeader.Attribute member is set to KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE, and the KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE SignalProcessingMode member is set to AUDIO_SIGNALPROCESSINGMODE_DEFAULT or other processing modes that the driver supports. For more information, see <a href="https://msdn.microsoft.com/44b55a5a-ec58-4c1e-b780-e20829fe3edf">KS Data Formats and Data Ranges</a>.</p>


## -syntax

````
typedef struct _KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE {
  KSATTRIBUTE AttributeHeader;
  GUID        SignalProcessingMode;
} KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE, *PKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE;
````


## -struct-fields
<dl>

### -field AttributeHeader

<dd>
<p>The AttributeHeader member specifies the attribute header using a <a href="stream.ksattribute">KSATTRIBUTE</a> data type.</p>
</dd>

### -field SignalProcessingMode

<dd>
<p>The SignalProcessingMode member specifies the unique GUIDs of the SignalProcessingMode. For more information, see <a href="https://msdn.microsoft.com/104275F8-2302-484B-B673-7448CAA1F793">Audio Signal Processing Modes</a>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>