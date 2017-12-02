---
UID: NS.d3dkmdt._D3DKMDT_MONITOR_DESCRIPTOR
title: D3DKMDT_MONITOR_DESCRIPTOR
author: windows-driver-content
description: The D3DKMDT_MONITOR_DESCRIPTOR structure contains a pointer to a monitor descriptor along with information about the monitor descriptor.
old-location: display\d3dkmdt_monitor_descriptor.htm
old-project: display
ms.assetid: 4bdce35f-adce-4898-8ef5-011a5476065a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_MONITOR_DESCRIPTOR,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_DESCRIPTOR
req.alt-loc: d3dkmdt.h
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

# D3DKMDT_MONITOR_DESCRIPTOR structure



## -description
<p>The D3DKMDT_MONITOR_DESCRIPTOR structure contains a pointer to a monitor descriptor along with information about the monitor descriptor.</p>


## -syntax

````
typedef struct _D3DKMDT_MONITOR_DESCRIPTOR {
  D3DKMDT_MONITOR_DESCRIPTOR_ID       Id;
  D3DKMDT_MONITOR_DESCRIPTOR_TYPE     Type;
  SIZE_T                              DataSize;
  VOID                                *pData;
  D3DKMDT_MONITOR_CAPABILITIES_ORIGIN Origin;
} D3DKMDT_MONITOR_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field Id

<dd>
<p>An integer that identifies the monitor descriptor.</p>
</dd>

### -field Type

<dd>
<p>A value from the <a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-monitor-descriptor-type.md">D3DKMDT_MONITOR_DESCRIPTOR_TYPE</a> enumeration that indicates the descriptor type.</p>
</dd>

### -field DataSize

<dd>
<p>The size, in bytes, of the monitor descriptor.</p>
</dd>

### -field pData

<dd>
<p>A pointer to the monitor descriptor.</p>
</dd>

### -field Origin

<dd>
<p>A value of type <a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-monitor-capabilities-origin.md">D3DKMDT_MONITOR_CAPABILITIES_ORIGIN</a> that indicates the source of the mode information for the monitor. For example, the mode information could be from a default monitor profile or it could be from an override in an INF file.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-monitor-capabilities-origin.md">D3DKMDT_MONITOR_CAPABILITIES_ORIGIN</a>
</dt>
<dt>
<a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-monitor-descriptor-type.md">D3DKMDT_MONITOR_DESCRIPTOR_TYPE</a>
</dt>
<dt>
<a href="display.monitor_descriptor_set_interface">Monitor Descriptor Set Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MONITOR_DESCRIPTOR structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
