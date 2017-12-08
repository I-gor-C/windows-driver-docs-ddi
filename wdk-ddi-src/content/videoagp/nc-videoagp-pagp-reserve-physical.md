---
UID: NC.videoagp.PAGP_RESERVE_PHYSICAL
title: PAGP_RESERVE_PHYSICAL
author: windows-driver-content
description: The AgpReservePhysical function reserves a range of physical addresses on the system bus to which the AGP controller can respond.
old-location: display\agpreservephysical.htm
old-project: display
ms.assetid: b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa
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
req.alt-api: AgpReservePhysical
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

# PAGP_RESERVE_PHYSICAL callback



## -description
<p>The <b>AgpReservePhysical</b> function reserves a range of physical addresses on the system bus to which the AGP controller can respond.</p>


## -prototype

````
PAGP_RESERVE_PHYSICAL AgpReservePhysical;

PHYSICAL_ADDRESS APIENTRY AgpReservePhysical(
  _In_  PVOID                 HwDeviceExtension,
  _In_  ULONG                 Pages,
  _In_  VIDEO_PORT_CACHE_TYPE Caching,
  _Out_ PVOID                 *PhysicalReserveContext
)
{ ... }
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param Pages [in]

<dd>
<p>Specifies the number of pages that the video port driver should reserve.</p>
</dd>

### -param Caching [in]

<dd>
<p>Specifies the type of caching that the system should use. This parameter can be set to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>VpNonCached</b></p>
</td>
<td>
<p>The system should not cache the range of addresses.</p>
</td>
</tr>
<tr>
<td>
<p><b>VpWriteCombined</b></p>
</td>
<td>
<p>The system should use write-combined (WC) caching. For information about WC caching, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=204787">Write-Combining Memory in Video Miniport Drivers</a> website article.</p>
</td>
</tr>
<tr>
<td>
<p><b>VpCached</b></p>
</td>
<td>
<p>The system should use ordinary caching.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param PhysicalReserveContext [out]

<dd>
<p>Specifies the location in which the video port driver writes a context handle that identifies the reserved physical address space.</p>
</dd>
</dl>

## -returns
<p><b>AgpReservePhysical</b> returns the base address of the reserved physical address range if successful; otherwise, it returns <b>NULL</b>.</p>

## -remarks
<p>Video miniport drivers that run on Microsoft Windows 2000 should always reserve a range whose size is a multiple of 64 kilobytes. Reserving a range that is not a multiple of 64 kilobytes can result in <a href="..\videoagp\nc-videoagp-pagp-reserve-virtual.md">AgpReserveVirtual</a> or <a href="..\videoagp\nc-videoagp-pagp-commit-virtual.md">AgpCommitVirtual</a> returning an invalid virtual address.</p>

<p>On Microsoft Windows XP and later, <b>AgpReservePhysical</b> automatically expands the requested range to a multiple of 64 kilobytes.</p>

<p>Upon successful return, the AGP controller can respond to the reserved physical address range on the bus. However, the video miniport driver must first call <a href="..\videoagp\nc-videoagp-pagp-commit-physical.md">AgpCommitPhysical</a> to cause this memory to be committed before accessing it in order for the accessed results to be defined.</p>

<p>The miniport driver can call <b>AgpReservePhysical</b> several times to reserve many smaller address ranges rather than one big range.</p>

<p>The miniport driver should call <a href="..\videoagp\nc-videoagp-pagp-release-physical.md">AgpReleasePhysical</a> to release the physical address range when it is no longer needed. </p>

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
<a href="..\videoagp\nc-videoagp-pagp-commit-physical.md">AgpCommitPhysical</a>
</dt>
<dt>
<a href="..\videoagp\nc-videoagp-pagp-release-physical.md">AgpReleasePhysical</a>
</dt>
<dt>
<a href="..\videoagp\nc-videoagp-pagp-reserve-virtual.md">AgpReserveVirtual</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PAGP_RESERVE_PHYSICAL callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
