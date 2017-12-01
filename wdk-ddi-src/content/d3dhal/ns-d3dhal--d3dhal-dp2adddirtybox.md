---
UID: NS.d3dhal._D3DHAL_DP2ADDDIRTYBOX
title: D3DHAL_DP2ADDDIRTYBOX
author: windows-driver-content
description: DirectX 8.1 and later versions only. D3DHAL_DP2ADDDIRTYBOX is used to specify that a portion of a 3D resource--a volume texture--was dirtied in system memory. Therefore, this volume must be reloaded into video memory before being used.
old-location: display\d3dhal_dp2adddirtybox.htm
old-project: display
ms.assetid: 9cb74a6f-64ae-449a-a1de-6b05419e3387
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2ADDDIRTYBOX, D3DHAL_DP2ADDDIRTYBOX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2ADDDIRTYBOX
req.alt-loc: d3dhal.h
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

# D3DHAL_DP2ADDDIRTYBOX structure



## -description
<p>
   DirectX 8.1 and later versions only.
   </p>
<p>D3DHAL_DP2ADDDIRTYBOX is used to specify that a portion of a 3D resource--a volume texture--was dirtied in system memory. Therefore, this volume must be reloaded into video memory before being used. </p>


## -syntax

````
typedef struct _D3DHAL_DP2ADDDIRTYBOX {
  DWORD  dwSurface;
  D3DBOX DirtyBox;
} D3DHAL_DP2ADDDIRTYBOX, *LPD3DHAL_DP2ADDDIRTYBOX;
````


## -struct-fields
<dl>

### -field <b>dwSurface</b>

<dd>
<p>Specifies the handle to the managed 3D resource that contains a dirtied volume texture.</p>
</dd>

### -field <b>DirtyBox</b>

<dd>
<p>Specifies the volume texture that was marked as dirtied. This is a D3DBOX structure, which is described in the Microsoft Windows SDK documentation. </p>
</dd>
</dl>

## -remarks
<p>D3DHAL_DP2ADDDIRTYBOX, along with the DP2OP_ADDDIRTYBOX token, is used only for driver managed resources. D3DHAL_DP2ADDDIRTYBOX is never sent unless the driver indicates that it manages resources. To indicate that it manages resources, the driver must set the DDCAPS2_CANMANAGERESOURCE bit, in addition to the DDCAPS2_CANMANAGETEXTURE bit, in the <b>dwCaps2</b> member of a DDCORECAPS structure. The driver specifies this <a href="display.ddcorecaps">DDCORECAPS</a> structure in the <b>ddCaps</b> member of a <a href="display.dd_halinfo">DD_HALINFO</a> structure when the driver's <a href="display.drvgetdirectdrawinfo">DrvGetDirectDrawInfo</a> function is called to initialize the DirectDraw component of the driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2command.md">D3DHAL_DP2COMMAND</a>
</dt>
<dt>
<a href="..\d3dhal\ne-d3dhal--d3dhal-dp2operation.md">D3DHAL_DP2OPERATION</a>
</dt>
<dt>
<a href="display.ddcorecaps">DDCORECAPS</a>
</dt>
<dt>
<a href="display.dd_halinfo">DD_HALINFO</a>
</dt>
<dt>
<a href="display.drvgetdirectdrawinfo">DrvGetDirectDrawInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2ADDDIRTYBOX structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
