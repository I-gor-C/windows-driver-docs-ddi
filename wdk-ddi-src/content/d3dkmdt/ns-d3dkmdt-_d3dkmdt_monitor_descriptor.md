---
UID: NS.D3DKMDT._D3DKMDT_MONITOR_DESCRIPTOR
title: _D3DKMDT_MONITOR_DESCRIPTOR
author: windows-driver-content
description: The D3DKMDT_MONITOR_DESCRIPTOR structure contains a pointer to a monitor descriptor along with information about the monitor descriptor.
old-location: display\d3dkmdt_monitor_descriptor.htm
old-project: display
ms.assetid: 4bdce35f-adce-4898-8ef5-011a5476065a
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _D3DKMDT_MONITOR_DESCRIPTOR, D3DKMDT_MONITOR_DESCRIPTOR
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
---

# _D3DKMDT_MONITOR_DESCRIPTOR structure



## -description
The D3DKMDT_MONITOR_DESCRIPTOR structure contains a pointer to a monitor descriptor along with information about the monitor descriptor.



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

### -field Id

An integer that identifies the monitor descriptor.


### -field Type

A value from the <a href="display.d3dkmdt_monitor_descriptor_type">D3DKMDT_MONITOR_DESCRIPTOR_TYPE</a> enumeration that indicates the descriptor type.


### -field DataSize

The size, in bytes, of the monitor descriptor.


### -field pData

A pointer to the monitor descriptor.


### -field Origin

A value of type <a href="display.d3dkmdt_monitor_capabilities_origin">D3DKMDT_MONITOR_CAPABILITIES_ORIGIN</a> that indicates the source of the mode information for the monitor. For example, the mode information could be from a default monitor profile or it could be from an override in an INF file.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="display.d3dkmdt_monitor_capabilities_origin">D3DKMDT_MONITOR_CAPABILITIES_ORIGIN</a>
</dt>
<dt>
<a href="display.d3dkmdt_monitor_descriptor_type">D3DKMDT_MONITOR_DESCRIPTOR_TYPE</a>
</dt>
<dt>
<a href="display.monitor_descriptor_set_interface">Monitor Descriptor Set Interface</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MONITOR_DESCRIPTOR structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

