---
UID: NS.ksmedia._KSAUDIOMODULE_DESCRIPTOR
title: KSAUDIOMODULE_DESCRIPTOR
author: windows-driver-content
description: The KSAUDIOMODULE_DESCRIPTOR structure describes the static, external properties of audio modules.
old-location: audio\ksaudiomodule_descriptor.htm
old-project: audio
ms.assetid: 3A991D49-B873-4C03-8A5B-D91EB5E63192
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSAUDIOMODULE_DESCRIPTOR, KSAUDIOMODULE_DESCRIPTOR, *PKSAUDIOMODULE_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSAUDIOMODULE_DESCRIPTOR
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
req.iface: 
---

# KSAUDIOMODULE_DESCRIPTOR structure



## -description
<p>The <b>KSAUDIOMODULE_DESCRIPTOR</b> structure describes the static, external  properties of audio modules.</p>


## -syntax

````
typedef struct _KSAUDIOMODULE_DESCRIPTOR {
  GUID  ClassId;
  ULONG InstanceId;
  ULONG VersionMajor;
  ULONG VersionMinor;
  WCHAR Name[AUDIOMODULE_MAX_NAME_CCH_SIZE];
} KSAUDIOMODULE_DESCRIPTOR, *PKSAUDIOMODULE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field ClassId

<dd>
<p>The ClassId of the audio module. The ClassId is an identifier that establishes what type of module this is. The value and mapping is established by the ISV and IHV.</p>
</dd>

### -field InstanceId

<dd>
<p>The InstanceId of the audio module.  The InstanceId is a unique identifier that distinguishes this instance of a module from another instance of a module. </p>
</dd>

### -field VersionMajor

<dd>
<p>The major version of the audio module. Usage is defined by the implementer.</p>
</dd>

### -field VersionMinor

<dd>
<p>The minor version of the audio module.  Usage is defined by the implementer.</p>
</dd>

### -field Name[AUDIOMODULE_MAX_NAME_CCH_SIZE]

<dd>
<p>The friendly name of the audio module. The maximum length is AUDIOMODULE_MAX_NAME_CCH_SIZE wide characters. It is defined as 128 in KSMedia.h.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSAUDIOMODULE_DESCRIPTOR structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
