---
UID: NE.ksmedia.PCAPTURE_MEMORY_ALLOCATION_FLAGS
title: PCAPTURE_MEMORY_ALLOCATION_FLAGS
author: windows-driver-content
description: The CAPTURE_MEMORY_ALLOCATION_FLAGS enumeration defines types of memory surfaces to which AVStream minidrivers can capture audio and video data.
old-location: stream\capture_memory_allocation_flags.htm
old-project: stream
ms.assetid: 3b96301a-28a5-494b-bd12-8d3d4516730e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CAPTURE_MEMORY_ALLOCATION_FLAGS
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

# PCAPTURE_MEMORY_ALLOCATION_FLAGS enumeration



## -description
<p>The CAPTURE_MEMORY_ALLOCATION_FLAGS enumeration defines types of memory surfaces to which AVStream minidrivers can capture audio and video data. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff565209">KSPROPERTY_PREFERRED_CAPTURE_SURFACE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff565130">KSPROPERTY_CURRENT_CAPTURE_SURFACE</a> requests use this type to specify property values.</p>


## -syntax

````
typedef enum  { 
  KS_CAPTURE_ALLOC_INVALID      = 0,
  KS_CAPTURE_ALLOC_SYSTEM       = 0x0001,
  KS_CAPTURE_ALLOC_VRAM         = 0x0002,
  KS_CAPTURE_ALLOC_SYSTEM_AGP   = 0x0004,
  KS_CAPTURE_ALLOC_VRAM_MAPPED  = 0x0008
} CAPTURE_MEMORY_ALLOCATION_FLAGS, *PCAPTURE_MEMORY_ALLOCATION_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="KS_CAPTURE_ALLOC_INVALID"></a><a id="ks_capture_alloc_invalid"></a><b>KS_CAPTURE_ALLOC_INVALID</b>

<dd>
<p>Invalid memory surface.</p>
</dd>

### -field <a id="KS_CAPTURE_ALLOC_SYSTEM"></a><a id="ks_capture_alloc_system"></a><b>KS_CAPTURE_ALLOC_SYSTEM</b>

<dd>
<p>Not currently supported. </p>
</dd>

### -field <a id="KS_CAPTURE_ALLOC_VRAM"></a><a id="ks_capture_alloc_vram"></a><b>KS_CAPTURE_ALLOC_VRAM</b>

<dd>
<p>Identifies a surface in display memory.</p>
</dd>

### -field <a id="KS_CAPTURE_ALLOC_SYSTEM_AGP"></a><a id="ks_capture_alloc_system_agp"></a><b>KS_CAPTURE_ALLOC_SYSTEM_AGP</b>

<dd>
<p>Identifies a surface in system memory that is tagged as AGP accessible. </p>
</dd>

### -field <a id="KS_CAPTURE_ALLOC_VRAM_MAPPED"></a><a id="ks_capture_alloc_vram_mapped"></a><b>KS_CAPTURE_ALLOC_VRAM_MAPPED</b>

<dd>
<p>Not currently supported.  </p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565209">KSPROPERTY_PREFERRED_CAPTURE_SURFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565130">KSPROPERTY_CURRENT_CAPTURE_SURFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20CAPTURE_MEMORY_ALLOCATION_FLAGS enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
