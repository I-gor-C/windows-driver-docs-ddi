---
UID: NS.d3dkmddi.DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
title: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
author: windows-driver-content
description: Specifies limitations on hardware support of multiplane overlays.
old-location: display\dxgk_check_multiplane_overlay_support_return_info.htm
ms.assetid: EA440D77-18E6-4EB4-8621-50C3233DFEA6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.alt-loc: D3dkmddi.h
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO structure



## -description
<p>Specifies limitations on hardware support of multiplane overlays.</p>


## -syntax

````
typedef struct DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO {
  union {
    struct {
      UINT FailingPlane;
      UINT TryAgain;
      UINT Reserved  :27;
    };
    UINT Value;
  };
} DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO;
````


## -struct-fields
<dl>

### -field <b>FailingPlane</b>

<dd>
<p>The zero-based index of the first overlay plane in the list of planes that the hardware cannot support. For example, if planes 0 and 1 could have been supported, but not plane 2, then the driver should set <b>FailingPlane</b> to 2.</p>
<p>Setting this member is equivalent to setting the first 4 bits of the 32-bit <b>Value</b> member (0x0000000F).</p>
</dd>

### -field <b>TryAgain</b>

<dd>
<p>The multiplane overlay configuration isn't supported because of a transient condition, which isn't permanent and should end soon. Therefore the support check call should be tried again and will probably succeed after another one or two VSync intervals.</p>
<p>Setting this member is equivalent to setting the fifth bit of the 32-bit <b>Value</b> member (0x00000010).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 27 bits (0xFFFFFFE0) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A 32-bit value that identifies the hardware support limitations.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>