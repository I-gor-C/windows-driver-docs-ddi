---
UID: NS.d3dumddi._DXVAHDDDI_STREAM_STATE_ALPHA_DATA
title: DXVAHDDDI_STREAM_STATE_ALPHA_DATA
author: windows-driver-content
description: The DXVAHDDDI_STREAM_STATE_ALPHA_DATA structure describes stream-state data that specifies the alpha blend level per-plane.
old-location: display\dxvahdddi_stream_state_alpha_data.htm
ms.assetid: 0cd14f0c-5b7b-443b-ab37-c455b4accacb
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_STREAM_STATE_ALPHA_DATA is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_STREAM_STATE_ALPHA_DATA
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
ms.keywords: DXVAHDDDI_STREAM_STATE_ALPHA_DATA, DXVAHDDDI_STREAM_STATE_ALPHA_DATA
req.iface: 
---

# DXVAHDDDI_STREAM_STATE_ALPHA_DATA structure



## -description
<p>The DXVAHDDDI_STREAM_STATE_ALPHA_DATA structure describes stream-state data that specifies the alpha blend level per-plane. </p>


## -syntax

````
typedef struct _DXVAHDDDI_STREAM_STATE_ALPHA_DATA {
  BOOL  Enable;
  FLOAT Alpha;
} DXVAHDDDI_STREAM_STATE_ALPHA_DATA;
````


## -struct-fields
<dl>

### -field <b>Enable</b>

<dd>
<p>[in] A Boolean value that specifies whether the driver should alpha blend. The default value is <b>FALSE</b>, which indicates that alpha blend is disabled. </p>
</dd>

### -field <b>Alpha</b>

<dd>
<p>[in] A FLOAT value in the 0.0 to 1.0 range that describes the alpha level (that is, the transparency level). The default value is 1.0 for opaque. </p>
</dd>
</dl>

## -remarks
<p>The driver multiplies the alpha value with each source pixel and blends the result with the destination pixel. For example, the driver uses the following values to perform the following calculation:</p>

<p>Cs = source pixel color value</p>

<p>Cd = destination pixel color value</p>

<p>As = per-pixel source alpha value [0.0, 1.0]</p>

<p>Ap = per-plane alpha value [0.0, 1.0]</p>

<p>Ae = per-entry palette alpha value [0.0, 1.0] or 1.0 if the driver did not set the DXVAHDDDI_FEATURE_CAPS_ALPHA_PALETTE value in the <b>FeatureCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a> structure when the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPDEVCAPS value set.</p>

<p>Cd = Cs * (As * Ap * Ae) + Cd * (1.0 - As * Ap * Ae)</p>

<p>Ad = per-pixel destination alpha value [0.0, 1.0]</p>

<p>The Ad parameter is set with values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562974">DXVAHDDDI_ALPHA_FILL_MODE</a> enumeration.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_STREAM_STATE_ALPHA_DATA is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562974">DXVAHDDDI_ALPHA_FILL_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_STREAM_STATE_ALPHA_DATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
