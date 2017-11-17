---
UID: NE.d3d10umddi.D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS
title: D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS
author: windows-driver-content
description: The D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS enumeration type contains values that identify quality levels for multisample patterns.
old-location: display\d3d10_1_ddiarg_standard_multisample_quality_levels.htm
ms.assetid: 47c285fa-f53a-4e35-ad66-bf14dfc9f80e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS
req.alt-loc: d3d10umddi.h
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS enumeration



## -description
<p>The D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS enumeration type contains values that identify quality levels for multisample patterns. </p>


## -syntax

````
typedef enum D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS { 
  D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN  = 0xffffffff,
  D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN    = 0xfffffffe
} D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS;
````


## -enum-fields
<dl>

### -field <a id="D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN"></a><a id="d3d10_1_ddiarg_standard_multisample_pattern"></a><b>D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN</b>

<dd>
<p>The quality level value for standard multisample pattern. </p>
</dd>

### -field <a id="D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN"></a><a id="d3d10_1_ddiarg_center_multisample_pattern"></a><b>D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN</b>

<dd>
<p>The same number of samples as D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN, except all the samples overlap the center of the pixel. </p>
</dd>
</dl>

## -remarks
<p>The quality level value for standard multisample pattern is D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN. To expose support for the standard multisample pattern for a given sample count, the driver must expose at least one standard quality level through its <a href="https://msdn.microsoft.com/2b6a0ab8-f197-48c3-baf2-305b77b7e8b5">CheckMultisampleQualityLevels</a> function. The D3D runtime can then use the D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN value. If hardware vendors have no proprietary sample patterns that they want to expose and just have the standard pattern, they can just implement the standard pattern for both quality level 0 as well as quality level D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN. In this situation, the driver's <b>CheckMultisampleQualityLevels</b> function would return a pointer to 1 in the <i>pNumQualityLevels</i> parameter. Applications can then request quality level 0 or D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN, and both quality levels provide the same behavior.</p>

<p>For every sample count where D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN is supported, a sibling pattern (D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN) must be supported. D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN has the same number of samples as D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN, except all the samples overlap the center of the pixel.</p>

<p>The quality level value for standard multisample pattern is D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN. To expose support for the standard multisample pattern for a given sample count, the driver must expose at least one standard quality level through its <a href="https://msdn.microsoft.com/2b6a0ab8-f197-48c3-baf2-305b77b7e8b5">CheckMultisampleQualityLevels</a> function. The D3D runtime can then use the D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN value. If hardware vendors have no proprietary sample patterns that they want to expose and just have the standard pattern, they can just implement the standard pattern for both quality level 0 as well as quality level D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN. In this situation, the driver's <b>CheckMultisampleQualityLevels</b> function would return a pointer to 1 in the <i>pNumQualityLevels</i> parameter. Applications can then request quality level 0 or D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN, and both quality levels provide the same behavior.</p>

<p>For every sample count where D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN is supported, a sibling pattern (D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN) must be supported. D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN has the same number of samples as D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN, except all the samples overlap the center of the pixel.</p>

<p>The quality level value for standard multisample pattern is D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN. To expose support for the standard multisample pattern for a given sample count, the driver must expose at least one standard quality level through its <a href="https://msdn.microsoft.com/2b6a0ab8-f197-48c3-baf2-305b77b7e8b5">CheckMultisampleQualityLevels</a> function. The D3D runtime can then use the D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN value. If hardware vendors have no proprietary sample patterns that they want to expose and just have the standard pattern, they can just implement the standard pattern for both quality level 0 as well as quality level D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN. In this situation, the driver's <b>CheckMultisampleQualityLevels</b> function would return a pointer to 1 in the <i>pNumQualityLevels</i> parameter. Applications can then request quality level 0 or D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN, and both quality levels provide the same behavior.</p>

<p>For every sample count where D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN is supported, a sibling pattern (D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN) must be supported. D3D10_1_DDIARG_CENTER_MULTISAMPLE_PATTERN has the same number of samples as D3D10_1_DDIARG_STANDARD_MULTISAMPLE_PATTERN, except all the samples overlap the center of the pixel.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/2b6a0ab8-f197-48c3-baf2-305b77b7e8b5">CheckMultisampleQualityLevels</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_1_DDIARG_STANDARD_MULTISAMPLE_QUALITY_LEVELS enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
