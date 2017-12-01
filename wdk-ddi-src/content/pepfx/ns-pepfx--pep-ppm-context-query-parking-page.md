---
UID: NS.pepfx._PEP_PPM_CONTEXT_QUERY_PARKING_PAGE
title: PEP_PPM_CONTEXT_QUERY_PARKING_PAGE
author: windows-driver-content
description: The PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure describes the parking page for a processor.
old-location: kernel\pep_ppm_context_query_parking_page.htm
old-project: kernel
ms.assetid: F714D6EE-90F9-4FC6-95EB-32225284DC1F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_PPM_CONTEXT_QUERY_PARKING_PAGE, PEP_PPM_CONTEXT_QUERY_PARKING_PAGE, *PPEP_PPM_CONTEXT_QUERY_PARKING_PAGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_PPM_CONTEXT_QUERY_PARKING_PAGE
req.alt-loc: pepfx.h
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

# PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure



## -description
<p>The <b>PEP_PPM_CONTEXT_QUERY_PARKING_PAGE</b> structure describes the parking page for a processor.</p>


## -syntax

````
typedef struct _PEP_PPM_CONTEXT_QUERY_PARKING_PAGE {
  PHYSICAL_ADDRESS PhysicalPageAddress;
  PVOID            VirtualPageAddress;
} PEP_PPM_CONTEXT_QUERY_PARKING_PAGE, *PPEP_PPM_CONTEXT_QUERY_PARKING_PAGE;
````


## -struct-fields
<dl>

### -field <b>PhysicalPageAddress</b>

<dd>
<p>The physical memory address of the parking page.</p>
</dd>

### -field <b>VirtualPageAddress</b>

<dd>
<p>The virtual memory address of the parking page.</p>
</dd>
</dl>

## -remarks
<p>The output buffer for a <a href="kernel.pep_ppm_power_control_query_parking_page_power_control_code">PEP_PPM_POWER_CONTROL_QUERY_PARKING_PAGE</a> power control request is a <b>PEP_PPM_CONTEXT_QUERY_PARKING_PAGE</b> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_ppm_power_control_query_parking_page_power_control_code">PEP_PPM_POWER_CONTROL_QUERY_PARKING_PAGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
