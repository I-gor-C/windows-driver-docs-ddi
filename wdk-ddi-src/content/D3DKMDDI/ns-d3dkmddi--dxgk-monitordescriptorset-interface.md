---
UID: NS.d3dkmddi._DXGK_MONITORDESCRIPTORSET_INTERFACE
title: DXGK_MONITORDESCRIPTORSET_INTERFACE
author: windows-driver-content
description: The DXGK_MONITORDESCRIPTORSET_INTERFACE structure contains pointers to functions that belong to the Monitor Descriptor Set Interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_monitordescriptorset_interface.htm
ms.assetid: ac492a44-f14e-4b66-9ec1-4f1b04806646
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MONITORDESCRIPTORSET_INTERFACE
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGK_MONITORDESCRIPTORSET_INTERFACE, DXGK_MONITORDESCRIPTORSET_INTERFACE
req.iface: 
---

# DXGK_MONITORDESCRIPTORSET_INTERFACE structure



## -description
<p>The DXGK_MONITORDESCRIPTORSET_INTERFACE structure contains pointers to functions that belong to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568427">Monitor Descriptor Set Interface</a>, which is implemented by the video present network (VidPN) manager.</p>


## -syntax

````
typedef struct _DXGK_MONITORDESCRIPTORSET_INTERFACE {
  DXGKDDI_MONITORDESCRIPTORSET_GETNUMDESCRIPTORS          pfnGetNumDescriptors;
  DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO pfnAcquireFirstDescriptorInfo;
  DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO  pfnAcquireNextDescriptorInfo;
  DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO      pfnReleaseDescriptorInfo;
} DXGK_MONITORDESCRIPTORSET_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>pfnGetNumDescriptors</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/7bfcef0b-1371-4e3b-b5dc-c4c548625c8f">pfnGetNumDescriptors</a> function. </p>
</dd>

### -field <b>pfnAcquireFirstDescriptorInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/228f6947-a7e5-4b76-8224-fac6889fc77a">pfnAcquireFirstDescriptorInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireNextDescriptorInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/34d048df-d4a1-4ef5-b917-791f35de9e3a">pfnAcquireNextDescriptorInfo</a> function. </p>
</dd>

### -field <b>pfnReleaseDescriptorInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/8debdd01-c4e4-4b7c-b4cd-c1143ea7ebaa">pfnReleaseDescriptorInfo</a> function. </p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/228f6947-a7e5-4b76-8224-fac6889fc77a">pfnAcquireFirstDescriptorInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/34d048df-d4a1-4ef5-b917-791f35de9e3a">pfnAcquireNextDescriptorInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7bfcef0b-1371-4e3b-b5dc-c4c548625c8f">pfnGetNumDescriptors</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8debdd01-c4e4-4b7c-b4cd-c1143ea7ebaa">pfnReleaseDescriptorInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_MONITORDESCRIPTORSET_INTERFACE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
