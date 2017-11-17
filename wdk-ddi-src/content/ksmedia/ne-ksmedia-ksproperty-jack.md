---
UID: NE.ksmedia.KSPROPERTY_JACK
title: KSPROPERTY_JACK
author: windows-driver-content
description: The KSPROPERTY_JACK enumeration defines new property IDs that are used by audio jack structures.
old-location: audio\ksproperty_jack.htm
ms.assetid: d20a0b08-f20e-43a2-9ff5-eb0b9d1ea54e
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_JACK
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
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
req.iface: 
---

# KSPROPERTY_JACK enumeration



## -description
<p>The <code>KSPROPERTY_JACK</code> enumeration defines new property IDs that are used by audio jack structures.</p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_JACK_DESCRIPTION   = 1,
  KSPROPERTY_JACK_DESCRIPTION2  = 2,
  KSPROPERTY_JACK_SINK_INFO     = 3,
  KSPROPERTY_JACK_CONTAINERID
} KSPROPERTY_JACK;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_JACK_DESCRIPTION"></a><a id="ksproperty_jack_description"></a><b>KSPROPERTY_JACK_DESCRIPTION</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537364">KSPROPERTY_JACK_DESCRIPTION</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_JACK_DESCRIPTION2"></a><a id="ksproperty_jack_description2"></a><b>KSPROPERTY_JACK_DESCRIPTION2</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537365">KSPROPERTY_JACK_DESCRIPTION2</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_JACK_SINK_INFO"></a><a id="ksproperty_jack_sink_info"></a><b>KSPROPERTY_JACK_SINK_INFO</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537367">KSPROPERTY_JACK_SINK_INFO</a> property.</p>
</dd>

### -field <a id="KSPROPERTY_JACK_CONTAINERID"></a><a id="ksproperty_jack_containerid"></a><b>KSPROPERTY_JACK_CONTAINERID</b>

<dd>
<p>Specifies the ID for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265129">KSPROPERTY_JACK_CONTAINERID</a> property.</p>
</dd>
</dl>

## -remarks
<p>None</p>

<p>None</p>

<p>None</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later Windows operating systems.</p>
</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537364">KSPROPERTY_JACK_DESCRIPTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSPROPERTY_JACK enumeration%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
