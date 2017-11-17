---
UID: NE.d3dukmdt._D3DDDI_POOL
title: D3DDDI_POOL
author: windows-driver-content
description: The D3DDDI_POOL enumeration type contains values that identify particular types of memory pool.
old-location: display\d3dddi_pool.htm
ms.assetid: b3f34183-7595-47b6-a2f1-c32650734a04
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_POOL
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
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
req.iface: 
---

# D3DDDI_POOL enumeration



## -description
<p>The D3DDDI_POOL enumeration type contains values that identify particular types of memory pool.</p>


## -syntax

````
typedef enum _D3DDDI_POOL { 
  D3DDDIPOOL_SYSTEMMEM       = 1,
  D3DDDIPOOL_VIDEOMEMORY     = 2,
  D3DDDIPOOL_LOCALVIDMEM     = 3,
  D3DDDIPOOL_NONLOCALVIDMEM  = 4,
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3)
  D3DDDIPOOL_STAGINGMEM      = 5

#endif } D3DDDI_POOL;
````


## -enum-fields
<dl>

### -field <a id="D3DDDIPOOL_SYSTEMMEM"></a><a id="d3dddipool_systemmem"></a><b>D3DDDIPOOL_SYSTEMMEM</b>

<dd>
<p>Resources exist in system memory.</p>
</dd>

### -field <a id="D3DDDIPOOL_VIDEOMEMORY"></a><a id="d3dddipool_videomemory"></a><b>D3DDDIPOOL_VIDEOMEMORY</b>

<dd>
<p>Resources exist in display memory.</p>
</dd>

### -field <a id="D3DDDIPOOL_LOCALVIDMEM"></a><a id="d3dddipool_localvidmem"></a><b>D3DDDIPOOL_LOCALVIDMEM</b>

<dd>
<p>Resources exist in true, local display memory rather than nonlocal display memory (for example, AGP memory).</p>
</dd>

### -field <a id="D3DDDIPOOL_NONLOCALVIDMEM"></a><a id="d3dddipool_nonlocalvidmem"></a><b>D3DDDIPOOL_NONLOCALVIDMEM</b>

<dd>
<p>Resources exist in nonlocal display memory (for example, AGP memory) rather than true, local display memory.</p>
</dd>

### -field <a id="D3DDDIPOOL_STAGINGMEM"></a><a id="d3dddipool_stagingmem"></a><b>D3DDDIPOOL_STAGINGMEM</b>

<dd>
<p>Resources exist in staging memory that the user-mode display driver has allocated. This value indicates to the driver that it should allocate its own staging memory rather than use allocated Direct3D 10Level 9 memory.</p>
<p>Must be supported by WDDM 1.3 and later drivers. Available starting with Windows 8.1.</p>
</dd>
</dl>

## -remarks
<p>Pool memory types are defined as an enumeration type rather than separate flags because the types are all mutually exclusive.</p>

<p>Note that the D3DDDIPOOL_LOCALVIDMEM and D3DDDIPOOL_NONLOCALVIDMEM values are provided as hints to the user-mode display driver so it can improve performance. For more information about these values, see <a href="https://msdn.microsoft.com/b4691de0-d3c9-4a6f-a9f4-aafb22ea3e97">Specifying Memory Type for a Resource</a>.</p>

<p>Pool memory types are defined as an enumeration type rather than separate flags because the types are all mutually exclusive.</p>

<p>Note that the D3DDDIPOOL_LOCALVIDMEM and D3DDDIPOOL_NONLOCALVIDMEM values are provided as hints to the user-mode display driver so it can improve performance. For more information about these values, see <a href="https://msdn.microsoft.com/b4691de0-d3c9-4a6f-a9f4-aafb22ea3e97">Specifying Memory Type for a Resource</a>.</p>

<p>Pool memory types are defined as an enumeration type rather than separate flags because the types are all mutually exclusive.</p>

<p>Note that the D3DDDIPOOL_LOCALVIDMEM and D3DDDIPOOL_NONLOCALVIDMEM values are provided as hints to the user-mode display driver so it can improve performance. For more information about these values, see <a href="https://msdn.microsoft.com/b4691de0-d3c9-4a6f-a9f4-aafb22ea3e97">Specifying Memory Type for a Resource</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542963">D3DDDIARG_CREATERESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_POOL enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
