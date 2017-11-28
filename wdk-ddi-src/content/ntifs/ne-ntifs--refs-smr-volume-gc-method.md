---
UID: NE.ntifs._REFS_SMR_VOLUME_GC_METHOD
title: REFS_SMR_VOLUME_GC_METHOD
author: windows-driver-content
description: The REFS_SMR_VOLUME_GC_METHOD enum specifies the garbage collection method or strategy for FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS.
old-location: ifsk\refs_smr_volume_gc_method.htm
old-project: ifsk
ms.assetid: 6C58EFD4-B5F9-4E2B-AF76-E9614218E0DC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REFS_SMR_VOLUME_GC_METHOD
req.alt-loc: Ntifs.h
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
req.iface: 
---

# REFS_SMR_VOLUME_GC_METHOD enumeration



## -description
<p>The <b>REFS_SMR_VOLUME_GC_METHOD</b> enum specifies the garbage collection method or strategy for <a href="ifsk.fsctl_set_refs_smr_volume_gc_parameters">FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS</a>.</p>


## -syntax

````
typedef enum _REFS_SMR_VOLUME_GC_METHOD { 
  SmrGcMethodCompaction   = 1,
  SmrGcMethodCompression  = 2,
  SmrGcMethodRotation     = 3
} REFS_SMR_VOLUME_GC_METHOD, *PREFS_SMR_VOLUME_GC_METHOD;
````


## -enum-fields
<dl>

### -field <a id="SmrGcMethodCompaction"></a><a id="smrgcmethodcompaction"></a><a id="SMRGCMETHODCOMPACTION"></a><b>SmrGcMethodCompaction</b>

<dd>
<p>Specifies the use of the compaction method for garbage collection.  </p>
</dd>

### -field <a id="SmrGcMethodCompression"></a><a id="smrgcmethodcompression"></a><a id="SMRGCMETHODCOMPRESSION"></a><b>SmrGcMethodCompression</b>

<dd>
<p>Specifies the use of the compression method for garbage collection.</p>
</dd>

### -field <a id="SmrGcMethodRotation"></a><a id="smrgcmethodrotation"></a><a id="SMRGCMETHODROTATION"></a><b>SmrGcMethodRotation</b>

<dd>
<p>Specifies the use of the rotation method for garbage collection. Moves data from one tier to another.</p>
</dd>
</dl>

## -remarks
<p>Currently the only supported value  is <b>SmrGcMethodCompaction</b>.</p>

<p>Currently the only supported value  is <b>SmrGcMethodCompaction</b>.</p>

<p>Currently the only supported value  is <b>SmrGcMethodCompaction</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10, version 1709.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsctl_set_refs_smr_volume_gc_parameters">FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20REFS_SMR_VOLUME_GC_METHOD enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
