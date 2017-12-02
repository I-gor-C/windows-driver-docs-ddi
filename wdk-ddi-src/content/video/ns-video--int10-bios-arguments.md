---
UID: NS.video._INT10_BIOS_ARGUMENTS
title: INT10_BIOS_ARGUMENTS
author: windows-driver-content
description: The INT10_BIOS_ARGUMENTS structure is used to support full-screen MS-DOS application INT10 calls. It contains nine of the high-end x86 microprocessor registers.
old-location: display\int10_bios_arguments.htm
old-project: display
ms.assetid: 66fc9bd4-da47-4cd1-baf2-b536272ea28e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: INT10_BIOS_ARGUMENTS, INT10_BIOS_ARGUMENTS, *PINT10_BIOS_ARGUMENTS
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
req.alt-api: INT10_BIOS_ARGUMENTS
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

# INT10_BIOS_ARGUMENTS structure



## -description
<p>The INT10_BIOS_ARGUMENTS structure is used to support full-screen MS-DOS application INT10 calls. It contains nine of the high-end x86 microprocessor registers.</p>


## -syntax

````
typedef struct _INT10_BIOS_ARGUMENTS {
  ULONG  Eax;
  ULONG  Ebx;
  ULONG  Ecx;
  ULONG  Edx;
  ULONG  Esi;
  ULONG  Edi;
  ULONG  Ebp;
  USHORT SegDs;
  USHORT SegEs;
} INT10_BIOS_ARGUMENTS, *PINT10_BIOS_ARGUMENTS;
````


## -struct-fields
<dl>

### -field Eax

<dd></dd>

### -field Ebx

<dd></dd>

### -field Ecx

<dd></dd>

### -field Edx

<dd></dd>

### -field Esi

<dd></dd>

### -field Edi

<dd></dd>

### -field Ebp

<dd>
<p>Are seven of the x86 microprocessor registers.</p>
</dd>

### -field SegDs

<dd></dd>

### -field SegEs

<dd>
<p>Are two of the x86 microprocessor segment registers.</p>
</dd>
</dl>

## -remarks
<p>The first seven members of the INT10_BIOS_ARGUMENTS structure are identical to those of the <a href="..\video\ns-video--video-x86-bios-arguments.md">VIDEO_x86_BIOS_ARGUMENTS</a> structure.</p>

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
<a href="..\video\nc-video-pint10-call-bios.md">Int10CallBios</a>
</dt>
<dt>
<a href="..\video\ns-video--video-x86-bios-arguments.md">VIDEO_x86_BIOS_ARGUMENTS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20INT10_BIOS_ARGUMENTS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
