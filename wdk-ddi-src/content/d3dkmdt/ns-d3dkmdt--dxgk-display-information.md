---
UID: NS.d3dkmdt._DXGK_DISPLAY_INFORMATION
title: DXGK_DISPLAY_INFORMATION
author: windows-driver-content
description: Contains the display information that is passed between the operating system and the display miniport driver when the driver is started or stopped in response to a Plug and Play (PnP) event.
old-location: display\dxgk_display_information.htm
old-project: display
ms.assetid: e6902724-a81b-4a06-8089-a8e98392dc78
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_DISPLAY_INFORMATION, DXGK_DISPLAY_INFORMATION, *PDXGK_DISPLAY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DISPLAY_INFORMATION
req.alt-loc: D3dkmdt.h
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

# DXGK_DISPLAY_INFORMATION structure



## -description
<p>Contains the display information that is passed between the operating system and the display miniport driver when the driver is started or stopped in response to a Plug and Play (PnP) event.</p>


## -syntax

````
typedef struct _DXGK_DISPLAY_INFORMATION {
  UINT                           Width;
  UINT                           Height;
  UINT                           Pitch;
  D3DDDIFORMAT                   ColorFormat;
  PHYSICAL_ADDRESS               PhysicAddress;
  D3DDDI_VIDEO_PRESENT_TARGET_ID TargetId;
  ULONG                          AcpiId;
} DXGK_DISPLAY_INFORMATION, *PDXGK_DISPLAY_INFORMATION;
````


## -struct-fields
<dl>

### -field Width

<dd>
<p>A UINT value that specifies the width of the current display mode in units of pixels.</p>
</dd>

### -field Height

<dd>
<p>A UINT value that specifies the height of the current display mode  in units of pixels.</p>
</dd>

### -field Pitch

<dd>
<p>A UINT value that specifies the total number of bytes contained in one screen line.</p>
</dd>

### -field ColorFormat

<dd>
<p>A value of type <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> that indicates the pixel color format of the current display mode. The driver does not have to support all color formats in the <b>D3DDDIFORMAT</b> structure. For more information on formats that must be supported, see <a href="display.DxgkCbAcquirePostDisplayOwnership">DxgkCbAcquirePostDisplayOwnership</a> and <a href="display.dxgkddireleasepostdisplayownership">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a>.</p>
</dd>

### -field PhysicAddress

<dd>
<p>The physical start address of the frame buffer for the current display mode.</p>
</dd>

### -field TargetId

<dd>
<p>An integer value that specifies the identifier of the video present target on the display adapter that the display device is connected to.</p>
</dd>

### -field AcpiId

<dd>
<p>A ULONG value that specifies the ACPI identifier of the video present target specified by the <b>TargetId</b> member.</p>
<div class="alert"><b>Note</b>  If the video present target is not an ACPI device, this member must be set to zero.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>For more information on the use of the members of <b>DXGK_DISPLAY_INFORMATION</b>, see <a href="display.DxgkCbAcquirePostDisplayOwnership">DxgkCbAcquirePostDisplayOwnership</a> and <a href="display.dxgkddireleasepostdisplayownership">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a>.</p>

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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="display.DxgkCbAcquirePostDisplayOwnership">DxgkCbAcquirePostDisplayOwnership</a>
</dt>
<dt>
<a href="display.dxgkddireleasepostdisplayownership">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_DISPLAY_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
