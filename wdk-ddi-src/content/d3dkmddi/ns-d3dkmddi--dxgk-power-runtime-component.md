---
UID: NS.d3dkmddi._DXGK_POWER_RUNTIME_COMPONENT
title: DXGK_POWER_RUNTIME_COMPONENT
author: windows-driver-content
description: Describes information about a power component&#8212;for example, a graphics processing engine, a display device, or a block of memory.
old-location: display\dxgk_power_runtime_component.htm
old-project: display
ms.assetid: ed7e6fc4-651d-4dc3-9c90-cca3c5f0eb67
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_POWER_RUNTIME_COMPONENT, DXGK_POWER_RUNTIME_COMPONENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_POWER_RUNTIME_COMPONENT
req.alt-loc: D3dkmddi.h
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

# DXGK_POWER_RUNTIME_COMPONENT structure



## -description
<p>Describes information about a <i>power component</i>—for example, a graphics processing engine, a display device, or a block of memory.</p>


## -syntax

````
typedef struct _DXGK_POWER_RUNTIME_COMPONENT {
  ULONG                        StateCount;
  DXGK_POWER_RUNTIME_STATE     States[DXGK_MAX_F_STATES];
  DXGK_POWER_COMPONENT_MAPPING ComponentMapping;
  DXGK_POWER_COMPONENT_FLAGS   Flags;
  GUID                         ComponentGuid;
  UCHAR                        ComponentName[DXGK_POWER_COMPONENT_NAME_SIZE];
  ULONG                        ProviderCount;
  ULONG                        Providers[DXGK_MAX_POWER_COMPONENT_PROVIDERS];
} DXGK_POWER_RUNTIME_COMPONENT;
````


## -struct-fields
<dl>

### -field <b>StateCount</b>

<dd>
<p>Defines the number of idle states (F-states) for the power component.</p>
</dd>

### -field <b>States</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh464076">DXGK_POWER_RUNTIME_STATE</a> structure that defines information about every idle state. </p>
<p><b>DXGK_MAX_F_STATES</b> is the maximum number of F-states that a power component can have. In Windows 8, <b>DXGK_MAX_F_STATES</b> is defined to have a value of 8.</p>
</dd>

### -field <b>ComponentMapping</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh464067">DXGK_POWER_COMPONENT_MAPPING</a> structure that defines the standard component types of the DirectX graphics kernel subsystem (Dxgkrnl.sys) that describe the power component.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh464063">DXGK_POWER_COMPONENT_FLAGS</a> structure that specifies power state transition information.</p>
</dd>

### -field <b>ComponentGuid</b>

<dd>
<p>A GUID that identifies the power component. This GUID is used by the Power Engine Plug-in (PEP).</p>
</dd>

### -field <b>ComponentName</b>

<dd>
<p>A name for the power component. This name is used by GPU profiling tools and is not passed to the PEP.</p>
</dd>

### -field <b>ProviderCount</b>

<dd>
<p>Defines the number of other power components that need to be active before this power component becomes active.</p>
</dd>

### -field <b>Providers</b>

<dd>
<p>Specifies the indices of other power components that need to be active before this power component becomes active. Each index value must be less than the total number of power components.</p>
</dd>
</dl>

## -remarks
<p>Each power component must be mapped to an engine, a display, a memory segment, or another similar device component. The DirectX graphics kernel subsystem detects the idle state of engines, displays, and memory segments.</p>

<p>Multiple power components should not be mapped to the same engine (node), to the same memory segment, or to the same VidPN source or target. A power component can be used with only one engine, memory segment, or VidPN source.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464063">DXGK_POWER_COMPONENT_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464067">DXGK_POWER_COMPONENT_MAPPING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464076">DXGK_POWER_RUNTIME_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_POWER_RUNTIME_COMPONENT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
