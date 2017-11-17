---
UID: NS.pepfx._PEP_PPM_QUERY_COORDINATED_DEPENDENCY
title: PEP_PPM_QUERY_COORDINATED_DEPENDENCY
author: windows-driver-content
description: The PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure describes dependencies for coordinated idle states.
old-location: kernel\pep_ppm_query_coordinated_dependency.htm
ms.assetid: B7E857ED-66FF-4A4D-849B-A15663106507
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PPM_QUERY_COORDINATED_DEPENDENCY
req.alt-loc: pepfx.h
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
ms.keywords: PEP_PPM_QUERY_COORDINATED_DEPENDENCY, PEP_PPM_QUERY_COORDINATED_DEPENDENCY, *PPEP_PPM_QUERY_COORDINATED_DEPENDENCY
req.iface: 
---

# PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure



## -description
<p>The <b>PEP_PPM_QUERY_COORDINATED_DEPENDENCY</b> structure describes dependencies for coordinated idle states.</p>


## -syntax

````
typedef struct _PEP_PPM_QUERY_COORDINATED_DEPENDENCY {
  ULONG                                                                                   StateIndex;
  ULONG                                                                                   DependencyIndex;
  ULONG                                                                                   DependencySize;
  _Field_range_(0, DependencySize) ULONG                                                  DependencySizeUsed;
  POHANDLE                                                                                TargetProcessor;
  _Field_size_part_(DependencySize, DependencySizeUsed) PEP_COORDINATED_DEPENDENCY_OPTION Options[ANYSIZE_ARRAY];
} PEP_PPM_QUERY_COORDINATED_DEPENDENCY, *PPEP_PPM_QUERY_COORDINATED_DEPENDENCY;
````


## -struct-fields
<dl>

### -field <b>StateIndex</b>

<dd>
<p>[in] The index of the coordinated idle state which is having its dependencies queried.</p>
</dd>

### -field <b>DependencyIndex</b>

<dd>
<p>[in] The index of the dependency being queried.</p>
</dd>

### -field <b>DependencySize</b>

<dd>
<p>[in] The size of the <b>Dependencies</b> array.</p>
</dd>

### -field <b>DependencySizeUsed</b>

<dd>
<p>[out] The number of elements of the <b>Dependencies</b> array filled in by the PEP.</p>
</dd>

### -field <b>TargetProcessor</b>

<dd>
<p>[out] The <b>POHANDLE</b> corresponding to the processor being targeted by this dependency, or <b>NULL</b> if this is a coordinated state dependency.</p>
</dd>

### -field <b>Options</b>

<dd>
<p>[out] A list of <a href="https://msdn.microsoft.com/library/windows/hardware/mt186706">PEP_COORDINATED_DEPENDENCY_OPTION</a> structures describing dependency options, one of which must be satisfied for this coordinated state to be entered.</p>
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
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186775">PEP_NOTIFY_PPM_QUERY_COORDINATED_DEPENDENCY notification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186706">PEP_COORDINATED_DEPENDENCY_OPTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
