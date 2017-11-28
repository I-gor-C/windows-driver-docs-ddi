---
UID: NS.video._VIDEO_PORT_INT10_INTERFACE
title: VIDEO_PORT_INT10_INTERFACE
author: windows-driver-content
description: The VIDEO_PORT_INT10_INTERFACE structure provides a way to allocate and deallocate memory in another thread's context, read from and write to that memory, and make INT10 BIOS calls.
old-location: display\video_port_int10_interface.htm
old-project: display
ms.assetid: 551b2255-c221-4a95-a812-dec34f09438b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_PORT_INT10_INTERFACE, VIDEO_PORT_INT10_INTERFACE, *PVIDEO_PORT_INT10_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_PORT_INT10_INTERFACE
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
req.iface: 
req.product: Windows 10 or later.
---

# VIDEO_PORT_INT10_INTERFACE structure



## -description
<p>The VIDEO_PORT_INT10_INTERFACE structure provides a way to allocate and deallocate memory in another thread's context, read from and write to that memory, and make INT10 BIOS calls.</p>


## -syntax

````
typedef struct _VIDEO_PORT_INT10_INTERFACE {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  PINT10_ALLOCATE_BUFFER Int10AllocateBuffer;
  PINT10_FREE_BUFFER     Int10FreeBuffer;
  PINT10_READ_MEMORY     Int10ReadMemory;
  PINT10_WRITE_MEMORY    Int10WriteMemory;
  PINT10_CALL_BIOS       Int10CallBios;
} VIDEO_PORT_INT10_INTERFACE, *PVIDEO_PORT_INT10_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size in bytes of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the version of the interface to be returned by the video port driver. The current interface version is defined in <i>video.h</i> and has the form VIDEO_PORT_INT10_INTERFACE_<i>N</i>.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Pointer to a video port driver-defined context for the interface.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>Pointer to the video port driver-implemented reference routine for this interface.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>Pointer to the video port driver-implemented dereference routine for this interface.</p>
</dd>

### -field <b>Int10AllocateBuffer</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\video\nc-video-pint10-allocate-buffer.md">Int10AllocateBuffer</a> routine.</p>
</dd>

### -field <b>Int10FreeBuffer</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\video\nc-video-pint10-free-buffer.md">Int10FreeBuffer</a> routine.</p>
</dd>

### -field <b>Int10ReadMemory</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\video\nc-video-pint10-read-memory.md">Int10ReadMemory</a> routine.</p>
</dd>

### -field <b>Int10WriteMemory</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\video\nc-video-pint10-write-memory.md">Int10WriteMemory</a> routine.</p>
</dd>

### -field <b>Int10CallBios</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\video\nc-video-pint10-call-bios.md">Int10CallBios</a> routine.</p>
</dd>
</dl>

## -remarks
<p>PnP video miniport drivers that intend to make BIOS calls should fill in the <b>Size</b> and <b>Version</b> members of this structure, and then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff570337">VideoPortQueryServices</a>, which initializes the remaining members of this structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570337">VideoPortQueryServices</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_PORT_INT10_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
