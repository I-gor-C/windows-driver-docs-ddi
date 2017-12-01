---
UID: NS.d3dumddi._DXVAHDDDI_DEVICE_DESC
title: DXVAHDDDI_DEVICE_DESC
author: windows-driver-content
description: The DXVAHDDDI_DEVICE_DESC structure describes a decode device.
old-location: display\dxvahdddi_device_desc.htm
old-project: display
ms.assetid: c40f4151-a392-463f-888f-d575e6992062
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVAHDDDI_DEVICE_DESC, DXVAHDDDI_DEVICE_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_DEVICE_DESC is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_DEVICE_DESC
req.alt-loc: d3dumddi.h
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

# DXVAHDDDI_DEVICE_DESC structure



## -description
<p>The DXVAHDDDI_DEVICE_DESC structure describes a decode device.  </p>


## -syntax

````
typedef struct _DXVAHDDDI_DEVICE_DESC {
  DXVAHDDDI_CONTENT_DESC *pContentDesc;
  DXVAHDDDI_DEVICE_USAGE Usage;
} DXVAHDDDI_DEVICE_DESC;
````


## -struct-fields
<dl>

### -field <b>pContentDesc</b>

<dd>
<p>[in] A pointer to a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-content-desc.md">DXVAHDDDI_CONTENT_DESC</a> structure that describes how the device decodes content. </p>
</dd>

### -field <b>Usage</b>

<dd>
<p>[in] A <a href="..\d3dumddi\ne-d3dumddi--dxvahdddi-device-usage.md">DXVAHDDDI_DEVICE_USAGE</a>-typed value that indicates how the decode device plays video. </p>
</dd>
</dl>

## -remarks
<p>The driver considers the value in the <b>Usage</b> member and the information to which <b>pContentDesc</b> points to optimize its capabilities. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_DEVICE_DESC is supported beginning with the Windows 7 operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-content-desc.md">DXVAHDDDI_CONTENT_DESC</a>
</dt>
<dt>
<a href="..\d3dumddi\ne-d3dumddi--dxvahdddi-device-usage.md">DXVAHDDDI_DEVICE_USAGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_DEVICE_DESC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
