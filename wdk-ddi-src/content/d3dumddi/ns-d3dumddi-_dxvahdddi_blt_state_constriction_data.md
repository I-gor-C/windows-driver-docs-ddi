---
UID: NS.D3DUMDDI._DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA
title: _DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA
author: windows-driver-content
description: The DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure describes data that specifies the down-sampling of the output.
old-location: display\dxvahdddi_blt_state_constriction_data.htm
old-project: display
ms.assetid: 5bdb39cc-18b3-4a01-b733-f308273399a1
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA, DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# _DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure



## -description
The DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure describes data that specifies the down-sampling of the output. If constriction is enabled, the composed target rectangle is down-sampled to the specified size and then scaled back to the target rectangle. 



## -syntax

````
typedef struct _DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA {
  BOOL Enable;
  SIZE Size;
} DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA;
````


## -struct-fields

### -field Enable

[in] A Boolean value that specifies whether constriction is enabled. The default value is <b>FALSE</b>, which indicates that constriction is disabled. 


### -field Size

[in] A <a href="display.size">SIZE</a> structure that specifies the sampling size to which the output image is reduced. <b>Size</b> should be from (1, 1) to (width, height) of the target rectangle. <b>Size</b> should be (0, 0) to represent no constriction. The default value is (1, 1). 


## -remarks
The Direct3D runtime specifies the DXVAHDDDI_BLT_STATE_CONSTRICTION state in the <b>State</b> member of the <a href="display.d3dddiarg_dxvahd_setvideoprocessbltstate">D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE</a> structure in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_dxvahd_setvideoprocessbltstate.md">SetVideoProcessBltState</a> function. This is specified only if the driver has previously set the DXVAHDDDI_FEATURE_CAPS_CONSTRICTION value in the <b>FeatureCaps</b> member of the <a href="display.dxvahdddi_vpdevcaps">DXVAHDDDI_VPDEVCAPS</a> structure when the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPDEVCAPS value set. 

Sampling sizes of (0, anything) and (anything, 0) are invalid and the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_dxvahd_setvideoprocessbltstate.md">SetVideoProcessBltState</a> function should return an error if these sampling sizes are supplied.

If the supplied sampling size is larger than the size of the target rectangle, then the driver rounds the sampling size to the size of the target rectangle. 


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA is supported beginning with the Windows 7 operating system.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="display.d3dddiarg_dxvahd_setvideoprocessbltstate">D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE</a>
</dt>
<dt>
<a href="display.dxvahdddi_vpdevcaps">DXVAHDDDI_VPDEVCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_dxvahd_setvideoprocessbltstate.md">SetVideoProcessBltState</a>
</dt>
<dt>
<a href="display.size">SIZE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_BLT_STATE_CONSTRICTION_DATA structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

