---
UID: NS.ksmedia._KSAUDIOMODULE_PROPERTY
title: KSAUDIOMODULE_PROPERTY
author: windows-driver-content
description: The KSAUDIOMODULE_DESCRIPTOR structure describes the static, external properties of the audio modules.
old-location: audio\ksaudiomodule_property.htm
ms.assetid: 1DE3F065-6F8E-402F-87EF-F9582E31BFFE
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSAUDIOMODULE_PROPERTY
req.alt-loc: Ksmedia.h
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
ms.keywords: KSAUDIOMODULE_PROPERTY, KSAUDIOMODULE_PROPERTY, *PKSAUDIOMODULE_PROPERTY
req.iface: 
---

# KSAUDIOMODULE_PROPERTY structure



## -description
<p>The <b>KSAUDIOMODULE_DESCRIPTOR</b> structure describes the static, external  properties of the audio modules.</p>


## -syntax

````
typedef struct _KSAUDIOMODULE_PROPERTY {
    KSPROPERTY Property;
  GUID         ClassId;
  ULONG        InstanceId;
} KSAUDIOMODULE_PROPERTY, *PKSAUDIOMODULE_PROPERTY;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>The KSPROPERTY of the audio module is defined as follows.</p>
<dl>
<dd>property.Set = KSPROPSETID_AudioModule;
</dd>
<dd>property.Id = KSPROPERTY_AUDIOMODULE_COMMAND;


</dd>
<dd>property.Flags = KSPROPERTY_TYPE_GET;</dd>
</dl>
</dd>

### -field <b>ClassId</b>

<dd>
<p>The ClassId of the audio module. The ClassId is an identifier that establishes what type of module this is. The value and mapping is established by the ISV and IHV.</p>
</dd>

### -field <b>InstanceId</b>

<dd>
<p>The InstanceId of the audio module.  The InstanceId is a unique identifier that distinguishes this instance of a module from another instance of an module. </p>
</dd>
</dl>

## -remarks
<p>For more information about audio modules, see  <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/EAD613AA-005B-4751-B60E-212853CA40B4">KSPROPERTY_AUDIOMODULE_DESCRIPTORS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSAUDIOMODULE_PROPERTY structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
