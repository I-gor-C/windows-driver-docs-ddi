---
UID: NS.d3dukmdt._D3DDDI_MULTISAMPLINGMETHOD
title: D3DDDI_MULTISAMPLINGMETHOD
author: windows-driver-content
description: The D3DDDI_MULTISAMPLINGMETHOD structure describes a multiple-sampling method.
old-location: display\d3dddi_multisamplingmethod.htm
old-project: display
ms.assetid: 2838cb87-0cd5-4351-a477-00f75eca0896
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_MULTISAMPLINGMETHOD,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_MULTISAMPLINGMETHOD
req.alt-loc: d3dukmdt.h
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

# D3DDDI_MULTISAMPLINGMETHOD structure



## -description
<p>The D3DDDI_MULTISAMPLINGMETHOD structure describes a multiple-sampling method.</p>


## -syntax

````
typedef struct _D3DDDI_MULTISAMPLINGMETHOD {
  UINT NumSamples;
  UINT NumQualityLevels;
} D3DDDI_MULTISAMPLINGMETHOD;
````


## -struct-fields
<dl>

### -field <b>NumSamples</b>

<dd>
<p>[out] The number of subpixels that are used in the multiple-sampling method (for example, 2 for 2x and 8 for 8x multiple-sampling).</p>
</dd>

### -field <b>NumQualityLevels</b>

<dd>
<p>[out] The upper bound on the quality range that is supported for the multiple-sampling method. The range includes values from 0 through the reported maximum quality setting.</p>
</dd>
</dl>

## -remarks
<p>The driver can partition its quality levels for a given multiple-sampling method into as many increments as it requires; however, each incremental step noticeably improves quality of the presented image.</p>

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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557575">DXGKARG_DESCRIBEALLOCATION</a>
</dt>
<dt>
<a href="display.dxgkddidescribeallocation">DxgkDdiDescribeAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_MULTISAMPLINGMETHOD structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
