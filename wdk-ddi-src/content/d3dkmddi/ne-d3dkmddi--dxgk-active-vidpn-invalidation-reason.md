---
UID: NE.d3dkmddi._DXGK_ACTIVE_VIDPN_INVALIDATION_REASON
title: DXGK_ACTIVE_VIDPN_INVALIDATION_REASON
author: windows-driver-content
description: The DXGK_ACTIVE_VIDPN_INVALIDATION_REASON enumeration is used to indicate the reason why an active VidPN is invalidated and a new VidPN is requested.
old-location: display\dxgk_active_vidpn_invalidation_reason.htm
old-project: display
ms.assetid: e1f33307-1bb0-4cdd-aa47-954f6e551582
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_ACTIVE_VIDPN_INVALIDATION_REASON
req.alt-loc: d3dkmddi.h
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

# DXGK_ACTIVE_VIDPN_INVALIDATION_REASON enumeration



## -description
<p>The DXGK_ACTIVE_VIDPN_INVALIDATION_REASON enumeration is used to indicate the reason why an active VidPN is invalidated and a new VidPN is requested.</p>


## -syntax

````
typedef enum _DXGK_ACTIVE_VIDPN_INVALIDATION_REASON { 
  DXGK_AVIR_UNINITIALIZED  = DXGK_RFVR_UNINITIALIZED,
  DXGK_AVIR_HOTKEY         = DXGK_RFVR_HOTKEY,
  DXGK_AVIR_USERMODE       = DXGK_RFVR_USERMODE
} DXGK_ACTIVE_VIDPN_INVALIDATION_REASON;
````


## -enum-fields
<dl>

### -field <a id="DXGK_AVIR_UNINITIALIZED"></a><a id="dxgk_avir_uninitialized"></a><b>DXGK_AVIR_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type DXGK_ACTIVE_VIDPN_INVALIDATION_REASON has not yet been assigned a meaningful value. </p>
</dd>

### -field <a id="DXGK_AVIR_HOTKEY"></a><a id="dxgk_avir_hotkey"></a><b>DXGK_AVIR_HOTKEY</b>

<dd>
<p>Indicates that the user pressed a keyboard shortcut to change the set of monitors (or other display devices) being used to display the desktop. </p>
</dd>

### -field <a id="DXGK_AVIR_USERMODE"></a><a id="dxgk_avir_usermode"></a><b>DXGK_AVIR_USERMODE</b>

<dd>
<p>Indicates that a call to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtinvalidateactivevidpn.md">D3DKMTInvalidateActiveVidPn</a> function has been made in user mode.</p>
</dd>
</dl>

## -remarks


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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtinvalidateactivevidpn.md">D3DKMTInvalidateActiveVidPN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_ACTIVE_VIDPN_INVALIDATION_REASON enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
