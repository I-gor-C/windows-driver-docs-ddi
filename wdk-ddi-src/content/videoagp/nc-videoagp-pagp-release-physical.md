---
UID: NC.videoagp.PAGP_RELEASE_PHYSICAL
title: PAGP_RELEASE_PHYSICAL
author: windows-driver-content
description: The AgpReleasePhysical function frees a physical address range reserved by a previous call to AgpReservePhysical.
old-location: display\agpreleasephysical.htm
old-project: display
ms.assetid: 4da0f5cb-a017-4df5-958b-c76b7a08495a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VPOSVERSIONINFO, VPOSVERSIONINFO, *PVPOSVERSIONINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: videoagp.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AgpReleasePhysical
req.alt-loc: videoagp.h
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
req.product: Windows 10 or later.
---

# PAGP_RELEASE_PHYSICAL callback



## -description
<p>The <b>AgpReleasePhysical</b> function frees a physical address range reserved by a previous call to <a href="..\videoagp\nc-videoagp-pagp-reserve-physical.md">AgpReservePhysical</a>.</p>


## -prototype

````
PAGP_RELEASE_PHYSICAL AgpReleasePhysical;

VOID APIENTRY AgpReleasePhysical(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID PhysicalReserveContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>PhysicalReserveContext</i> [in]

<dd>
<p>Is the context handle that identifies the reserved physical address range to be released. This context was obtained from <a href="..\videoagp\nc-videoagp-pagp-reserve-physical.md">AgpReservePhysical</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The miniport driver must call <a href="..\videoagp\nc-videoagp-pagp-free-physical.md">AgpFreePhysical</a> to unmap all committed memory within the address range identified by <b>PhysicalReserveContext</b> before calling <b>AgpReleasePhysical</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Videoagp.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\videoagp\nc-videoagp-pagp-free-physical.md">AgpFreePhysical</a>
</dt>
<dt>
<a href="..\videoagp\nc-videoagp-pagp-reserve-physical.md">AgpReservePhysical</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PAGP_RELEASE_PHYSICAL callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
