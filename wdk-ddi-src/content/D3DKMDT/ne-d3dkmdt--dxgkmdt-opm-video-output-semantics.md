---
UID: NE.d3dkmdt._DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS
title: DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS
author: windows-driver-content
description: The DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS enumeration identifies the semantics of a protected output that is created in a call to the DxgkDdiOPMCreateProtectedOutput function.
old-location: display\dxgkmdt_opm_video_output_semantics.htm
ms.assetid: f399e597-df5e-4dab-8c35-d43803e33bcd
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS enumeration



## -description
<p>The DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS enumeration identifies the semantics of a protected output that is created in a call to the <a href="https://msdn.microsoft.com/8143732e-cef6-49f1-9b20-db6b6ee073e6">DxgkDdiOPMCreateProtectedOutput</a> function. </p>


## -syntax

````
typedef enum _DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS { 
  DXGKMDT_OPM_VOS_COPP_SEMANTICS  = 0,
  DXGKMDT_OPM_VOS_OPM_SEMANTICS   = 1
} DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS;
````


## -enum-fields
<dl>

### -field <a id="DXGKMDT_OPM_VOS_COPP_SEMANTICS"></a><a id="dxgkmdt_opm_vos_copp_semantics"></a><b>DXGKMDT_OPM_VOS_COPP_SEMANTICS</b>

<dd>
<p>Indicates that a protected output has Certified Output Protection Protocol (COPP) semantics. </p>
</dd>

### -field <a id="DXGKMDT_OPM_VOS_OPM_SEMANTICS"></a><a id="dxgkmdt_opm_vos_opm_semantics"></a><b>DXGKMDT_OPM_VOS_OPM_SEMANTICS</b>

<dd>
<p>Indicates that a protected output has Output Protection Management (OPM) semantics. </p>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/8143732e-cef6-49f1-9b20-db6b6ee073e6">DxgkDdiOPMCreateProtectedOutput</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
