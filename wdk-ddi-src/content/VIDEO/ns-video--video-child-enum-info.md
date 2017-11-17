---
UID: NS.video._VIDEO_CHILD_ENUM_INFO
title: VIDEO_CHILD_ENUM_INFO
author: windows-driver-content
description: Describes the child device to be enumerated by the miniport driver. All members are set by the video port driver.
old-location: display\video_child_enum_info.htm
ms.assetid: ce3b17e9-bcbd-46a4-b379-472abfdb4c2a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_CHILD_ENUM_INFO
req.alt-loc: video.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
ms.keywords: VIDEO_CHILD_ENUM_INFO, VIDEO_CHILD_ENUM_INFO, *PVIDEO_CHILD_ENUM_INFO
req.iface: 
req.product: Windows 10 or later.
---

# VIDEO_CHILD_ENUM_INFO structure



## -description
<p>Describes the child device to be enumerated by the miniport driver. All members are set by the video port driver.</p>


## -syntax

````
typedef struct _VIDEO_CHILD_ENUM_INFO {
  ULONG Size;
  ULONG ChildDescriptorSize;
  ULONG ChildIndex;
  ULONG ACPIHwId;
  PVOID ChildHwDeviceExtension;
} VIDEO_CHILD_ENUM_INFO, *PVIDEO_CHILD_ENUM_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field <b>ChildDescriptorSize</b>

<dd>
<p>The size in bytes of the buffer to which <i>pChildDescriptor</i> points. The video port driver allocates this buffer to be large enough to accommodate a DDC2-compliant EDID structure.</p>
</dd>

### -field <b>ChildIndex</b>

<dd>
<p>The index of the child device for which the system is requesting information. This member is used to enumerate devices that are not enumerated by ACPI or other operating system components. If <b>ChildIndex</b> is set to zero, the driver should use the value specified in <b>ACPIHwId</b> as the ID of the device being enumerated.</p>
</dd>

### -field <b>ACPIHwId</b>

<dd>
<p>The identifier returned by the ACPI BIOS that represents the child device being enumerated. The miniport driver should use this member only if <b>ChildIndex</b> is zero.</p>
<p>The <b>ACPIHwId</b> returned by the firmware must match the value returned in <i>UId</i> by the miniport driver. The System BIOS manufacturer and the graphics IHV must synchronize these IDs.</p>
</dd>

### -field <b>ChildHwDeviceExtension</b>

<dd>
<p>A pointer to a device extension specific to this child device. This member is valid only if the miniport driver filled the <b>ChildHwDeviceExtensionSize</b> member of VIDEO_HW_INITIALIZATION_DATA with a value other than zero.</p>
</dd>
</dl>

## -remarks
<p>One parameter of the <i>HwVidGetVideoChildDescriptor</i> function is an instance of a VIDEO_CHILD_ENUM_INFO structure. </p>

<p>The ACPI_METHOD_DISPLAY_DOD alias, defined in Dispmprt.h, represents the method used to enumerate the devices attached to the display adapter. This method is required if the integrated device controller supports switching of output devices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/175030c1-95d9-4a3b-976c-16e04852cb91">HwVidGetVideoChildDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570505">VIDEO_HW_INITIALIZATION_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_CHILD_ENUM_INFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
