---
UID: NS.dispmprt._DXGK_CHILD_DESCRIPTOR
title: DXGK_CHILD_DESCRIPTOR
author: windows-driver-content
description: The DXGK_CHILD_DESCRIPTOR structure holds identification and capability information for an individual child device of the display adapter.
old-location: display\dxgk_child_descriptor.htm
old-project: display
ms.assetid: a814da0c-3712-4e7b-9349-a446d7b32c90
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHILD_DESCRIPTOR, DXGK_CHILD_DESCRIPTOR, *PDXGK_CHILD_DESCRIPTOR
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
req.alt-api: DXGK_CHILD_DESCRIPTOR
req.alt-loc: Dispmprt.h
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

# DXGK_CHILD_DESCRIPTOR structure



## -description
<p>The DXGK_CHILD_DESCRIPTOR structure holds identification and capability information for an individual child device of the display adapter.</p>


## -syntax

````
typedef struct _DXGK_CHILD_DESCRIPTOR {
  DXGK_CHILD_DEVICE_TYPE  ChildDeviceType;
  DXGK_CHILD_CAPABILITIES ChildCapabilities;
  ULONG                   AcpiUid;
  ULONG                   ChildUid;
} DXGK_CHILD_DESCRIPTOR, *PDXGK_CHILD_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>ChildDeviceType</b>

<dd>
<p>A member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561008">DXGK_CHILD_DEVICE_TYPE</a> enumeration that indicates the type of the child device.</p>
</dd>

### -field <b>ChildCapabilities</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560995">DXGK_CHILD_CAPABILITIES</a> structure that describes the capabilities of the child device.</p>
</dd>

### -field <b>AcpiUid</b>

<dd>
<p>If the child device is an ACPI device, this member contains the unique ACPI identifier of the child device.</p>
</dd>

### -field <b>ChildUid</b>

<dd>
<p>A unique identifier, created by the display miniport driver, that identifies the child device.</p>
</dd>
</dl>

## -remarks
<p>The <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a> function, implemented by the display miniport driver, fills in an array of DXGK_CHILD_DESCRIPTOR structures, one for each child device of the display adapter.</p>

<p>Each child device of type <b>TypeVideoOutput</b> is associated with a video present target, and the <b>ChildUid</b> member of this structure is used as the identifier for that video present target. Several functions implemented by the video present network (VidPN) manager receive a video present target identifier. For an example, see the <i>VidPnTargetId</i> parameter of the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561008">DXGK_CHILD_DEVICE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560995">DXGK_CHILD_CAPABILITIES</a>
</dt>
<dt>
<a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>
</dt>
<dt>
<a href="display.dxgkddiquerychildstatus">DxgkDdiQueryChildStatus</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CHILD_DESCRIPTOR structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
