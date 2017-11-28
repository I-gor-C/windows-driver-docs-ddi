---
UID: NS.ksmedia.PKSDS3D_HRTF_FILTER_FORMAT_MSG
title: PKSDS3D_HRTF_FILTER_FORMAT_MSG
author: windows-driver-content
description: The KSDS3D_HRTF_FILTER_FORMAT_MSG structure specifies the filter format to use for a head-relative transfer function (HRTF).
old-location: audio\ksds3d_hrtf_filter_format_msg.htm
old-project: audio
ms.assetid: c0122c96-5bd3-4c1f-85d3-5d4ead5c0c86
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PKSDS3D_HRTF_FILTER_FORMAT_MSG, KSDS3D_HRTF_FILTER_FORMAT_MSG, *PKSDS3D_HRTF_FILTER_FORMAT_MSG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDS3D_HRTF_FILTER_FORMAT_MSG
req.alt-loc: ksmedia.h
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

# PKSDS3D_HRTF_FILTER_FORMAT_MSG structure



## -description
<p>The KSDS3D_HRTF_FILTER_FORMAT_MSG structure specifies the filter format to use for a head-relative transfer function (HRTF).</p>


## -syntax

````
typedef struct {
  KSDS3D_HRTF_FILTER_METHOD  FilterMethod;
  KSDS3D_HRTF_COEFF_FORMAT   CoeffFormat;
  KSDS3D_HRTF_FILTER_VERSION Version;
  ULONG                      Reserved;
} KSDS3D_HRTF_FILTER_FORMAT_MSG, *PKSDS3D_HRTF_FILTER_FORMAT_MSG;
````


## -struct-fields
<dl>

### -field <b>FilterMethod</b>

<dd>
<p>Specifies the filter method to use. Set this parameter to one of the following KSDS3D_HRTF_FILTER_METHOD enumeration values:</p>
<ul>
<li>
<p>DIRECT_FORM</p>
</li>
<li>
<p>CASCADE_FORM</p>
</li>
</ul>
<p>For more information, see the description of the <b>MaxFilterSize</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff537106">KSDS3D_HRTF_INIT_MSG</a>.</p>
</dd>

### -field <b>CoeffFormat</b>

<dd>
<p>Specifies the coefficient format to use. Set this parameter to one of the following KSDS3D_HRTF_COEFF_FORMAT enumeration values:</p>
<ul>
<li>
<p>FLOAT_COEFF specifies floating-point coefficients.</p>
</li>
<li>
<p>SHORT_COEFF specifies 16-bit integer coefficients.</p>
</li>
</ul>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the filter version. Set this parameter to the KSDS3D_HRTF_FILTER_VERSION enumeration value DS3D_HRTF_VERSION_1.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Set to zero.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537353">KSPROPERTY_HRTF3D_FILTER_FORMAT</a> property.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537482">KSPROPSETID_Hrtf3d</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537353">KSPROPERTY_HRTF3D_FILTER_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537482">KSPROPSETID_Hrtf3d</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSDS3D_HRTF_FILTER_FORMAT_MSG structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
