---
UID: NS.d3dumddi._DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA
title: DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA
author: windows-driver-content
description: The DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure describes data that specifies the down-sampling of the output.
old-location: display\dxvahdddi_blt_state_constriction_data.htm
ms.assetid: 5bdb39cc-18b3-4a01-b733-f308273399a1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA
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
ms.keywords: DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA, DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA
req.iface: 
---

# DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure



## -description
<p>The DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure describes data that specifies the down-sampling of the output. If constriction is enabled, the composed target rectangle is down-sampled to the specified size and then scaled back to the target rectangle. </p>


## -syntax

````
typedef struct _DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA {
  BOOL Enable;
  SIZE Size;
} DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA;
````


## -struct-fields
<dl>

### -field <b>Enable</b>

<dd>
<p>[in] A Boolean value that specifies whether constriction is enabled. The default value is <b>FALSE</b>, which indicates that constriction is disabled. </p>
</dd>

### -field <b>Size</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/dn915850">SIZE</a> structure that specifies the sampling size to which the output image is reduced. <b>Size</b> should be from (1, 1) to (width, height) of the target rectangle. <b>Size</b> should be (0, 0) to represent no constriction. The default value is (1, 1). </p>
</dd>
</dl>

## -remarks
<p>The Direct3D runtime specifies the DXVAHDDDI_BLT_STATE_CONSTRICTION state in the <b>State</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543093">D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE</a> structure in a call to the driver's <a href="https://msdn.microsoft.com/6796372c-279d-427c-a2a4-9b7c99494f53">SetVideoProcessBltState</a> function. This is specified only if the driver has previously set the DXVAHDDDI_FEATURE_CAPS_CONSTRICTION value in the <b>FeatureCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a> structure when the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPDEVCAPS value set. </p>

<p>Sampling sizes of (0, anything) and (anything, 0) are invalid and the driver's <a href="https://msdn.microsoft.com/6796372c-279d-427c-a2a4-9b7c99494f53">SetVideoProcessBltState</a> function should return an error if these sampling sizes are supplied.</p>

<p>If the supplied sampling size is larger than the size of the target rectangle, then the driver rounds the sampling size to the size of the target rectangle. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543093">D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6796372c-279d-427c-a2a4-9b7c99494f53">SetVideoProcessBltState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn915850">SIZE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
