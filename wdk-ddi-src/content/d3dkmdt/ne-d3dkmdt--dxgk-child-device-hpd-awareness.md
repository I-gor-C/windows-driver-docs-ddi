---
UID: NE.d3dkmdt._DXGK_CHILD_DEVICE_HPD_AWARENESS
title: DXGK_CHILD_DEVICE_HPD_AWARENESS
author: windows-driver-content
description: The DXGK_CHILD_DEVICE_HPD_AWARENESS enumeration is used to describe the hot plug capabilities of a child device of a display adapter.
old-location: display\dxgk_child_device_hpd_awareness.htm
old-project: display
ms.assetid: daef347a-26d4-46cf-82b4-a5852fe49b71
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CHILD_DEVICE_HPD_AWARENESS
req.alt-loc: d3dkmdt.h
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

# DXGK_CHILD_DEVICE_HPD_AWARENESS enumeration



## -description
<p>The DXGK_CHILD_DEVICE_HPD_AWARENESS enumeration is used to describe the hot plug capabilities of a child device of a display adapter.</p>


## -syntax

````
typedef enum _DXGK_CHILD_DEVICE_HPD_AWARENESS { 
  HpdAwarenessUninitialized    = 0,
  HpdAwarenessAlwaysConnected  = 1,
  HpdAwarenessNone             = 2,
  HpdAwarenessPolled           = 3,
  HpdAwarenessInterruptible    = 4
} DXGK_CHILD_DEVICE_HPD_AWARENESS, *PDXGK_CHILD_DEVICE_HPD_AWARENESS;
````


## -enum-fields
<dl>

### -field <a id="HpdAwarenessUninitialized"></a><a id="hpdawarenessuninitialized"></a><a id="HPDAWARENESSUNINITIALIZED"></a><b>HpdAwarenessUninitialized</b>

<dd>
<p>Indicates that a variable of type DXGK_CHILD_DEVICE_HPD_AWARENESS has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="HpdAwarenessAlwaysConnected"></a><a id="hpdawarenessalwaysconnected"></a><a id="HPDAWARENESSALWAYSCONNECTED"></a><b>HpdAwarenessAlwaysConnected</b>

<dd>
<p>Indicates that the child device is always connected; that is, it does not serve as a connector for external devices.</p>
</dd>

### -field <a id="HpdAwarenessNone"></a><a id="hpdawarenessnone"></a><a id="HPDAWARENESSNONE"></a><b>HpdAwarenessNone</b>

<dd>
<p>Reserved for system use. You should not use this value.</p>
</dd>

### -field <a id="HpdAwarenessPolled"></a><a id="hpdawarenesspolled"></a><a id="HPDAWARENESSPOLLED"></a><b>HpdAwarenessPolled</b>

<dd>
<p>Indicates that the display miniport driver is able to determine whether an external device is connected to the child device by polling the child device.</p>
</dd>

### -field <a id="HpdAwarenessInterruptible"></a><a id="hpdawarenessinterruptible"></a><a id="HPDAWARENESSINTERRUPTIBLE"></a><b>HpdAwarenessInterruptible</b>

<dd>
<p>Indicates that the child device is able to generate an interrupt when an external device is connected or disconnected.</p>
</dd>
</dl>

## -remarks
<p>The <b>ChildCapabilities</b> member of a <a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structure is a <a href="..\dispmprt\ns-dispmprt--dxgk-child-capabilities.md">DXGK_CHILD_CAPABILITIES</a> structure. The <b>HpdAwareness</b> member of a <b>DXGK_CHILD_DEVICE_HPD_AWARENESS</b> structure is a <b>DXGK_CHILD_CAPABILITIES</b>  structure.</p>

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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CHILD_DEVICE_HPD_AWARENESS enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
