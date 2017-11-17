---
UID: NE.icm.COLORPROFILETYPE
title: COLORPROFILETYPE
author: windows-driver-content
description: The COLORPROFILETYPE enumeration is used to specify the type of color profile.
old-location: print\colorprofiletype.htm
ms.assetid: 756ba822-ace2-4893-a989-9d355434e57c
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: print
req.header: icm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Included in Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: COLORPROFILETYPE
req.alt-loc: icm.h
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
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
req.iface: 
---

# COLORPROFILETYPE enumeration



## -description
<p>The COLORPROFILETYPE enumeration is used to specify the type of color profile.</p>


## -syntax

````
typedef enum  { 
  CPT_ICC   = 0,
  CPT_DMP   = 1,
  CPT_CAMP  = 2,
  CPT_GMMP  = 3
} COLORPROFILETYPE;
````


## -enum-fields
<dl>

### -field <a id="CPT_ICC"></a><a id="cpt_icc"></a><b>CPT_ICC</b>

<dd>
<p>Specifies an ICC profile. If this value is specified, only the CPST_RGB_WORKING_SPACE and CPST_CUSTOM_WORKING_SPACE values of <a href="https://msdn.microsoft.com/library/windows/hardware/ff546012">COLORPROFILESUBTYPE</a> are valid.</p>
</dd>

### -field <a id="CPT_DMP"></a><a id="cpt_dmp"></a><b>CPT_DMP</b>

<dd>
<p>Specifies a WCS device model profile (DMP). If this value is specified, only the CPST_RGB_WORKING_SPACE and CPST_CUSTOM_WORKING_SPACE values of <a href="https://msdn.microsoft.com/library/windows/hardware/ff546012">COLORPROFILESUBTYPE</a> are valid.</p>
</dd>

### -field <a id="CPT_CAMP"></a><a id="cpt_camp"></a><b>CPT_CAMP</b>

<dd>
<p>Specifies a WCS color appearance model profile (CAMP). If this value is specified, only the CPST_NONE value of <a href="https://msdn.microsoft.com/library/windows/hardware/ff546012">COLORPROFILESUBTYPE</a> is valid.</p>
</dd>

### -field <a id="CPT_GMMP"></a><a id="cpt_gmmp"></a><b>CPT_GMMP</b>

<dd>
<p>Specifies a WCS gamut map model profile (GMMP). If this value is specified, only the CPST_PERCEPTUAL, CPST_SATURATION, CPST_RELATIVE_COLORIMETRIC, and CPST_ABSOLUTE_COLORIMETRIC values of <a href="https://msdn.microsoft.com/library/windows/hardware/ff546012">COLORPROFILESUBTYPE</a> are valid. Any one of these values may optionally be combined (in a bitwise OR operation) with CPST_DEFAULT.</p>
</dd>
</dl>

## -remarks
<p>The PCOLORPROFILETYPE and LPCOLORPROFILETYPE data types are defined as pointers to this enumeration:</p>

<p>The PCOLORPROFILETYPE and LPCOLORPROFILETYPE data types are defined as pointers to this enumeration:</p>

<p>The PCOLORPROFILETYPE and LPCOLORPROFILETYPE data types are defined as pointers to this enumeration:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Included in Windows Vista and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Icm.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546012">COLORPROFILESUBTYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20COLORPROFILETYPE enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
