---
UID: NS.dispmprt._DXGK_CHILD_CAPABILITIES
title: DXGK_CHILD_CAPABILITIES
author: windows-driver-content
description: The DXGK_CHILD_CAPABILITIES structure contains information about the capabilities of an individual child device of a display adapter.
old-location: display\dxgk_child_capabilities.htm
old-project: display
ms.assetid: 6ab6a505-ad02-4dce-8061-bba13081208a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHILD_CAPABILITIES, DXGK_CHILD_CAPABILITIES, *PDXGK_CHILD_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CHILD_CAPABILITIES
req.alt-loc: dispmprt.h
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

# DXGK_CHILD_CAPABILITIES structure



## -description
<p>The DXGK_CHILD_CAPABILITIES structure contains information about the capabilities of an individual child device of a display adapter.</p>


## -syntax

````
typedef struct _DXGK_CHILD_CAPABILITIES {
  union {
    DXGK_VIDEO_OUTPUT_CAPABILITIES VideoOutput;
    struct {
      UINT MustBeZero;
    } Other;
    DXGK_INTEGRATED_DISPLAY_CHILD  IntegratedDisplayChild;
  } Type;
  DXGK_CHILD_DEVICE_HPD_AWARENESS HpdAwareness;
} DXGK_CHILD_CAPABILITIES, *PDXGK_CHILD_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>
      A union that can contain either video output information or other information in the following members. 
     </p>
<dl>

### -field <b>VideoOutput</b>

<dd>
<p>A <a href="..\dispmprt\ns-dispmprt--dxgk-video-output-capabilities.md">DXGK_VIDEO_OUTPUT_CAPABILITIES</a> structure that contains information about a video output. This member is meaningful only if the child device has type <b>TypeVideoOutput</b>.</p>
</dd>

### -field <b>Other</b>

<dd>
<p>A structure whose only member must be equal to zero if the child device has type <b>TypeOther</b>.</p>
<dl>

### -field <b>MustBeZero</b>

<dd>
<p>A UINT value that must be equal to zero.</p>
</dd>
</dl>
</dd>

### -field <b>IntegratedDisplayChild</b>

<dd>
<p>Returns the integrated display child specific fields of the child capabilities.</p>
</dd>
</dl>
</dd>

### -field <b>HpdAwareness</b>

<dd>
<p>A <a href="..\d3dkmdt\ne-d3dkmdt--dxgk-child-device-hpd-awareness.md">DXGK_CHILD_DEVICE_HPD_AWARENESS</a> enumerator that indicates the child device's level of hot-plug awareness.</p>
</dd>
</dl>

## -remarks
<p>The <b>ChildDeviceType</b> member of a <a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structure is a <a href="..\dispmprt\ne-dispmprt--dxgk-child-device-type.md">DXGK_CHILD_DEVICE_TYPE</a> enumerator that indicates type of the child device: <b>TypeVideoOutput</b> or <b>TypeOther</b>.</p>

<p>If a child device is of type <b>TypeVideoOutput</b>, the <b>Type.VideoOutput</b> member of its DXGK_CHILD_DESCRIPTOR structure is a DXGK_VIDEO_OUTPUT_CAPABILITIES structure.</p>

<p>If a child device is of type <b>TypeOther</b>, then <b>Type.Other.MustBeZero</b> must be set to zero.</p>

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
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>
</dt>
<dt>
<a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\dispmprt\ns-dispmprt--dxgk-video-output-capabilities.md">DXGK_VIDEO_OUTPUT_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CHILD_CAPABILITIES structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
