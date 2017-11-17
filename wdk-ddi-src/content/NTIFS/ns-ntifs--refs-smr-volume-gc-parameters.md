---
UID: NS.ntifs._REFS_SMR_VOLUME_GC_PARAMETERS
title: REFS_SMR_VOLUME_GC_PARAMETERS
author: windows-driver-content
description: The REFS_SMR_VOLUME_GC_PARAMETERS structure.
old-location: ifsk\refs_smr_volume_gc_parameters.htm
ms.assetid: 78C8FFFE-8A80-4C92-B822-5C6675E2BC18
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REFS_SMR_VOLUME_GC_PARAMETERS
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
req.irql: 
ms.keywords: REFS_SMR_VOLUME_GC_PARAMETERS, REFS_SMR_VOLUME_GC_PARAMETERS, *PREFS_SMR_VOLUME_GC_PARAMETERS
req.iface: 
---

# REFS_SMR_VOLUME_GC_PARAMETERS structure



## -description
<p>The <b>REFS_SMR_VOLUME_GC_PARAMETERS</b> structure is used as the input structure for <a href="https://msdn.microsoft.com/782542C4-CFC5-4BF7-AF38-3247A3AC6AB9">FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS</a>.</p>


## -syntax

````
typedef struct _REFS_SMR_VOLUME_GC_PARAMETERS {
  ULONG                     Version;
  ULONG                     Flags;
  REFS_SMR_VOLUME_GC_ACTION Action;
  REFS_SMR_VOLUME_GC_METHOD Method;
  ULONG                     IoGranularity;
  ULONG                     CompressionFormat;
  ULONG                     Unused[8];
} REFS_SMR_VOLUME_GC_PARAMETERS, *PREFS_SMR_VOLUME_GC_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Specifies the current version of <b>REFS_SMR_VOLUME_GC_PARAMETERS</b>. Version is currently ignored but should be set to <b>REFS_SMR_VOLUME_GC_PARAMETERS_VERSION_V1</b>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the flags. Flags is currently ignored.</p>
</dd>

### -field <b>Action</b>

<dd>
<p>Specifies the garbage collection action.</p>
</dd>

### -field <b>Method</b>

<dd>
<p>Specifies the garbage collection method or strategy. Currently only <b>MsSmrGcMethodCompaction</b> is allowed.</p>
</dd>

### -field <b>IoGranularity</b>

<dd>
<p>Specifies the volume's granularity. <b>IoGranularity</b> is a multiple of the cluster size up to the Shingled Magnetic Recording (SMR) band size (256 MB).  Zero or non-multiple of cluster size will result in a <b>STATUS_INVALID_PARAMETERS</b> status.</p>
</dd>

### -field <b>CompressionFormat</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Unused</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/782542C4-CFC5-4BF7-AF38-3247A3AC6AB9">FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20REFS_SMR_VOLUME_GC_PARAMETERS structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
